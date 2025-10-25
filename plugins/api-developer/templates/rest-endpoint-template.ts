/**
 * REST Endpoint Template
 *
 * Production-ready REST endpoint with validation, error handling, and security.
 * Replace placeholders with your resource details.
 */

import { Router, Request, Response, NextFunction } from 'express';
import { z } from 'zod';
import { authenticate, authorize } from '../middleware/auth';
import { validateRequest } from '../middleware/validation';
import { rateLimit } from '../middleware/rateLimit';

const router = Router();

// ============================================================================
// Validation Schemas
// ============================================================================

const createResourceSchema = z.object({
  name: z.string().min(1).max(100),
  description: z.string().max(500).optional(),
  status: z.enum(['active', 'inactive']).default('active'),
  // Add your fields here
});

const updateResourceSchema = z.object({
  name: z.string().min(1).max(100).optional(),
  description: z.string().max(500).optional(),
  status: z.enum(['active', 'inactive']).optional(),
  // Add your fields here
});

const paginationSchema = z.object({
  page: z.coerce.number().int().positive().default(1),
  limit: z.coerce.number().int().positive().max(100).default(20),
  sort: z.string().optional(),
});

const resourceIdSchema = z.object({
  id: z.string().uuid(),
});

// ============================================================================
// GET /resources - List resources
// ============================================================================

router.get(
  '/resources',
  authenticate,
  authorize(['read:resources']),
  rateLimit({ max: 1000, window: '1h' }),
  validateRequest({ query: paginationSchema }),
  async (req: Request, res: Response, next: NextFunction) => {
    try {
      const { page, limit, sort } = req.query;

      // Fetch resources from database
      const { resources, total } = await resourceService.findAll({
        page: Number(page),
        limit: Number(limit),
        sort: sort as string,
      });

      const totalPages = Math.ceil(total / Number(limit));

      res.status(200).json({
        data: resources,
        pagination: {
          page: Number(page),
          limit: Number(limit),
          total,
          totalPages,
          hasNext: Number(page) < totalPages,
          hasPrev: Number(page) > 1,
        },
      });
    } catch (error) {
      next(error);
    }
  }
);

// ============================================================================
// GET /resources/:id - Get single resource
// ============================================================================

router.get(
  '/resources/:id',
  authenticate,
  authorize(['read:resources']),
  rateLimit({ max: 1000, window: '1h' }),
  validateRequest({ params: resourceIdSchema }),
  async (req: Request, res: Response, next: NextFunction) => {
    try {
      const { id } = req.params;

      const resource = await resourceService.findById(id);

      if (!resource) {
        return res.status(404).json({
          error: 'not_found',
          message: 'Resource not found',
        });
      }

      res.status(200).json(resource);
    } catch (error) {
      next(error);
    }
  }
);

// ============================================================================
// POST /resources - Create resource
// ============================================================================

router.post(
  '/resources',
  authenticate,
  authorize(['write:resources']),
  rateLimit({ max: 100, window: '1h' }),
  validateRequest({ body: createResourceSchema }),
  async (req: Request, res: Response, next: NextFunction) => {
    try {
      const resourceData = req.body;

      // Check for duplicates (if applicable)
      const existing = await resourceService.findByName(resourceData.name);
      if (existing) {
        return res.status(409).json({
          error: 'conflict',
          message: 'Resource with this name already exists',
        });
      }

      // Create resource
      const resource = await resourceService.create(resourceData);

      res.status(201)
        .location(`/resources/${resource.id}`)
        .json(resource);
    } catch (error) {
      next(error);
    }
  }
);

// ============================================================================
// PATCH /resources/:id - Update resource
// ============================================================================

router.patch(
  '/resources/:id',
  authenticate,
  authorize(['write:resources']),
  rateLimit({ max: 200, window: '1h' }),
  validateRequest({
    params: resourceIdSchema,
    body: updateResourceSchema,
  }),
  async (req: Request, res: Response, next: NextFunction) => {
    try {
      const { id } = req.params;
      const updates = req.body;

      // Check if resource exists
      const existing = await resourceService.findById(id);
      if (!existing) {
        return res.status(404).json({
          error: 'not_found',
          message: 'Resource not found',
        });
      }

      // Check ownership (if applicable)
      // if (existing.userId !== req.user.id && req.user.role !== 'admin') {
      //   return res.status(403).json({
      //     error: 'forbidden',
      //     message: 'You can only update your own resources',
      //   });
      // }

      // Update resource
      const resource = await resourceService.update(id, updates);

      res.status(200).json(resource);
    } catch (error) {
      next(error);
    }
  }
);

// ============================================================================
// DELETE /resources/:id - Delete resource
// ============================================================================

router.delete(
  '/resources/:id',
  authenticate,
  authorize(['delete:resources']),
  rateLimit({ max: 100, window: '1h' }),
  validateRequest({ params: resourceIdSchema }),
  async (req: Request, res: Response, next: NextFunction) => {
    try {
      const { id } = req.params;

      // Check if resource exists
      const existing = await resourceService.findById(id);
      if (!existing) {
        return res.status(404).json({
          error: 'not_found',
          message: 'Resource not found',
        });
      }

      // Check ownership (if applicable)
      // if (existing.userId !== req.user.id && req.user.role !== 'admin') {
      //   return res.status(403).json({
      //     error: 'forbidden',
      //     message: 'You can only delete your own resources',
      //   });
      // }

      // Delete resource
      await resourceService.delete(id);

      res.status(204).send();
    } catch (error) {
      next(error);
    }
  }
);

// ============================================================================
// Additional Custom Endpoints
// ============================================================================

// Example: GET /resources/:id/related
// Add custom endpoints following the same pattern

export default router;

// ============================================================================
// Service Layer (separate file: services/resource.service.ts)
// ============================================================================

/*
interface Resource {
  id: string;
  name: string;
  description?: string;
  status: 'active' | 'inactive';
  createdAt: Date;
  updatedAt: Date;
}

class ResourceService {
  async findAll(options: {
    page: number;
    limit: number;
    sort?: string;
  }): Promise<{ resources: Resource[]; total: number }> {
    const { page, limit, sort } = options;
    const offset = (page - 1) * limit;

    let query = resourceRepository
      .createQueryBuilder('resource')
      .skip(offset)
      .take(limit);

    // Apply sorting
    if (sort) {
      const descending = sort.startsWith('-');
      const field = descending ? sort.substring(1) : sort;
      query = query.orderBy(`resource.${field}`, descending ? 'DESC' : 'ASC');
    } else {
      query = query.orderBy('resource.createdAt', 'DESC');
    }

    const [resources, total] = await query.getManyAndCount();

    return { resources, total };
  }

  async findById(id: string): Promise<Resource | null> {
    return await resourceRepository.findOne({ where: { id } });
  }

  async findByName(name: string): Promise<Resource | null> {
    return await resourceRepository.findOne({ where: { name } });
  }

  async create(data: Omit<Resource, 'id' | 'createdAt' | 'updatedAt'>): Promise<Resource> {
    const resource = resourceRepository.create(data);
    return await resourceRepository.save(resource);
  }

  async update(id: string, updates: Partial<Resource>): Promise<Resource> {
    await resourceRepository.update(id, updates);
    return await this.findById(id);
  }

  async delete(id: string): Promise<void> {
    await resourceRepository.delete(id);
  }
}

export const resourceService = new ResourceService();
*/

// ============================================================================
// Tests (separate file: tests/resource.test.ts)
// ============================================================================

/*
import request from 'supertest';
import { app } from '../app';
import { setupTestDatabase, teardownTestDatabase } from './helpers/database';
import { createTestUser, generateAuthToken } from './helpers/auth';

describe('Resource API', () => {
  let authToken: string;
  let resourceId: string;

  beforeAll(async () => {
    await setupTestDatabase();
  });

  afterAll(async () => {
    await teardownTestDatabase();
  });

  beforeEach(async () => {
    const user = await createTestUser({ role: 'admin' });
    authToken = generateAuthToken(user);
  });

  describe('GET /resources', () => {
    it('should return paginated resources', async () => {
      const response = await request(app)
        .get('/resources')
        .query({ page: 1, limit: 20 })
        .set('Authorization', `Bearer ${authToken}`)
        .expect(200);

      expect(response.body).toMatchObject({
        data: expect.any(Array),
        pagination: expect.objectContaining({
          page: 1,
          limit: 20,
          total: expect.any(Number),
        }),
      });
    });
  });

  describe('POST /resources', () => {
    it('should create new resource', async () => {
      const resourceData = {
        name: 'Test Resource',
        description: 'Test description',
        status: 'active',
      };

      const response = await request(app)
        .post('/resources')
        .set('Authorization', `Bearer ${authToken}`)
        .send(resourceData)
        .expect(201);

      expect(response.body).toMatchObject({
        id: expect.any(String),
        name: resourceData.name,
        status: resourceData.status,
      });

      resourceId = response.body.id;
    });
  });

  // Add more tests...
});
*/
