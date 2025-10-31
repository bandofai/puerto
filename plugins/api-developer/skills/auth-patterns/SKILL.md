# Authentication Patterns Skill

**Security best practices for JWT, OAuth 2.0, API keys, and authorization patterns**

## Core Principles

1. **Security First**: Assume breach, defense in depth
2. **Standards-Based**: Use proven protocols (OAuth 2.0, JWT)
3. **Least Privilege**: Grant minimum necessary permissions
4. **Fail Secure**: When in doubt, deny access
5. **Audit Everything**: Log all authentication/authorization events

---

## JWT Authentication

### Token Structure

**Payload Design**:
```typescript
interface JWTPayload {
  // Standard claims
  iss: string;        // Issuer (your API domain)
  sub: string;        // Subject (user ID)
  aud: string;        // Audience (your API domain)
  exp: number;        // Expiration (Unix timestamp)
  iat: number;        // Issued at (Unix timestamp)
  jti: string;        // JWT ID (unique token identifier)

  // Custom claims
  email: string;      // User email
  role: string;       // User role
  permissions?: string[]; // Specific permissions
}
```

### Token Generation

```typescript
import jwt from 'jsonwebtoken';
import crypto from 'crypto';

class TokenService {
  private readonly ACCESS_TOKEN_SECRET = process.env.JWT_SECRET!;
  private readonly REFRESH_TOKEN_SECRET = process.env.JWT_REFRESH_SECRET!;
  private readonly ACCESS_TOKEN_EXPIRY = '15m';
  private readonly REFRESH_TOKEN_EXPIRY = '7d';

  generateAccessToken(user: User): string {
    return jwt.sign(
      {
        sub: user.id,
        email: user.email,
        role: user.role,
        permissions: user.permissions,
      },
      this.ACCESS_TOKEN_SECRET,
      {
        expiresIn: this.ACCESS_TOKEN_EXPIRY,
        issuer: 'api.example.com',
        audience: 'api.example.com',
        jwtid: crypto.randomUUID(),
      }
    );
  }

  generateRefreshToken(userId: string): string {
    return jwt.sign(
      {
        sub: userId,
        type: 'refresh',
      },
      this.REFRESH_TOKEN_SECRET,
      {
        expiresIn: this.REFRESH_TOKEN_EXPIRY,
        issuer: 'api.example.com',
        jwtid: crypto.randomUUID(),
      }
    );
  }

  verifyAccessToken(token: string): JWTPayload {
    return jwt.verify(token, this.ACCESS_TOKEN_SECRET, {
      issuer: 'api.example.com',
      audience: 'api.example.com',
    }) as JWTPayload;
  }

  verifyRefreshToken(token: string): { sub: string; jti: string } {
    return jwt.verify(token, this.REFRESH_TOKEN_SECRET, {
      issuer: 'api.example.com',
    }) as { sub: string; jti: string };
  }
}
```

### Token Refresh Flow

```typescript
class AuthService {
  async refreshToken(refreshToken: string) {
    try {
      // Verify refresh token
      const payload = tokenService.verifyRefreshToken(refreshToken);

      // Check if token is revoked
      const isRevoked = await tokenBlacklist.isRevoked(payload.jti);
      if (isRevoked) {
        throw new UnauthorizedError('Token has been revoked');
      }

      // Get user
      const user = await userRepository.findById(payload.sub);
      if (!user) {
        throw new UnauthorizedError('User not found');
      }

      // Generate new tokens
      const newAccessToken = tokenService.generateAccessToken(user);
      const newRefreshToken = tokenService.generateRefreshToken(user.id);

      // Revoke old refresh token (token rotation)
      await tokenBlacklist.revoke(payload.jti);

      // Store new refresh token hash
      await refreshTokenRepository.store(user.id, newRefreshToken);

      return {
        accessToken: newAccessToken,
        refreshToken: newRefreshToken,
        expiresIn: 900, // 15 minutes in seconds
        tokenType: 'Bearer',
      };
    } catch (error) {
      if (error instanceof jwt.TokenExpiredError) {
        throw new UnauthorizedError('Refresh token expired');
      }
      throw new UnauthorizedError('Invalid refresh token');
    }
  }
}
```

### Token Blacklist (Redis)

```typescript
import { Redis } from 'ioredis';

class TokenBlacklist {
  private redis: Redis;

  constructor() {
    this.redis = new Redis(process.env.REDIS_URL);
  }

  async revoke(tokenId: string, expiresIn: number = 900) {
    await this.redis.setex(`blacklist:${tokenId}`, expiresIn, '1');
  }

  async isRevoked(tokenId: string): Promise<boolean> {
    const result = await this.redis.get(`blacklist:${tokenId}`);
    return result === '1';
  }

  async revokeAllUserTokens(userId: string) {
    await this.redis.sadd(`revoked:user:${userId}`, '1');
  }

  async isUserTokensRevoked(userId: string): Promise<boolean> {
    const result = await this.redis.sismember(`revoked:user:${userId}`, '1');
    return result === 1;
  }
}
```

---

## Password Security

### Hashing

```typescript
import bcrypt from 'bcrypt';
import crypto from 'crypto';

class PasswordService {
  private readonly SALT_ROUNDS = 12; // 12 is recommended minimum

  async hash(password: string): Promise<string> {
    // Validate password strength first
    this.validatePasswordStrength(password);

    return await bcrypt.hash(password, this.SALT_ROUNDS);
  }

  async verify(password: string, hash: string): Promise<boolean> {
    try {
      return await bcrypt.compare(password, hash);
    } catch {
      return false;
    }
  }

  validatePasswordStrength(password: string): void {
    const errors: string[] = [];

    if (password.length < 8) {
      errors.push('Password must be at least 8 characters');
    }

    if (password.length > 128) {
      errors.push('Password must be less than 128 characters');
    }

    if (!/[a-z]/.test(password)) {
      errors.push('Password must contain lowercase letter');
    }

    if (!/[A-Z]/.test(password)) {
      errors.push('Password must contain uppercase letter');
    }

    if (!/[0-9]/.test(password)) {
      errors.push('Password must contain number');
    }

    if (!/[^a-zA-Z0-9]/.test(password)) {
      errors.push('Password must contain special character');
    }

    // Check against common passwords
    if (this.isCommonPassword(password)) {
      errors.push('Password is too common');
    }

    if (errors.length > 0) {
      throw new ValidationError('Password validation failed', errors);
    }
  }

  private isCommonPassword(password: string): boolean {
    const common = [
      'password', 'password123', '12345678', 'qwerty',
      'abc123', 'monkey', '1234567', 'letmein',
    ];
    return common.includes(password.toLowerCase());
  }

  generateSecureRandom(length: number = 32): string {
    return crypto.randomBytes(length).toString('hex');
  }
}
```

### Password Reset Flow

```typescript
class PasswordResetService {
  async requestReset(email: string) {
    const user = await userRepository.findByEmail(email);
    if (!user) {
      // Don't reveal if email exists
      return { success: true };
    }

    // Generate secure token
    const token = crypto.randomBytes(32).toString('hex');
    const tokenHash = await bcrypt.hash(token, 10);

    // Store token with expiry (1 hour)
    await passwordResetRepository.create({
      userId: user.id,
      tokenHash,
      expiresAt: new Date(Date.now() + 3600000),
    });

    // Send email with reset link
    await emailService.sendPasswordReset(user.email, token);

    return { success: true };
  }

  async resetPassword(token: string, newPassword: string) {
    // Find reset request
    const resets = await passwordResetRepository.findPending();

    let resetRequest = null;
    for (const reset of resets) {
      const isValid = await bcrypt.compare(token, reset.tokenHash);
      if (isValid) {
        resetRequest = reset;
        break;
      }
    }

    if (!resetRequest) {
      throw new BadRequestError('Invalid or expired reset token');
    }

    // Check expiry
    if (resetRequest.expiresAt < new Date()) {
      throw new BadRequestError('Reset token has expired');
    }

    // Update password
    const passwordHash = await passwordService.hash(newPassword);
    await userRepository.updatePassword(resetRequest.userId, passwordHash);

    // Delete reset request
    await passwordResetRepository.delete(resetRequest.id);

    // Revoke all existing tokens for this user
    await tokenBlacklist.revokeAllUserTokens(resetRequest.userId);

    return { success: true };
  }
}
```

---

## OAuth 2.0

### Authorization Code Flow

```typescript
import { Strategy as GoogleStrategy } from 'passport-google-oauth20';
import { Strategy as GitHubStrategy } from 'passport-github2';
import passport from 'passport';

// Configure Google OAuth
passport.use(
  new GoogleStrategy(
    {
      clientID: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
      callbackURL: '/auth/google/callback',
      scope: ['profile', 'email'],
    },
    async (accessToken, refreshToken, profile, done) => {
      try {
        // Find or create user
        let user = await userRepository.findByProviderId(
          'google',
          profile.id
        );

        if (!user) {
          // Check if email already exists
          const existingUser = await userRepository.findByEmail(
            profile.emails![0].value
          );

          if (existingUser) {
            // Link accounts
            await userRepository.linkProvider(existingUser.id, {
              provider: 'google',
              providerId: profile.id,
            });
            user = existingUser;
          } else {
            // Create new user
            user = await userRepository.create({
              email: profile.emails![0].value,
              name: profile.displayName,
              avatar: profile.photos![0]?.value,
              provider: 'google',
              providerId: profile.id,
              emailVerified: true,
            });
          }
        }

        // Update OAuth tokens
        await oauthTokenRepository.upsert({
          userId: user.id,
          provider: 'google',
          accessToken,
          refreshToken,
          expiresAt: new Date(Date.now() + 3600000),
        });

        done(null, user);
      } catch (error) {
        done(error);
      }
    }
  )
);

// OAuth routes
router.get('/auth/google',
  passport.authenticate('google', {
    scope: ['profile', 'email'],
  })
);

router.get('/auth/google/callback',
  passport.authenticate('google', {
    session: false,
    failureRedirect: '/login?error=oauth_failed',
  }),
  (req, res) => {
    // Generate JWT tokens
    const accessToken = tokenService.generateAccessToken(req.user);
    const refreshToken = tokenService.generateRefreshToken(req.user.id);

    // Redirect to frontend with tokens
    res.redirect(
      `${process.env.FRONTEND_URL}/auth/callback?` +
      `access_token=${accessToken}&refresh_token=${refreshToken}`
    );
  }
);
```

### OAuth Token Refresh

```typescript
class OAuthService {
  async refreshGoogleToken(userId: string) {
    const stored = await oauthTokenRepository.findByUserAndProvider(
      userId,
      'google'
    );

    if (!stored || !stored.refreshToken) {
      throw new Error('No refresh token available');
    }

    const response = await fetch('https://oauth2.googleapis.com/token', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        client_id: process.env.GOOGLE_CLIENT_ID!,
        client_secret: process.env.GOOGLE_CLIENT_SECRET!,
        refresh_token: stored.refreshToken,
        grant_type: 'refresh_token',
      }),
    });

    const data = await response.json();

    // Update stored tokens
    await oauthTokenRepository.update(stored.id, {
      accessToken: data.access_token,
      expiresAt: new Date(Date.now() + data.expires_in * 1000),
    });

    return data.access_token;
  }
}
```

---

## API Keys

### Generation and Storage

```typescript
class ApiKeyService {
  async generate(userId: string, name: string, scopes: string[]) {
    // Generate secure random key
    const key = `sk_${crypto.randomBytes(32).toString('hex')}`;

    // Hash key before storing (NEVER store plain text)
    const keyHash = await bcrypt.hash(key, 10);

    // Store in database
    const apiKey = await apiKeyRepository.create({
      userId,
      name,
      keyHash,
      scopes,
      lastUsed: null,
      createdAt: new Date(),
    });

    // Return key ONCE (cannot be retrieved later)
    return {
      id: apiKey.id,
      key, // Only time this is visible
      name,
      scopes,
      createdAt: apiKey.createdAt,
    };
  }

  async validate(key: string): Promise<ApiKey | null> {
    // Verify format
    if (!key.startsWith('sk_')) {
      return null;
    }

    // Find all keys and compare hashes
    // (In production, add key prefix index for performance)
    const keys = await apiKeyRepository.findAll();

    for (const stored of keys) {
      const isValid = await bcrypt.compare(key, stored.keyHash);
      if (isValid) {
        // Update last used timestamp (async, don't wait)
        apiKeyRepository.updateLastUsed(stored.id).catch(console.error);

        return stored;
      }
    }

    return null;
  }

  async revoke(userId: string, keyId: string) {
    await apiKeyRepository.delete({ userId, id: keyId });
  }

  async list(userId: string) {
    return await apiKeyRepository.findByUserId(userId);
  }
}
```

### API Key Middleware

```typescript
export async function authenticateApiKey(
  req: AuthRequest,
  res: Response,
  next: NextFunction
) {
  const apiKey = req.headers['x-api-key'] as string;

  if (!apiKey) {
    return res.status(401).json({
      error: 'unauthorized',
      message: 'API key required',
    });
  }

  const key = await apiKeyService.validate(apiKey);

  if (!key) {
    return res.status(401).json({
      error: 'invalid_api_key',
      message: 'Invalid API key',
    });
  }

  // Load user
  const user = await userRepository.findById(key.userId);
  if (!user) {
    return res.status(401).json({
      error: 'invalid_api_key',
      message: 'Associated user not found',
    });
  }

  // Attach to request
  req.user = user;
  req.apiKey = key;

  next();
}

// Scope validation
export function requireScopes(scopes: string[]) {
  return (req: AuthRequest, res: Response, next: NextFunction) => {
    if (!req.apiKey) {
      return res.status(403).json({
        error: 'forbidden',
        message: 'API key required for this operation',
      });
    }

    const hasAllScopes = scopes.every(scope =>
      req.apiKey.scopes.includes(scope)
    );

    if (!hasAllScopes) {
      return res.status(403).json({
        error: 'insufficient_scope',
        message: `Required scopes: ${scopes.join(', ')}`,
      });
    }

    next();
  };
}
```

---

## Authorization

### Role-Based Access Control (RBAC)

```typescript
type Role = 'admin' | 'user' | 'guest';

const rolePermissions: Record<Role, string[]> = {
  admin: [
    'read:users',
    'write:users',
    'delete:users',
    'read:posts',
    'write:posts',
    'delete:posts',
    'admin:*',
  ],
  user: ['read:users', 'read:posts', 'write:posts', 'write:own'],
  guest: ['read:posts'],
};

// Authorization middleware
export function authorize(requiredPermissions: string[]) {
  return (req: AuthRequest, res: Response, next: NextFunction) => {
    if (!req.user) {
      return res.status(401).json({
        error: 'unauthorized',
        message: 'Authentication required',
      });
    }

    const userPermissions = rolePermissions[req.user.role] || [];

    const hasPermission = requiredPermissions.every(permission =>
      userPermissions.includes(permission) ||
      userPermissions.includes('admin:*')
    );

    if (!hasPermission) {
      return res.status(403).json({
        error: 'forbidden',
        message: 'Insufficient permissions',
        required: requiredPermissions,
      });
    }

    next();
  };
}

// Usage
router.get('/users', authenticate, authorize(['read:users']), getUsersHandler);
router.post('/users', authenticate, authorize(['write:users']), createUserHandler);
```

### Resource Ownership

```typescript
// Check if user owns resource
export function requireOwnership(
  resourceGetter: (req: AuthRequest) => Promise<{ userId: string }>
) {
  return async (req: AuthRequest, res: Response, next: NextFunction) => {
    if (!req.user) {
      return res.status(401).json({
        error: 'unauthorized',
        message: 'Authentication required',
      });
    }

    // Admin bypass
    if (req.user.role === 'admin') {
      return next();
    }

    const resource = await resourceGetter(req);

    if (resource.userId !== req.user.id) {
      return res.status(403).json({
        error: 'forbidden',
        message: 'You can only access your own resources',
      });
    }

    next();
  };
}

// Usage
router.patch(
  '/posts/:id',
  authenticate,
  requireOwnership(async (req) => {
    return await postRepository.findById(req.params.id);
  }),
  updatePostHandler
);
```

---

## Security Best Practices

### Environment Configuration

```bash
# .env (NEVER commit to git)
JWT_SECRET=<64+ char random string>
JWT_REFRESH_SECRET=<64+ char random string>
GOOGLE_CLIENT_ID=<google client id>
GOOGLE_CLIENT_SECRET=<google client secret>
REDIS_URL=redis://localhost:6379
DATABASE_URL=postgresql://user:pass@localhost:5432/db

# Use different secrets for each environment
# Generate with: openssl rand -hex 64
```

### Rate Limiting Auth Endpoints

```typescript
// Strict rate limiting for auth endpoints
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5, // 5 attempts
  message: 'Too many login attempts, please try again later',
  standardHeaders: true,
  legacyHeaders: false,
});

router.post('/auth/login', authLimiter, loginHandler);
router.post('/auth/register', authLimiter, registerHandler);
router.post('/auth/reset-password', authLimiter, resetPasswordHandler);
```

### Account Lockout

```typescript
class LoginAttemptTracker {
  private redis: Redis;
  private readonly MAX_ATTEMPTS = 5;
  private readonly LOCKOUT_DURATION = 15 * 60; // 15 minutes

  async recordAttempt(email: string): Promise<void> {
    const key = `login_attempts:${email}`;
    await this.redis.incr(key);
    await this.redis.expire(key, this.LOCKOUT_DURATION);
  }

  async getAttempts(email: string): Promise<number> {
    const attempts = await this.redis.get(`login_attempts:${email}`);
    return parseInt(attempts || '0');
  }

  async isLocked(email: string): Promise<boolean> {
    const attempts = await this.getAttempts(email);
    return attempts >= this.MAX_ATTEMPTS;
  }

  async reset(email: string): Promise<void> {
    await this.redis.del(`login_attempts:${email}`);
  }
}
```

---

## Best Practices Checklist

- [ ] Passwords hashed with bcrypt (12+ rounds) or argon2
- [ ] JWT tokens signed with strong secret (64+ chars)
- [ ] Access tokens short-lived (15 minutes)
- [ ] Refresh tokens rotated on use
- [ ] Refresh tokens stored hashed
- [ ] Token blacklist implemented
- [ ] Rate limiting on auth endpoints
- [ ] Account lockout after failed attempts
- [ ] Password strength validation
- [ ] Common password checking
- [ ] HTTPS only (no HTTP)
- [ ] Secure cookie flags (httpOnly, secure, sameSite)
- [ ] CORS configured correctly
- [ ] Security headers (helmet.js)
- [ ] API keys stored hashed
- [ ] OAuth tokens encrypted at rest
- [ ] Audit logging for auth events
- [ ] Multi-factor authentication (optional)

---

**Version**: 1.0
**Last Updated**: January 2025
**Use Cases**: JWT authentication, OAuth 2.0, API keys, RBAC, security best practices
