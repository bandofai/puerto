# API Implementation Skill

**Production patterns for REST and GraphQL API development with validation, error handling, and security**

## Core Principles

1. **Consistency**: Uniform patterns across all endpoints
2. **Validation**: Trust nothing from the client
3. **Security**: Defense in depth, assume breach
4. **Performance**: Optimize for scale from day one
5. **Testability**: Easy to test, easy to trust

---

## REST API Implementation

### Request Validation

**Always validate inputs with schema-based validation**:

```typescript
import { z } from 'zod';

// Define schema
const createUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(1).max(100),
  password: z.string().min(8),
  age: z.number().int().positive().optional(),
  role: z.enum(['admin', 'user', 'guest']).default('user'),
});

// Validate in middleware
function validateRequest(schema: z.ZodSchema) {
  return (req, res, next) => {
    try {
      req.body = schema.parse(req.body);
      next();
    } catch (error) {
      res.status(422).json({
        error: 'validation_error',
        message: 'Request validation failed',
        details: error.errors.map(e => ({
          field: e.path.join('.'),
          message: e.message,
        })),
      });
    }
  };
}

// Use in route
router.post('/users', validateRequest(createUserSchema), async (req, res) => {
  // req.body is now type-safe and validated
});
```

**Common validation patterns**:
```typescript
// UUID validation
const uuidSchema = z.string().uuid();

// Email validation
const emailSchema = z.string().email();

// Enum validation
const roleSchema = z.enum(['admin', 'user', 'guest']);

// Date validation
const dateSchema = z.string().datetime();

// Array validation
const tagsSchema = z.array(z.string()).min(1).max(10);

// Nested object validation
const addressSchema = z.object({
  street: z.string(),
  city: z.string(),
  zip: z.string().regex(/^\d{5}$/),
});

// Conditional validation
const userSchema = z.object({
  role: z.enum(['admin', 'user']),
  permissions: z.array(z.string()).optional(),
}).refine(data => {
  // Admins must have permissions
  if (data.role === 'admin' && !data.permissions) {
    return false;
  }
  return true;
}, 'Admins must have permissions defined');
```

### Error Handling

**Consistent error response format**:

```typescript
interface ApiError {
  error: string;           // Machine-readable error code
  message: string;         // Human-readable message
  requestId?: string;      // For tracing
  timestamp?: string;      // ISO 8601 timestamp
  details?: Array<{        // Validation errors
    field: string;
    message: string;
    code?: string;
  }>;
}

// Error classes
class ApiError extends Error {
  constructor(
    public statusCode: number,
    public error: string,
    message: string,
    public details?: any[]
  ) {
    super(message);
  }
}

class BadRequestError extends ApiError {
  constructor(message: string, details?: any[]) {
    super(400, 'bad_request', message, details);
  }
}

class UnauthorizedError extends ApiError {
  constructor(message: string = 'Authentication required') {
    super(401, 'unauthorized', message);
  }
}

class ForbiddenError extends ApiError {
  constructor(message: string = 'Insufficient permissions') {
    super(403, 'forbidden', message);
  }
}

class NotFoundError extends ApiError {
  constructor(message: string = 'Resource not found') {
    super(404, 'not_found', message);
  }
}

class ConflictError extends ApiError {
  constructor(message: string, details?: any[]) {
    super(409, 'conflict', message, details);
  }
}

class ValidationError extends ApiError {
  constructor(message: string, details: any[]) {
    super(422, 'validation_error', message, details);
  }
}

// Error handler middleware
function errorHandler(err, req, res, next) {
  // Generate request ID for tracing
  const requestId = req.id || crypto.randomUUID();

  // Log error
  logger.error({
    requestId,
    error: err.message,
    stack: err.stack,
    path: req.path,
    method: req.method,
  });

  // Handle known errors
  if (err instanceof ApiError) {
    return res.status(err.statusCode).json({
      error: err.error,
      message: err.message,
      details: err.details,
      requestId,
      timestamp: new Date().toISOString(),
    });
  }

  // Handle unknown errors (don't expose internals)
  res.status(500).json({
    error: 'internal_error',
    message: 'An unexpected error occurred',
    requestId,
    timestamp: new Date().toISOString(),
  });
}
```

### Pagination

**Cursor-based pagination** (recommended for real-time data):

```typescript
interface CursorPaginationParams {
  cursor?: string;
  limit: number;
}

interface CursorPaginationResult<T> {
  data: T[];
  pagination: {
    nextCursor: string | null;
    prevCursor: string | null;
    hasNext: boolean;
    hasPrev: boolean;
  };
}

async function paginateWithCursor<T>(
  query: any,
  params: CursorPaginationParams
): Promise<CursorPaginationResult<T>> {
  const { cursor, limit } = params;

  // Decode cursor (base64 encoded ID)
  const decodedCursor = cursor ?
    Buffer.from(cursor, 'base64').toString() : null;

  // Fetch limit + 1 to check if there's more
  const items = await query
    .where(decodedCursor ? `id > :cursor` : '1=1', { cursor: decodedCursor })
    .limit(limit + 1)
    .getMany();

  const hasNext = items.length > limit;
  const data = hasNext ? items.slice(0, -1) : items;

  const nextCursor = hasNext ?
    Buffer.from(data[data.length - 1].id).toString('base64') : null;

  return {
    data,
    pagination: {
      nextCursor,
      prevCursor: null, // Implement if bidirectional needed
      hasNext,
      hasPrev: false,
    },
  };
}
```

**Offset-based pagination** (simpler, but not for real-time):

```typescript
interface OffsetPaginationParams {
  page: number;
  limit: number;
}

interface OffsetPaginationResult<T> {
  data: T[];
  pagination: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
    hasNext: boolean;
    hasPrev: boolean;
  };
}

async function paginateWithOffset<T>(
  query: any,
  params: OffsetPaginationParams
): Promise<OffsetPaginationResult<T>> {
  const { page, limit } = params;
  const offset = (page - 1) * limit;

  const [data, total] = await query
    .skip(offset)
    .take(limit)
    .getManyAndCount();

  const totalPages = Math.ceil(total / limit);

  return {
    data,
    pagination: {
      page,
      limit,
      total,
      totalPages,
      hasNext: page < totalPages,
      hasPrev: page > 1,
    },
  };
}
```

### Filtering and Sorting

```typescript
interface FilterParams {
  role?: string;
  status?: string;
  createdAfter?: string;
  createdBefore?: string;
  search?: string;
}

interface SortParams {
  sort?: string; // e.g., "-createdAt,name"
}

function applyFilters(query, filters: FilterParams) {
  if (filters.role) {
    query = query.andWhere('user.role = :role', { role: filters.role });
  }

  if (filters.status) {
    query = query.andWhere('user.status = :status', { status: filters.status });
  }

  if (filters.createdAfter) {
    query = query.andWhere('user.createdAt >= :after', {
      after: filters.createdAfter
    });
  }

  if (filters.search) {
    query = query.andWhere(
      '(user.name ILIKE :search OR user.email ILIKE :search)',
      { search: `%${filters.search}%` }
    );
  }

  return query;
}

function applySorting(query, sort?: string) {
  if (!sort) {
    return query.orderBy('user.createdAt', 'DESC');
  }

  const sortFields = sort.split(',');

  sortFields.forEach((field, index) => {
    const descending = field.startsWith('-');
    const fieldName = descending ? field.substring(1) : field;
    const direction = descending ? 'DESC' : 'ASC';

    if (index === 0) {
      query = query.orderBy(`user.${fieldName}`, direction);
    } else {
      query = query.addOrderBy(`user.${fieldName}`, direction);
    }
  });

  return query;
}
```

### Rate Limiting

```typescript
import rateLimit from 'express-rate-limit';
import RedisStore from 'rate-limit-redis';
import { Redis } from 'ioredis';

const redis = new Redis(process.env.REDIS_URL);

// Create rate limiter
function createRateLimiter(options: {
  max: number;
  window: string; // '1m', '1h', '1d'
  message?: string;
}) {
  const windowMs = parseWindow(options.window);

  return rateLimit({
    store: new RedisStore({
      client: redis,
      prefix: 'rl:',
    }),
    windowMs,
    max: options.max,
    standardHeaders: true, // Return rate limit info in headers
    legacyHeaders: false,
    handler: (req, res) => {
      res.status(429).json({
        error: 'rate_limit_exceeded',
        message: options.message || 'Too many requests',
        retryAfter: Math.ceil(windowMs / 1000),
      });
    },
  });
}

// Usage
const authLimiter = createRateLimiter({ max: 5, window: '15m' });
router.post('/auth/login', authLimiter, loginHandler);

const apiLimiter = createRateLimiter({ max: 100, window: '1h' });
router.use('/api', apiLimiter);

function parseWindow(window: string): number {
  const match = window.match(/^(\d+)(m|h|d)$/);
  if (!match) throw new Error('Invalid window format');

  const [, amount, unit] = match;
  const multipliers = { m: 60_000, h: 3600_000, d: 86400_000 };
  return parseInt(amount) * multipliers[unit];
}
```

### API Versioning

**URL-based versioning** (recommended):

```typescript
// v1/users.route.ts
const routerV1 = Router();
routerV1.get('/users', getUsersV1);

// v2/users.route.ts
const routerV2 = Router();
routerV2.get('/users', getUsersV2);

// app.ts
app.use('/api/v1', routerV1);
app.use('/api/v2', routerV2);
```

**Header-based versioning**:

```typescript
function versionMiddleware(req, res, next) {
  const version = req.headers['api-version'] || '1';
  req.apiVersion = version;
  next();
}

router.get('/users', versionMiddleware, (req, res) => {
  if (req.apiVersion === '2') {
    return getUsersV2(req, res);
  }
  return getUsersV1(req, res);
});
```

---

## GraphQL Implementation

### Resolver Pattern

```typescript
import { GraphQLError } from 'graphql';

export const resolvers = {
  Query: {
    user: async (parent, { id }, context) => {
      // Check authentication
      if (!context.user) {
        throw new GraphQLError('Authentication required', {
          extensions: { code: 'UNAUTHENTICATED' },
        });
      }

      // Fetch data
      const user = await context.dataSources.userService.findById(id);

      if (!user) {
        throw new GraphQLError('User not found', {
          extensions: { code: 'NOT_FOUND' },
        });
      }

      return user;
    },

    users: async (parent, { filter, pagination }, context) => {
      if (!context.user?.permissions.includes('read:users')) {
        throw new GraphQLError('Insufficient permissions', {
          extensions: { code: 'FORBIDDEN' },
        });
      }

      return await context.dataSources.userService.findAll({
        filter,
        pagination,
      });
    },
  },

  Mutation: {
    createUser: async (parent, { input }, context) => {
      // Validate input
      const validated = createUserSchema.parse(input);

      // Check permissions
      if (!context.user?.permissions.includes('create:users')) {
        throw new GraphQLError('Insufficient permissions', {
          extensions: { code: 'FORBIDDEN' },
        });
      }

      // Check for duplicates
      const existing = await context.dataSources.userService
        .findByEmail(validated.email);

      if (existing) {
        throw new GraphQLError('Email already exists', {
          extensions: {
            code: 'CONFLICT',
            field: 'email',
          },
        });
      }

      return await context.dataSources.userService.create(validated);
    },
  },

  User: {
    // Field resolver
    posts: async (parent, args, context) => {
      return await context.dataSources.postService
        .findByUserId(parent.id);
    },
  },
};
```

### DataLoader for N+1 Prevention

```typescript
import DataLoader from 'dataloader';

// Create DataLoader
const userLoader = new DataLoader(async (userIds: string[]) => {
  const users = await userRepository.findByIds(userIds);

  // Return in same order as input
  const userMap = new Map(users.map(u => [u.id, u]));
  return userIds.map(id => userMap.get(id) || null);
});

// Use in resolver
const postResolver = {
  author: async (parent, args, context) => {
    // Batches and caches requests
    return context.loaders.userLoader.load(parent.authorId);
  },
};
```

---

## Performance Optimization

### Database Query Optimization

```typescript
// Bad: N+1 query problem
const users = await userRepository.find();
for (const user of users) {
  user.posts = await postRepository.findByUserId(user.id); // N queries
}

// Good: Single query with JOIN
const users = await userRepository
  .createQueryBuilder('user')
  .leftJoinAndSelect('user.posts', 'post')
  .getMany();

// Good: Use DataLoader (GraphQL)
const users = await userRepository.find();
const userIds = users.map(u => u.id);
const posts = await context.loaders.postLoader.loadMany(userIds);
```

### Response Caching

```typescript
import { Redis } from 'ioredis';

const redis = new Redis();

// Cache middleware
function cacheResponse(ttl: number) {
  return async (req, res, next) => {
    const key = `cache:${req.path}:${JSON.stringify(req.query)}`;

    // Try cache first
    const cached = await redis.get(key);
    if (cached) {
      return res.json(JSON.parse(cached));
    }

    // Override res.json to cache response
    const originalJson = res.json.bind(res);
    res.json = (data) => {
      redis.setex(key, ttl, JSON.stringify(data));
      return originalJson(data);
    };

    next();
  };
}

// Usage
router.get('/users', cacheResponse(60), getUsersHandler);
```

### Response Compression

```typescript
import compression from 'compression';

app.use(compression({
  filter: (req, res) => {
    if (req.headers['x-no-compression']) {
      return false;
    }
    return compression.filter(req, res);
  },
  level: 6, // Compression level (0-9)
}));
```

---

## Security Best Practices

### Input Sanitization

```typescript
import sanitizeHtml from 'sanitize-html';
import validator from 'validator';

function sanitizeInput(input: any): any {
  if (typeof input === 'string') {
    // Remove HTML tags
    input = sanitizeHtml(input, { allowedTags: [] });

    // Escape special characters
    input = validator.escape(input);
  }

  if (typeof input === 'object') {
    for (const key in input) {
      input[key] = sanitizeInput(input[key]);
    }
  }

  return input;
}

// Use in middleware
app.use((req, res, next) => {
  req.body = sanitizeInput(req.body);
  req.query = sanitizeInput(req.query);
  next();
});
```

### SQL Injection Prevention

```typescript
// Bad: String concatenation
const users = await db.query(
  `SELECT * FROM users WHERE email = '${email}'` // VULNERABLE!
);

// Good: Parameterized queries
const users = await db.query(
  'SELECT * FROM users WHERE email = $1',
  [email]
);

// Good: Query builder
const users = await userRepository
  .createQueryBuilder('user')
  .where('user.email = :email', { email })
  .getMany();
```

### Security Headers

```typescript
import helmet from 'helmet';

app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      scriptSrc: ["'self'"],
      imgSrc: ["'self'", 'data:', 'https:'],
    },
  },
  hsts: {
    maxAge: 31536000,
    includeSubDomains: true,
    preload: true,
  },
}));
```

---

## Testing Patterns

### Unit Test Example

```typescript
describe('UserService', () => {
  let userService: UserService;
  let mockRepository: MockRepository;

  beforeEach(() => {
    mockRepository = createMockRepository();
    userService = new UserService(mockRepository);
  });

  it('should create user with hashed password', async () => {
    const userData = {
      email: 'test@example.com',
      password: 'password123',
    };

    const user = await userService.create(userData);

    expect(user.passwordHash).not.toBe(userData.password);
    expect(user.passwordHash).toMatch(/^\$2[aby]\$/);
  });

  it('should throw ConflictError for duplicate email', async () => {
    mockRepository.findByEmail.mockResolvedValue({ id: '123' });

    await expect(
      userService.create({ email: 'test@example.com', password: 'pass' })
    ).rejects.toThrow(ConflictError);
  });
});
```

---

## Best Practices Checklist

- [ ] All inputs validated with schemas
- [ ] Consistent error response format
- [ ] Proper HTTP status codes
- [ ] Authentication on protected routes
- [ ] Authorization checks before operations
- [ ] Rate limiting on all routes
- [ ] Pagination for list endpoints
- [ ] N+1 query prevention
- [ ] Response caching where appropriate
- [ ] Security headers configured
- [ ] SQL injection prevention
- [ ] XSS prevention (input sanitization)
- [ ] CORS configured correctly
- [ ] Comprehensive logging
- [ ] Request ID tracing
- [ ] Unit tests >= 85% coverage
- [ ] Integration tests for critical paths

---

**Version**: 1.0
**Last Updated**: January 2025
**Use Cases**: REST/GraphQL API implementation, validation, error handling, security
