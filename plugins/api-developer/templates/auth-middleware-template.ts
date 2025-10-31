/**
 * Authentication Middleware Template
 *
 * Production-ready JWT authentication middleware with refresh tokens,
 * role-based authorization, and security best practices.
 */

import { Request, Response, NextFunction } from 'express';
import jwt from 'jsonwebtoken';
import bcrypt from 'bcrypt';
import crypto from 'crypto';

// ============================================================================
// Type Definitions
// ============================================================================

export interface AuthRequest extends Request {
  user?: {
    userId: string;
    email: string;
    role: string;
    permissions?: string[];
  };
}

interface JWTPayload {
  sub: string;
  email: string;
  role: string;
  permissions?: string[];
  iss: string;
  aud: string;
  exp: number;
  iat: number;
  jti: string;
}

// ============================================================================
// Token Service
// ============================================================================

class TokenService {
  private readonly ACCESS_TOKEN_SECRET = process.env.JWT_SECRET!;
  private readonly REFRESH_TOKEN_SECRET = process.env.JWT_REFRESH_SECRET!;
  private readonly ACCESS_TOKEN_EXPIRY = '15m';
  private readonly REFRESH_TOKEN_EXPIRY = '7d';
  private readonly ISSUER = process.env.API_DOMAIN || 'api.example.com';

  /**
   * Generate JWT access token
   */
  generateAccessToken(user: {
    id: string;
    email: string;
    role: string;
    permissions?: string[];
  }): string {
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
        issuer: this.ISSUER,
        audience: this.ISSUER,
        jwtid: crypto.randomUUID(),
      }
    );
  }

  /**
   * Generate refresh token
   */
  generateRefreshToken(userId: string): string {
    return jwt.sign(
      {
        sub: userId,
        type: 'refresh',
      },
      this.REFRESH_TOKEN_SECRET,
      {
        expiresIn: this.REFRESH_TOKEN_EXPIRY,
        issuer: this.ISSUER,
        jwtid: crypto.randomUUID(),
      }
    );
  }

  /**
   * Verify access token
   */
  verifyAccessToken(token: string): JWTPayload {
    return jwt.verify(token, this.ACCESS_TOKEN_SECRET, {
      issuer: this.ISSUER,
      audience: this.ISSUER,
    }) as JWTPayload;
  }

  /**
   * Verify refresh token
   */
  verifyRefreshToken(token: string): { sub: string; jti: string } {
    return jwt.verify(token, this.REFRESH_TOKEN_SECRET, {
      issuer: this.ISSUER,
    }) as { sub: string; jti: string };
  }
}

export const tokenService = new TokenService();

// ============================================================================
// Authentication Middleware
// ============================================================================

/**
 * Authenticate request using JWT Bearer token
 */
export function authenticate(
  req: AuthRequest,
  res: Response,
  next: NextFunction
) {
  try {
    // Extract token from Authorization header
    const authHeader = req.headers.authorization;
    if (!authHeader?.startsWith('Bearer ')) {
      return res.status(401).json({
        error: 'unauthorized',
        message: 'Authentication required',
      });
    }

    const token = authHeader.substring(7);

    // Verify token
    const payload = tokenService.verifyAccessToken(token);

    // Check if token is blacklisted (optional, requires Redis)
    // const isBlacklisted = await tokenBlacklist.isRevoked(payload.jti);
    // if (isBlacklisted) {
    //   return res.status(401).json({
    //     error: 'token_revoked',
    //     message: 'Token has been revoked',
    //   });
    // }

    // Attach user to request
    req.user = {
      userId: payload.sub,
      email: payload.email,
      role: payload.role,
      permissions: payload.permissions,
    };

    next();
  } catch (error) {
    if (error instanceof jwt.TokenExpiredError) {
      return res.status(401).json({
        error: 'token_expired',
        message: 'Access token has expired. Please refresh your token.',
      });
    }

    if (error instanceof jwt.JsonWebTokenError) {
      return res.status(401).json({
        error: 'invalid_token',
        message: 'Invalid access token',
      });
    }

    return res.status(401).json({
      error: 'unauthorized',
      message: 'Authentication failed',
    });
  }
}

/**
 * Optional authentication - don't fail if token is missing or invalid
 */
export function optionalAuthenticate(
  req: AuthRequest,
  res: Response,
  next: NextFunction
) {
  const authHeader = req.headers.authorization;
  if (!authHeader?.startsWith('Bearer ')) {
    return next();
  }

  try {
    const token = authHeader.substring(7);
    const payload = tokenService.verifyAccessToken(token);

    req.user = {
      userId: payload.sub,
      email: payload.email,
      role: payload.role,
      permissions: payload.permissions,
    };
  } catch (error) {
    // Ignore invalid tokens for optional auth
  }

  next();
}

// ============================================================================
// Authorization Middleware
// ============================================================================

/**
 * Role-based authorization
 * @param roles - Array of allowed roles
 */
export function authorize(roles: string[]) {
  return (req: AuthRequest, res: Response, next: NextFunction) => {
    if (!req.user) {
      return res.status(401).json({
        error: 'unauthorized',
        message: 'Authentication required',
      });
    }

    if (!roles.includes(req.user.role)) {
      return res.status(403).json({
        error: 'forbidden',
        message: 'Insufficient permissions',
        required: `One of: ${roles.join(', ')}`,
        actual: req.user.role,
      });
    }

    next();
  };
}

/**
 * Permission-based authorization
 * @param permissions - Array of required permissions
 * @param requireAll - If true, user must have all permissions. If false, any permission is sufficient.
 */
export function requirePermissions(
  permissions: string[],
  requireAll: boolean = true
) {
  return (req: AuthRequest, res: Response, next: NextFunction) => {
    if (!req.user) {
      return res.status(401).json({
        error: 'unauthorized',
        message: 'Authentication required',
      });
    }

    const userPermissions = req.user.permissions || [];

    // Admin bypass
    if (userPermissions.includes('admin:*')) {
      return next();
    }

    const hasPermissions = requireAll
      ? permissions.every(p => userPermissions.includes(p))
      : permissions.some(p => userPermissions.includes(p));

    if (!hasPermissions) {
      return res.status(403).json({
        error: 'insufficient_permissions',
        message: 'You do not have the required permissions',
        required: permissions,
        condition: requireAll ? 'all' : 'any',
      });
    }

    next();
  };
}

/**
 * Resource ownership check
 * @param resourceGetter - Function to get resource and check ownership
 */
export function requireOwnership(
  resourceGetter: (req: AuthRequest) => Promise<{ userId: string } | null>
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

    try {
      const resource = await resourceGetter(req);

      if (!resource) {
        return res.status(404).json({
          error: 'not_found',
          message: 'Resource not found',
        });
      }

      if (resource.userId !== req.user.userId) {
        return res.status(403).json({
          error: 'forbidden',
          message: 'You can only access your own resources',
        });
      }

      next();
    } catch (error) {
      next(error);
    }
  };
}

// ============================================================================
// Authentication Service
// ============================================================================

class AuthService {
  /**
   * Login user and return tokens
   */
  async login(email: string, password: string) {
    // Find user
    const user = await userRepository.findByEmail(email);
    if (!user) {
      throw new UnauthorizedError('Invalid credentials');
    }

    // Verify password
    const isValid = await bcrypt.compare(password, user.passwordHash);
    if (!isValid) {
      throw new UnauthorizedError('Invalid credentials');
    }

    // Generate tokens
    const accessToken = tokenService.generateAccessToken({
      id: user.id,
      email: user.email,
      role: user.role,
      permissions: user.permissions,
    });

    const refreshToken = tokenService.generateRefreshToken(user.id);

    // Store refresh token hash
    const refreshTokenHash = await bcrypt.hash(refreshToken, 10);
    await refreshTokenRepository.create({
      userId: user.id,
      tokenHash: refreshTokenHash,
      expiresAt: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000),
    });

    return {
      accessToken,
      refreshToken,
      expiresIn: 900, // 15 minutes in seconds
      tokenType: 'Bearer',
    };
  }

  /**
   * Refresh access token using refresh token
   */
  async refreshToken(refreshToken: string) {
    try {
      // Verify refresh token
      const payload = tokenService.verifyRefreshToken(refreshToken);

      // Validate refresh token in database
      const stored = await refreshTokenRepository.findByUserId(payload.sub);
      if (!stored) {
        throw new UnauthorizedError('Invalid refresh token');
      }

      const isValid = await bcrypt.compare(refreshToken, stored.tokenHash);
      if (!isValid) {
        throw new UnauthorizedError('Invalid refresh token');
      }

      // Check expiry
      if (stored.expiresAt < new Date()) {
        await refreshTokenRepository.delete(stored.id);
        throw new UnauthorizedError('Refresh token has expired');
      }

      // Get user
      const user = await userRepository.findById(payload.sub);
      if (!user) {
        throw new UnauthorizedError('User not found');
      }

      // Generate new tokens (token rotation)
      const newAccessToken = tokenService.generateAccessToken({
        id: user.id,
        email: user.email,
        role: user.role,
        permissions: user.permissions,
      });

      const newRefreshToken = tokenService.generateRefreshToken(user.id);

      // Update stored refresh token
      const newTokenHash = await bcrypt.hash(newRefreshToken, 10);
      await refreshTokenRepository.update(stored.id, {
        tokenHash: newTokenHash,
        expiresAt: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000),
      });

      return {
        accessToken: newAccessToken,
        refreshToken: newRefreshToken,
        expiresIn: 900,
        tokenType: 'Bearer',
      };
    } catch (error) {
      if (error instanceof jwt.TokenExpiredError) {
        throw new UnauthorizedError('Refresh token has expired');
      }
      throw new UnauthorizedError('Invalid refresh token');
    }
  }

  /**
   * Logout user and revoke tokens
   */
  async logout(userId: string) {
    await refreshTokenRepository.deleteByUserId(userId);

    // Also add to token blacklist if implemented
    // await tokenBlacklist.revokeAllUserTokens(userId);
  }
}

export const authService = new AuthService();

// ============================================================================
// Error Classes
// ============================================================================

class UnauthorizedError extends Error {
  statusCode = 401;
  error = 'unauthorized';

  constructor(message: string = 'Authentication required') {
    super(message);
  }
}

// ============================================================================
// Usage Examples
// ============================================================================

/*
// Basic authentication
router.get('/profile', authenticate, (req: AuthRequest, res) => {
  res.json(req.user);
});

// Role-based authorization
router.get('/admin', authenticate, authorize(['admin']), (req, res) => {
  res.json({ message: 'Admin only' });
});

// Permission-based authorization
router.post(
  '/posts',
  authenticate,
  requirePermissions(['write:posts']),
  createPostHandler
);

// Resource ownership
router.patch(
  '/posts/:id',
  authenticate,
  requireOwnership(async (req) => {
    return await postRepository.findById(req.params.id);
  }),
  updatePostHandler
);

// Optional authentication
router.get('/public', optionalAuthenticate, (req: AuthRequest, res) => {
  if (req.user) {
    res.json({ message: 'Hello ' + req.user.email });
  } else {
    res.json({ message: 'Hello guest' });
  }
});
*/

// ============================================================================
// Repository Interfaces (implement according to your database)
// ============================================================================

/*
interface User {
  id: string;
  email: string;
  passwordHash: string;
  role: string;
  permissions: string[];
}

interface RefreshToken {
  id: string;
  userId: string;
  tokenHash: string;
  expiresAt: Date;
}

const userRepository = {
  findByEmail: async (email: string): Promise<User | null> => {},
  findById: async (id: string): Promise<User | null> => {},
};

const refreshTokenRepository = {
  create: async (data: Omit<RefreshToken, 'id'>): Promise<RefreshToken> => {},
  findByUserId: async (userId: string): Promise<RefreshToken | null> => {},
  update: async (id: string, data: Partial<RefreshToken>): Promise<void> => {},
  delete: async (id: string): Promise<void> => {},
  deleteByUserId: async (userId: string): Promise<void> => {},
};
*/
