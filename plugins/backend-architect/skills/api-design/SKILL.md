# API Design Skill

**Expert patterns for RESTful and GraphQL API design, OpenAPI specifications, and developer experience**

## Core Principles

1. **Consistency**: Follow established patterns throughout
2. **Discoverability**: API should be self-explanatory
3. **Versioning**: Plan for evolution from day 1
4. **Documentation**: OpenAPI spec is source of truth
5. **Developer Experience**: Make it easy and pleasant to use

---

## REST API Design Rules

### URL Structure

**Resource Naming**:
```
✅ GOOD - Noun-based, plural resources:
/users
/users/{id}
/users/{id}/posts
/posts/{id}/comments

❌ BAD - Verb-based, singular:
/getUser
/user
/createPost
/deleteComment
```

**URL Depth**:
```
✅ GOOD - Maximum 2 levels deep:
/users/{userId}/posts
/posts/{postId}/comments

❌ BAD - Too deep:
/organizations/{orgId}/teams/{teamId}/users/{userId}/posts/{postId}

Instead use:
/posts?userId={userId}&teamId={teamId}
```

**Conventions**:
- Use lowercase
- Use hyphens for multi-word resources: `/user-profiles`
- Avoid file extensions: `/users` not `/users.json`
- Use query params for filtering/sorting: `/users?role=admin&sort=created_at`

### HTTP Methods

| Method | Purpose | Idempotent | Safe | Request Body | Response Body |
|--------|---------|------------|------|--------------|---------------|
| GET | Retrieve resource(s) | ✅ | ✅ | ❌ | ✅ |
| POST | Create resource | ❌ | ❌ | ✅ | ✅ |
| PUT | Replace entire resource | ✅ | ❌ | ✅ | ✅ |
| PATCH | Partial update | ✅* | ❌ | ✅ | ✅ |
| DELETE | Remove resource | ✅ | ❌ | ❌ | ❌/✅ |

*PATCH should be idempotent but not always guaranteed

**Examples**:
```http
# List users
GET /users
→ 200 OK + array

# Get single user
GET /users/123
→ 200 OK + object

# Create user
POST /users
{"email": "user@example.com", "name": "John"}
→ 201 Created + object + Location header

# Replace user (full update)
PUT /users/123
{"email": "new@example.com", "name": "Jane", "role": "admin"}
→ 200 OK + object

# Partial update
PATCH /users/123
{"name": "Jane Doe"}
→ 200 OK + object

# Delete user
DELETE /users/123
→ 204 No Content
```

### HTTP Status Codes

**Success (2xx)**:
```
200 OK                 - Successful GET, PUT, PATCH, DELETE (with body)
201 Created            - Successful POST, resource created
202 Accepted           - Request accepted, processing async
204 No Content         - Successful DELETE, PUT, PATCH (no body)
```

**Client Errors (4xx)**:
```
400 Bad Request        - Invalid JSON, missing required fields
401 Unauthorized       - Missing or invalid authentication
403 Forbidden          - Authenticated but insufficient permissions
404 Not Found          - Resource doesn't exist
405 Method Not Allowed - HTTP method not supported for endpoint
409 Conflict           - Resource conflict (e.g., duplicate email)
422 Unprocessable      - Validation errors (well-formed but invalid)
429 Too Many Requests  - Rate limit exceeded
```

**Server Errors (5xx)**:
```
500 Internal Server    - Unexpected error
502 Bad Gateway        - Invalid response from upstream
503 Service Unavailable - Server overloaded or down for maintenance
504 Gateway Timeout    - Upstream server timeout
```

**Usage Example**:
```python
# POST /users
if not request.json:
    return 400, {"error": "bad_request", "message": "JSON body required"}

if not request.json.get("email"):
    return 422, {"error": "validation_error", "message": "Email is required"}

if db.query(User).filter_by(email=email).first():
    return 409, {"error": "conflict", "message": "Email already exists"}

user = create_user(request.json)
return 201, user, {"Location": f"/users/{user.id}"}
```

---

## Response Formats

### Consistent JSON Structure

**Single Resource**:
```json
{
  "id": "123",
  "email": "user@example.com",
  "name": "John Doe",
  "role": "user",
  "createdAt": "2025-01-20T10:00:00Z",
  "updatedAt": "2025-01-20T10:00:00Z"
}
```

**Collection** (with pagination):
```json
{
  "data": [
    {"id": "1", "name": "User 1"},
    {"id": "2", "name": "User 2"}
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "totalPages": 8,
    "hasNext": true,
    "hasPrev": false
  },
  "links": {
    "self": "/users?page=1&limit=20",
    "next": "/users?page=2&limit=20",
    "prev": null,
    "first": "/users?page=1&limit=20",
    "last": "/users?page=8&limit=20"
  }
}
```

**Error Response**:
```json
{
  "error": "validation_error",
  "message": "Request validation failed",
  "requestId": "abc-123-def-456",
  "timestamp": "2025-01-20T10:00:00Z",
  "details": [
    {
      "field": "email",
      "message": "Invalid email format",
      "code": "INVALID_FORMAT",
      "value": "not-an-email"
    },
    {
      "field": "password",
      "message": "Password must be at least 8 characters",
      "code": "TOO_SHORT"
    }
  ]
}
```

### Naming Conventions

**camelCase** (JavaScript/JSON standard):
```json
{
  "userId": "123",
  "firstName": "John",
  "createdAt": "2025-01-20T10:00:00Z"
}
```

**snake_case** (Python/Ruby standard):
```json
{
  "user_id": "123",
  "first_name": "John",
  "created_at": "2025-01-20T10:00:00Z"
}
```

**Be Consistent**: Pick one and stick to it across entire API

### Timestamps

**Always use ISO 8601 with UTC**:
```json
{
  "createdAt": "2025-01-20T10:00:00Z",
  "updatedAt": "2025-01-20T15:30:00.123Z",
  "publishedAt": "2025-01-20T12:00:00+00:00"
}
```

❌ Don't use:
- Unix timestamps: `1642680000`
- Locale-specific formats: `01/20/2025`
- Without timezone: `2025-01-20T10:00:00`

---

## Filtering, Sorting, Pagination

### Filtering

**Simple filters** (query params):
```
GET /users?role=admin
GET /users?role=admin&status=active
GET /users?createdAfter=2025-01-01
```

**Advanced filters** (JSON in query or POST):
```
GET /users?filter={"role": {"$in": ["admin", "moderator"]}, "age": {"$gte": 18}}

POST /users/search
{
  "filters": {
    "role": ["admin", "moderator"],
    "age": {"min": 18, "max": 65},
    "createdAt": {"after": "2025-01-01"}
  }
}
```

### Sorting

```
GET /users?sort=createdAt           # Ascending (default)
GET /users?sort=-createdAt          # Descending (- prefix)
GET /users?sort=lastName,firstName  # Multiple fields
```

**Response should indicate applied sorting**:
```json
{
  "data": [...],
  "meta": {
    "sort": ["-createdAt", "name"]
  }
}
```

### Pagination

**Offset-based** (simple, not suitable for real-time data):
```
GET /users?page=2&limit=20
GET /users?offset=20&limit=20
```

**Cursor-based** (recommended for real-time, consistent):
```
GET /users?cursor=abc123&limit=20

Response:
{
  "data": [...],
  "pagination": {
    "nextCursor": "def456",
    "prevCursor": "xyz789",
    "hasNext": true,
    "hasPrev": true
  }
}
```

**Defaults**:
```
Default page size: 20
Maximum page size: 100
```

---

## OpenAPI 3.0 Best Practices

### Complete Spec Structure

```yaml
openapi: 3.0.0

info:
  title: API Title
  description: |
    Comprehensive API description with:
    - Feature overview
    - Getting started guide
    - Authentication instructions
  version: 1.0.0
  termsOfService: https://example.com/terms
  contact:
    name: API Support
    email: api@example.com
    url: https://example.com/support
  license:
    name: MIT
    url: https://opensource.org/licenses/MIT

servers:
  - url: https://api.example.com/v1
    description: Production
  - url: https://staging-api.example.com/v1
    description: Staging
  - url: http://localhost:8000/v1
    description: Development

security:
  - bearerAuth: []

tags:
  - name: Users
    description: User management endpoints
  - name: Posts
    description: Post management endpoints

paths:
  # Define endpoints here

components:
  securitySchemes:
    # Define auth schemes

  schemas:
    # Define reusable schemas

  responses:
    # Define reusable responses

  parameters:
    # Define reusable parameters

  examples:
    # Define reusable examples
```

### Schema Definitions

**Use `$ref` for reusability**:
```yaml
components:
  schemas:
    User:
      type: object
      required:
        - id
        - email
        - name
      properties:
        id:
          type: string
          format: uuid
          description: Unique user identifier
          example: "123e4567-e89b-12d3-a456-426614174000"
        email:
          type: string
          format: email
          description: User email address
          example: "user@example.com"
        name:
          type: string
          minLength: 1
          maxLength: 100
          description: User full name
          example: "John Doe"
        role:
          type: string
          enum: [admin, user, guest]
          default: user
          description: User role
        createdAt:
          type: string
          format: date-time
          description: User creation timestamp
          readOnly: true
          example: "2025-01-20T10:00:00Z"
```

**Common Patterns**:
```yaml
# UUID
id:
  type: string
  format: uuid

# Email
email:
  type: string
  format: email
  pattern: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"

# URL
url:
  type: string
  format: uri

# Enum
status:
  type: string
  enum: [draft, published, archived]

# Array
tags:
  type: array
  items:
    type: string
  minItems: 1
  maxItems: 10

# Nested object
address:
  type: object
  properties:
    street:
      type: string
    city:
      type: string
    country:
      type: string
```

### Parameter Definitions

```yaml
parameters:
  PageParam:
    name: page
    in: query
    description: Page number (1-indexed)
    schema:
      type: integer
      minimum: 1
      default: 1

  LimitParam:
    name: limit
    in: query
    description: Number of items per page
    schema:
      type: integer
      minimum: 1
      maximum: 100
      default: 20

  UserIdParam:
    name: userId
    in: path
    required: true
    description: User ID
    schema:
      type: string
      format: uuid
```

**Usage**:
```yaml
paths:
  /users:
    get:
      parameters:
        - $ref: '#/components/parameters/PageParam'
        - $ref: '#/components/parameters/LimitParam'
```

---

## Authentication & Authorization

### JWT Bearer Token

**OpenAPI Definition**:
```yaml
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: |
        JWT bearer token authentication.

        To authenticate:
        1. POST to /auth/login with credentials
        2. Receive JWT token in response
        3. Include in Authorization header: `Bearer <token>`

        Token expires after 1 hour. Use /auth/refresh to get new token.

security:
  - bearerAuth: []  # Applied globally
```

**Login Flow**:
```yaml
paths:
  /auth/login:
    post:
      summary: Login
      description: Authenticate user and receive JWT token
      tags: [Authentication]
      security: []  # No auth required for login
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [email, password]
              properties:
                email:
                  type: string
                  format: email
                password:
                  type: string
                  format: password
            example:
              email: "user@example.com"
              password: "secretpassword"
      responses:
        '200':
          description: Login successful
          content:
            application/json:
              schema:
                type: object
                properties:
                  accessToken:
                    type: string
                    description: JWT access token (1 hour expiry)
                  refreshToken:
                    type: string
                    description: Refresh token (30 days expiry)
                  expiresIn:
                    type: integer
                    description: Access token expiry in seconds
                  tokenType:
                    type: string
                    example: "Bearer"
              example:
                accessToken: "eyJhbGciOiJIUzI1NiIs..."
                refreshToken: "def502003e..."
                expiresIn: 3600
                tokenType: "Bearer"
        '401':
          description: Invalid credentials
```

### API Keys

```yaml
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: X-API-Key
      description: |
        API key authentication.

        Obtain API key from dashboard: https://example.com/dashboard/api-keys

        Include in X-API-Key header:
        ```
        curl -H "X-API-Key: your-api-key-here" https://api.example.com/v1/users
        ```
```

### OAuth 2.0

```yaml
components:
  securitySchemes:
    oauth2:
      type: oauth2
      description: OAuth 2.0 authentication
      flows:
        authorizationCode:
          authorizationUrl: https://example.com/oauth/authorize
          tokenUrl: https://example.com/oauth/token
          refreshUrl: https://example.com/oauth/refresh
          scopes:
            read: Read access to resources
            write: Write access to resources
            admin: Administrative access
```

---

## Versioning Strategies

### URL Versioning (Recommended)

**Structure**:
```
https://api.example.com/v1/users
https://api.example.com/v2/users
```

**OpenAPI**:
```yaml
servers:
  - url: https://api.example.com/v1
    description: Version 1 (current)
  - url: https://api.example.com/v2
    description: Version 2 (beta)
```

**When to Version**:
- Breaking changes to response format
- Removing fields
- Changing field types
- Changing authentication
- Major behavior changes

**Non-Breaking Changes** (no version bump):
- Adding new endpoints
- Adding optional parameters
- Adding new fields to responses
- Increasing rate limits

### Deprecation Policy

```yaml
paths:
  /users/{userId}/profile:
    get:
      deprecated: true
      summary: Get user profile (DEPRECATED)
      description: |
        **DEPRECATED**: This endpoint will be removed in v2.
        Use GET /users/{userId} instead.

        Deprecation timeline:
        - 2025-03-01: Deprecated, still functional
        - 2025-06-01: Will return 410 Gone

      responses:
        '200':
          description: User profile
          headers:
            Deprecation:
              schema:
                type: string
                example: "true"
            Sunset:
              schema:
                type: string
                format: date
                example: "2025-06-01"
```

---

## Rate Limiting

### Rate Limit Headers

```yaml
responses:
  '200':
    description: Successful response
    headers:
      X-RateLimit-Limit:
        description: Request limit per hour
        schema:
          type: integer
          example: 1000
      X-RateLimit-Remaining:
        description: Remaining requests in current window
        schema:
          type: integer
          example: 950
      X-RateLimit-Reset:
        description: Unix timestamp when limit resets
        schema:
          type: integer
          example: 1642694400
      Retry-After:
        description: Seconds until rate limit resets
        schema:
          type: integer
          example: 3600
```

### Rate Limit Exceeded

```yaml
responses:
  '429':
    description: Too many requests
    headers:
      X-RateLimit-Limit:
        schema:
          type: integer
      X-RateLimit-Remaining:
        schema:
          type: integer
          example: 0
      X-RateLimit-Reset:
        schema:
          type: integer
      Retry-After:
        schema:
          type: integer
          example: 3600
    content:
      application/json:
        schema:
          $ref: '#/components/schemas/Error'
        example:
          error: "rate_limit_exceeded"
          message: "Too many requests. Please try again in 3600 seconds."
          retryAfter: 3600
```

### Rate Limiting Strategies

**Per User** (authenticated):
```
1000 requests per hour per user
```

**Per IP** (unauthenticated):
```
100 requests per hour per IP
```

**Tiered** (by plan):
```
Free tier: 100/hour
Pro tier: 1000/hour
Enterprise: 10000/hour
```

---

## Documentation Best Practices

### Endpoint Documentation

```yaml
paths:
  /users:
    get:
      summary: List users                # Short description
      description: |                    # Long description
        Retrieve a paginated list of users with optional filtering.

        ## Filtering
        Use query parameters to filter results:
        - `role`: Filter by user role
        - `status`: Filter by account status
        - `createdAfter`: Filter by creation date

        ## Sorting
        Use `sort` parameter with field name. Prefix with `-` for descending:
        - `sort=createdAt`: Oldest first
        - `sort=-createdAt`: Newest first

        ## Permissions
        Requires `read:users` permission.
```

### Examples

**Provide realistic examples**:
```yaml
requestBody:
  content:
    application/json:
      schema:
        $ref: '#/components/schemas/CreateUserRequest'
      examples:
        adminUser:
          summary: Create admin user
          value:
            email: "admin@example.com"
            name: "Admin User"
            role: "admin"
            permissions: ["read:all", "write:all"]
        regularUser:
          summary: Create regular user
          value:
            email: "user@example.com"
            name: "Regular User"
            role: "user"
```

### Code Generation

OpenAPI specs enable automatic code generation:
- **Client SDKs**: TypeScript, Python, Java, Go
- **Server Stubs**: FastAPI, Express, Spring
- **Documentation**: Swagger UI, ReDoc, Postman

---

## Best Practices Checklist

- [ ] RESTful URLs (nouns, not verbs)
- [ ] Correct HTTP methods and status codes
- [ ] Consistent JSON naming (camelCase or snake_case)
- [ ] ISO 8601 timestamps with UTC
- [ ] Pagination for list endpoints
- [ ] Filtering and sorting support
- [ ] Authentication documented
- [ ] Rate limiting implemented
- [ ] Versioning strategy defined
- [ ] Error responses standardized
- [ ] All endpoints documented in OpenAPI
- [ ] Request/response examples provided
- [ ] Deprecation policy established
- [ ] CORS configured correctly
- [ ] HTTPS only (no HTTP)

---

**Version**: 1.0
**Last Updated**: January 2025
**Use Cases**: REST API design, OpenAPI specifications, API documentation
