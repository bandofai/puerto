# CLAUDE.md Syntax & Structure Specification

**Version**: 1.0.0
**Last Updated**: 2025-11-01
**Source**: Official Puerto documentation (configuring-claude-md.md)

---

## Purpose of This Skill

This skill provides comprehensive knowledge of CLAUDE.md syntax, structure, and best practices. It serves as the authoritative reference for all claude-md-master agents when creating, validating, or optimizing CLAUDE.md files.

**Key Learning Objectives**:
- Complete CLAUDE.md file structure and sections
- WHEN/AUTOMATICALLY routing rule patterns (THE CRITICAL FEATURE)
- Project-specific pattern documentation
- Common mistakes and their fixes
- Complete examples by project type

---

## What is CLAUDE.md?

CLAUDE.md is a configuration file that lives in a project's root directory and serves as an instruction manual for Claude Code. It tells Claude:

1. **Which Puerto plugins are installed** and available
2. **When to automatically use specific agents** (via routing rules)
3. **Project-specific patterns** to follow (file structure, code conventions)
4. **Domain knowledge** that helps agents make appropriate decisions

**The Result**: Claude proactively uses the right expert agents without manual specification every time.

### Why CLAUDE.md Matters

Without CLAUDE.md, Claude won't automatically know WHEN to use installed Puerto plugin agents. The file creates a "cascade effect":

```
User Request
    ↓
1. Claude reads CLAUDE.md → identifies task → selects agent
    ↓
2. Agent is invoked and reads CLAUDE.md → learns patterns → understands context
    ↓
3. Agent generates code matching project conventions
```

---

## Complete CLAUDE.md Structure

### Standard Sections (in order)

```markdown
# [Project Name]

## Project Type
[Brief description of what this project is]

## Tech Stack
- Frontend: [Technologies]
- Backend: [Technologies]
- Database: [Technologies]
- Testing: [Technologies]
- Deployment: [Platforms]

## Installed Puerto Plugins
- plugin-name (agents: agent1, agent2, agent3)
- plugin-name (agents: agent1, agent2)

## Automatic Task Routing

### [Category] Tasks
WHEN [trigger condition] → AUTOMATICALLY invoke: plugin-name:agent-name
WHEN [trigger condition] → AUTOMATICALLY invoke: plugin-name:agent-name

### [Category] Tasks
WHEN [trigger condition] → AUTOMATICALLY invoke: plugin-name:agent-name

## Project Patterns

### File Organization
[Directory structure with examples]

### [Pattern Category]
[Code examples and conventions]

## Domain Knowledge
[Business rules, constraints, integration points]
```

### Section Details

#### 1. Project Type & Tech Stack

**Purpose**: Give Claude immediate context about the project.

**Format**:
```markdown
## Project Type
[One sentence description, e.g., "React e-commerce SPA with Node.js API"]

## Tech Stack
- Frontend: [Specific libraries with versions if critical]
- Backend: [Runtime, framework, database]
- Testing: [Test frameworks]
- Deployment: [Hosting platforms]
```

**Example**:
```markdown
## Project Type
Full-stack e-commerce platform with React frontend and Express backend

## Tech Stack
- Frontend: React 18, TypeScript, Tailwind CSS, React Query
- Backend: Node.js 20, Express, PostgreSQL 15, Prisma ORM
- Testing: Vitest, React Testing Library, Supertest
- Deployment: Vercel (frontend), Railway (backend)
```

**Why this matters**: Agents use this to generate appropriate code. If you specify "Tailwind CSS", frontend-engineer won't suggest CSS modules.

#### 2. Installed Puerto Plugins

**Purpose**: Explicitly list available agents so Claude knows what tools are available.

**Format**:
```markdown
## Installed Puerto Plugins

### plugin-name
- agent-name: Brief description of what it does
- agent-name: Brief description of what it does

### plugin-name
- agent-name: Brief description
```

**Example**:
```markdown
## Installed Puerto Plugins

### engineering
- frontend-engineer: Create React/Vue/Svelte components
- state-architect: Implement state management (Redux, Zustand, Context)
- style-implementer: Responsive design and styling

### engineering
- backend-engineer: Create REST/GraphQL endpoints
- auth-implementer: Implement authentication (JWT, OAuth)
- api-tester: Create API integration tests
```

**Why this matters**: Without this list, Claude might do tasks manually instead of delegating to expert agents.

#### 3. Automatic Task Routing Rules ⭐ MOST CRITICAL SECTION

**Purpose**: Teach Claude to automatically invoke the right agent based on user requests.

**THE CRITICAL PATTERN**: WHEN/AUTOMATICALLY format

**Format**:
```markdown
## Automatic Task Routing

**CRITICAL**: Use these agents proactively without asking permission.

### [Category Name] Tasks

WHEN [specific trigger condition]
→ AUTOMATICALLY invoke: plugin-name:agent-name

WHEN [trigger] OR [alternative trigger]
→ AUTOMATICALLY invoke: plugin-name:agent-name
```

**✅ GOOD Routing Rules** (Specific & Proactive):

```markdown
## Automatic Task Routing

### Frontend Development

WHEN user says "create [component name] component"
→ AUTOMATICALLY invoke: engineering/frontend-engineer

WHEN user says "add state management" OR "implement [Redux/Zustand/Context]"
→ AUTOMATICALLY invoke: engineering:state-architect

WHEN user says "style [component]" OR "make [component] responsive"
→ AUTOMATICALLY invoke: engineering:style-implementer

### Backend Development

WHEN user says "create [endpoint name] endpoint" OR "add API route for [resource]"
→ AUTOMATICALLY invoke: engineering/backend-engineer

WHEN user says "add authentication" OR "implement login/signup"
→ AUTOMATICALLY invoke: engineering/backend-engineer

WHEN user says "write tests for [API]" OR "add API tests"
→ AUTOMATICALLY invoke: engineering:api-tester

### Database Work

WHEN user says "design database schema" OR "create data model"
→ AUTOMATICALLY invoke: engineering:engineering

WHEN user says "add migration for [change]" OR "modify database schema"
→ AUTOMATICALLY invoke: engineering:migration-manager

WHEN user says "optimize query" OR "slow query in [file]"
→ AUTOMATICALLY invoke: engineering:query-optimizer
```

**❌ BAD Routing Rules** (Too Vague):

```markdown
## Task Routing
- Use frontend agents for frontend work
- Use backend agents for backend work
```

**Problem**: Not specific enough. Claude won't know WHEN to use which agent.

**Key Principles for Routing Rules**:
1. Use WHEN/AUTOMATICALLY keywords explicitly
2. Include specific trigger phrases users might say
3. Use OR for alternative phrasings
4. Include [placeholders] for variable parts
5. Group by logical categories
6. Be concrete, not abstract

#### 4. Project Patterns

**Purpose**: Ensure agents generate code that matches existing conventions.

**Format**:
```markdown
## Project Patterns

### File Organization
```
[directory tree with comments]
```

### [Pattern Category Name]
```[language]
// ✅ Follow this pattern (from [ExampleFile])
[actual code example from project]
```

**When creating new [things]**:
- [Convention 1]
- [Convention 2]
- [Reference file example]
```

**Example - Component Patterns**:
```markdown
### Component Structure
- Components live in: `src/components/`
- Use Tailwind for styling (no CSS modules)
- Follow existing pattern in `src/components/ProductCard.tsx`

```typescript
// ✅ Follow this pattern (from ProductCard.tsx)
import React from 'react';

interface ProductCardProps {
  // Props with JSDoc comments
  title: string;
  price: number;
}

export function ProductCard({ title, price }: ProductCardProps) {
  // Component logic
  return (
    <div className="rounded-lg shadow-md p-4">
      <h3>{title}</h3>
      <p>${price}</p>
    </div>
  );
}
```

**When creating new components**:
- Use named exports (not default)
- TypeScript interfaces for props
- Tailwind for styling
- Follow existing component structure
```

**Example - API Patterns**:
```markdown
### API Conventions
- REST endpoints in: `src/api/routes/`
- Use Zod for request validation
- Follow pattern in `src/api/routes/products.ts`

```typescript
// ✅ Follow this pattern (from src/api/routes/products.ts)
import { Router } from 'express';
import { z } from 'zod';
import { validateRequest } from '../middleware/validation';

const router = Router();

// Zod schema for validation
const createProductSchema = z.object({
  name: z.string(),
  price: z.number(),
});

// Route handler with validation
router.post('/products', validateRequest(createProductSchema), async (req, res) => {
  // Handler logic
});

export default router;
```

**When creating new endpoints**:
- Use Zod for request validation
- Async/await for handlers
- Consistent error handling middleware
- Follow REST conventions
```

**Why this matters**: Agents read these patterns and generate code that looks like it was written by the project team.

#### 5. Domain Knowledge

**Purpose**: Business context that helps agents make domain-appropriate decisions.

**Format**:
```markdown
## Domain Knowledge

### [Domain Area] Business Rules
- **[Rule Name]**: [Description with specifics]
- **[Rule Name]**: [Description]

### Critical Constraints
- [Constraint with reasoning]
- [Constraint with reasoning]

### Integration Points
- [External service description and reference file]
- [External service description and reference file]
```

**Example**:
```markdown
## Domain Knowledge

### E-commerce Business Rules
- **Products have variants**: Size, color, material (stored as separate SKUs)
- **Pricing calculation**: Base price + variant price + tax (by region)
- **Inventory**: Tracked per variant, not per product
- **Cart lifetime**: 24 hours for guest users, 30 days for authenticated
- **Payment processing**: Stripe for cards, PayPal for alternative payment

### Critical Constraints
- All prices stored in cents (integer) to avoid floating-point errors
- Product images must be optimized (<200KB) before storage
- PII (personally identifiable information) must not be logged
- GDPR compliance required: data deletion within 30 days of request

### Integration Points
- Stripe webhooks handle payment confirmations (see `src/webhooks/stripe.ts`)
- SendGrid for transactional emails (see `src/services/email.ts`)
- Cloudinary for image storage and transformation
```

**Why this matters**: Without this context, an agent might create a pricing system that uses floats (causing rounding errors) or log user emails (violating privacy).

---

## Common Mistakes & How to Fix Them

### ❌ Mistake 1: Vague Routing Rules

**Bad**:
```markdown
## Task Routing
Use frontend agents for frontend work
```

**Problem**: Not specific enough. Claude won't know when to invoke agents.

**✅ Fix**:
```markdown
## Automatic Task Routing

WHEN user says "create [component name] component" OR "add [component name]"
→ AUTOMATICALLY invoke: engineering/frontend-engineer

WHEN user says "style [component]" OR "make responsive"
→ AUTOMATICALLY invoke: engineering:style-implementer
```

### ❌ Mistake 2: Not Listing Installed Plugins

**Bad**:
```markdown
# My Project

## Project Patterns
[Goes straight to patterns without listing plugins]
```

**Problem**: Claude doesn't know which agents are available.

**✅ Fix**:
```markdown
## Installed Puerto Plugins
- engineering
- engineering
- engineering

## Automatic Task Routing
[Then routing rules that reference these plugins]
```

### ❌ Mistake 3: Missing Project Patterns

**Bad**:
```markdown
## Project Patterns
We use React and Tailwind
```

**Problem**: Too vague. Agents don't know file structure, naming conventions, etc.

**✅ Fix**:
```markdown
## Project Patterns

### Component Structure
- Location: `src/components/[Name].tsx`
- Styling: Tailwind classes (see ProductCard.tsx for example)
- Props: TypeScript interfaces

```typescript
// Follow this pattern from ProductCard.tsx
export function ProductCard({ title, price }: Props) {
  return <div className="rounded-lg shadow-md">...</div>;
}
```
```

### ❌ Mistake 4: Information Overload

**Bad**:
```markdown
[50 pages of detailed documentation about every aspect of the project]
```

**Problem**: Too much information. Claude gets overwhelmed and misses key points.

**✅ Fix**:
```markdown
## Key Points
- Component location: `src/components/`
- Styling: Tailwind only
- API routes: `src/api/routes/`
- Example component: See ProductCard.tsx
- Example API: See src/api/routes/products.ts

[Focus on most important patterns, reference files for details]
```

### ❌ Mistake 5: Outdated Information

**Bad**:
```markdown
## Tech Stack
- React 16
- Redux for state

[Project has since upgraded to React 18 and removed Redux]
```

**Problem**: Agents generate code for the wrong stack.

**✅ Fix**:
- Update when upgrading libraries
- Update when adding/removing plugins
- Update when changing patterns
- Review quarterly for accuracy

---

## Complete Examples by Project Type

### Example 1: React SPA with REST API

**Scenario**: E-commerce frontend in React, backend in Node.js/Express

**Plugins**: engineering, engineering, engineering

```markdown
# ShopHub - E-commerce Platform

## Project Type
React single-page application (SPA) with Node.js REST API backend

## Tech Stack
- Frontend: React 18, TypeScript, Tailwind CSS, React Query, React Router
- Backend: Node.js 20, Express, PostgreSQL 15, Prisma ORM
- Testing: Vitest, React Testing Library, Supertest
- Deployment: Vercel (frontend), Railway (backend)

## Installed Puerto Plugins
- engineering (frontend-engineer, state-architect, style-implementer)
- engineering (backend-engineer, auth-implementer, api-tester)
- engineering (api-designer, engineering)

## Automatic Task Routing

### Frontend Tasks
WHEN creating components → AUTOMATICALLY invoke engineering/frontend-engineer
WHEN implementing state → AUTOMATICALLY invoke engineering:state-architect
WHEN styling → AUTOMATICALLY invoke engineering:style-implementer

### Backend Tasks
WHEN creating endpoints → AUTOMATICALLY invoke engineering/backend-engineer
WHEN adding authentication → AUTOMATICALLY invoke engineering/backend-engineer
WHEN designing APIs → AUTOMATICALLY invoke engineering:api-designer

### Database Tasks
WHEN designing schemas → AUTOMATICALLY invoke engineering:engineering

## Project Patterns

### Component Structure
- Location: `src/components/[ComponentName].tsx`
- Styling: Tailwind classes only (no CSS modules)
- Props: TypeScript interfaces with JSDoc
- Exports: Named exports (not default)
- Example: See `src/components/ProductCard.tsx`

### API Structure
- Routes: `src/api/routes/[resource].ts`
- Validation: Zod schemas
- Auth: JWT middleware in `src/api/middleware/auth.ts`
- Example: See `src/api/routes/products.ts`

### State Management
- Global state: React Query for server state
- Local state: useState/useReducer
- Auth state: Custom useAuth hook
- No Redux (explicitly avoided)

## Domain Knowledge
- Products have variants (size, color) as separate SKUs
- Prices in cents (integer) to avoid floating-point errors
- Cart expires after 24 hours (guest) or 30 days (authenticated)
- Payment via Stripe webhooks
- GDPR compliance: no PII in logs
```

### Example 2: Node.js Microservices

**Scenario**: Backend-only microservices architecture

**Plugins**: engineering, engineering, engineering/devops-engineer, engineering

```markdown
# PaymentProcessor - Microservices Platform

## Project Type
Node.js microservices architecture with event-driven communication

## Tech Stack
- Runtime: Node.js 20, TypeScript
- Framework: Express, NestJS (auth service)
- Message Queue: RabbitMQ
- Databases: PostgreSQL (transactions), Redis (cache), MongoDB (logs)
- Testing: Jest, Supertest
- Deployment: Kubernetes (AWS EKS)

## Installed Puerto Plugins
- engineering (backend-engineer, auth-implementer, api-tester)
- engineering (api-designer, engineering, system-architect)
- engineering/devops-engineer (cicd-builder, deployment-orchestrator, infrastructure-manager)
- engineering (schema-designer, migration-manager, query-optimizer)

## Automatic Task Routing

### API Development
WHEN creating endpoints → AUTOMATICALLY invoke engineering/backend-engineer
WHEN implementing auth → AUTOMATICALLY invoke engineering/backend-engineer
WHEN writing API tests → AUTOMATICALLY invoke engineering:api-tester

### Architecture
WHEN designing APIs → AUTOMATICALLY invoke engineering:api-designer
WHEN designing schemas → AUTOMATICALLY invoke engineering:engineering
WHEN designing system architecture → AUTOMATICALLY invoke engineering:system-architect

### Database
WHEN creating migrations → AUTOMATICALLY invoke engineering:migration-manager
WHEN optimizing queries → AUTOMATICALLY invoke engineering:query-optimizer

### DevOps
WHEN setting up CI/CD → AUTOMATICALLY invoke engineering/devops-engineer:cicd-builder
WHEN deploying → AUTOMATICALLY invoke engineering/devops-engineer:deployment-orchestrator
WHEN creating infrastructure → AUTOMATICALLY invoke engineering/devops-engineer:infrastructure-manager

## Project Patterns

### Service Structure
```
services/
├── auth-service/          # NestJS service
├── payment-service/       # Express service
├── notification-service/  # Express service
└── shared/               # Shared libraries
```

### API Conventions
- All services expose: `/health`, `/metrics`, `/ready`
- OpenAPI spec required for all services
- REST for sync, RabbitMQ for async
- Correlation IDs for request tracing

### Event Patterns
```typescript
// Publisher pattern
await messageQueue.publish('payment.processed', {
  correlationId: req.id,
  payload: { orderId, amount, status }
});

// Consumer pattern
messageQueue.subscribe('payment.processed', async (message) => {
  // Handle event
});
```

### Database Patterns
- PostgreSQL for transactional data (ACID required)
- MongoDB for append-only logs
- Redis for caching and session storage
- Migrations: Knex.js for PostgreSQL
- Connection pooling: 20 max connections per service

## Domain Knowledge
- Payment processing: PCI DSS compliance required
- Idempotency: All payment endpoints must be idempotent (use idempotency keys)
- Event ordering: Use RabbitMQ with consistent hash exchange
- Retry logic: Exponential backoff with max 3 retries
- Circuit breaker: Fail fast after 5 consecutive errors
```

### Example 3: Full-Stack Next.js App

**Scenario**: Next.js with API routes and PostgreSQL

**Plugins**: engineering, engineering, engineering

```markdown
# TaskMaster - Project Management SaaS

## Project Type
Full-stack Next.js 14 application with App Router and server actions

## Tech Stack
- Framework: Next.js 14 (App Router), TypeScript, React 18
- Styling: Tailwind CSS, Shadcn UI components
- Database: PostgreSQL 15 with Drizzle ORM
- Auth: NextAuth.js v5
- Deployment: Vercel

## Installed Puerto Plugins
- engineering (frontend-engineer, state-architect, style-implementer)
- engineering (backend-engineer, auth-implementer)
- engineering (schema-designer, migration-manager, query-optimizer)

## Automatic Task Routing

### Frontend
WHEN creating components → AUTOMATICALLY invoke engineering/frontend-engineer
WHEN implementing client state → AUTOMATICALLY invoke engineering:state-architect

### Backend
WHEN creating API routes → AUTOMATICALLY invoke engineering/backend-engineer
WHEN creating server actions → AUTOMATICALLY invoke engineering/backend-engineer
WHEN implementing auth → AUTOMATICALLY invoke engineering/backend-engineer

### Database
WHEN designing schemas → AUTOMATICALLY invoke engineering:schema-designer
WHEN creating migrations → AUTOMATICALLY invoke engineering:migration-manager
WHEN optimizing queries → AUTOMATICALLY invoke engineering:query-optimizer

## Project Patterns

### File Structure (App Router)
```
app/
├── (auth)/            # Auth group
│   ├── login/
│   └── signup/
├── (dashboard)/       # Protected group
│   ├── projects/
│   └── tasks/
├── api/              # API routes
└── actions/          # Server actions
components/
├── ui/               # Shadcn components
└── [feature]/        # Feature components
```

### Component Patterns
- Use Shadcn UI components as base
- Server Components by default
- Client Components only when needed (mark with 'use client')
- Co-locate components with routes when route-specific

### Server Actions Pattern
```typescript
// app/actions/tasks.ts
'use server';

import { revalidatePath } from 'next/cache';
import { auth } from '@/lib/auth';

export async function createTask(formData: FormData) {
  const session = await auth();
  if (!session) throw new Error('Unauthorized');

  // Business logic

  revalidatePath('/dashboard/tasks');
}
```

### Database Patterns
- Drizzle ORM for type-safe queries
- Schemas in: `db/schema.ts`
- Migrations in: `db/migrations/`
- Use transactions for multi-table operations
- Index frequently queried columns

## Domain Knowledge
- Multi-tenancy: All data scoped to workspaceId
- Permissions: Role-based (owner, admin, member)
- Real-time: Use Supabase Realtime for live updates
- Webhooks: Stripe for billing, Slack for notifications
- Data retention: Soft delete with 30-day retention before hard delete
```

---

## Advanced Patterns

### Context-Specific Routing

Route differently based on file location:

```markdown
## Context-Specific Routing

WHEN working in `src/admin/` directory
→ Use admin-specific patterns (verbose logging, strict validation)

WHEN working in `src/public-api/` directory
→ Use public API patterns (rate limiting, thorough docs)
```

### Conditional Plugin Usage

```markdown
## Conditional Agent Usage

WHEN implementing payment features
→ MUST invoke: engineering/backend-engineer (for PCI compliance)
→ MUST add: Audit logging

WHEN implementing user data features
→ MUST consider: GDPR compliance (no PII in logs)
```

### Reference External Docs

```markdown
## Reference Documentation

For API design patterns: See `docs/api-guidelines.md`
For component library: See Storybook at `http://localhost:6006`
For database schema: See ER diagram at `docs/schema.png`
```

### Plugin Combinations for Complex Tasks

```markdown
## Complex Task Routing

WHEN user says "create new feature with [frontend + backend]"
→ First invoke: engineering:system-architect (design architecture)
→ Then invoke: engineering/frontend-engineer (build UI)
→ Then invoke: engineering/backend-engineer (build API)
→ Then invoke: engineering:schema-designer (design schema)

This ensures proper architecture before implementation.
```

---

## Validation Checklist

Use this checklist when validating CLAUDE.md files:

### Structure Validation
- [ ] Has Project Type section
- [ ] Has Tech Stack section
- [ ] Has Installed Puerto Plugins section
- [ ] Has Automatic Task Routing section
- [ ] Has Project Patterns section (optional but recommended)
- [ ] Has Domain Knowledge section (optional but recommended)

### Routing Rules Validation
- [ ] Uses WHEN/AUTOMATICALLY keywords
- [ ] Routing rules are specific (not vague)
- [ ] Includes trigger phrases users might say
- [ ] Uses OR for alternative phrasings
- [ ] Groups rules by logical categories
- [ ] References installed plugins correctly

### Pattern Validation
- [ ] Includes concrete code examples
- [ ] References actual project files
- [ ] Specifies file locations
- [ ] Documents naming conventions
- [ ] Shows technology usage (not just lists)

### Domain Knowledge Validation
- [ ] Includes business rules if applicable
- [ ] Documents critical constraints
- [ ] Lists integration points
- [ ] Explains "why" not just "what"

### Quality Validation
- [ ] Concise (not information overload)
- [ ] Up to date (matches current tech stack)
- [ ] Actionable (agents can follow patterns)
- [ ] Consistent (formatting throughout)

---

## Maintenance Best Practices

### Keep It Updated

Track changes:
```markdown
## Change Log
- 2025-11-01: Added engineering plugin
- 2025-10-15: Migrated from Redux to React Query
- 2025-09-20: Upgraded to React 18
```

### Version Control

Commit to repository:
```bash
git add CLAUDE.md
git commit -m "docs: add CLAUDE.md with routing rules for Puerto plugins"
```

### Iterative Improvement

1. **Start simple**: Basic routing rules and patterns
2. **Observe**: See how Claude uses it
3. **Refine**: Add specificity where Claude gets confused
4. **Expand**: Add domain knowledge as needed

---

## Summary: Key Principles

1. **CLAUDE.md guides agent selection** - Without it, Claude won't automatically use installed plugins

2. **Be specific in routing rules** - Use WHEN/AUTOMATICALLY format with concrete task descriptions

3. **Document patterns with examples** - Show actual code from the project that agents should follow

4. **Include domain knowledge** - Business context helps agents make appropriate decisions

5. **Keep it maintained** - Update when changing tech stack or patterns

6. **Test and iterate** - Start simple, observe behavior, refine based on results

---

**End of CLAUDE.md Syntax Specification**

This skill should be loaded at the start of every claude-md-master agent invocation to ensure complete and accurate knowledge of CLAUDE.md structure, syntax, and best practices.
