# Database Architect Plugin

Comprehensive database design, optimization, and migration specialist for relational databases (PostgreSQL, MySQL, SQLite).

## Overview

The Database Architect plugin provides expert assistance for all aspects of database management:

- **Schema Design**: ER diagrams, normalization, constraints, indexes
- **Query Optimization**: Performance tuning, execution plan analysis, indexing strategies
- **Migration Management**: Zero-downtime migrations, backfill strategies, rollback procedures
- **Backup & Recovery**: Disaster recovery planning, backup automation, restore procedures

## Agents

### 1. schema-designer (Sonnet)

Creates production-ready database schemas with proper normalization and constraints.

**When to use**:
- Designing new database schemas
- Refactoring existing schemas
- Adding tables or relationships
- Planning data models

**What it produces**:
- ER diagrams (Mermaid format)
- SQL DDL with constraints and indexes
- Design documentation
- Normalization recommendations

**Example**:
```
Design a schema for an e-commerce platform with customers, orders, products, and categories.
```

**Skills**: Reads `schema-design/SKILL.md` for expert patterns

**Tools**: Read, Write, Grep, Glob

---

### 2. query-optimizer (Sonnet)

Analyzes slow queries and suggests optimizations for better performance.

**When to use**:
- Queries running slow
- Need to optimize existing queries
- Adding indexes for performance
- Troubleshooting N+1 query problems

**What it produces**:
- Query execution plan analysis
- Index recommendations with SQL
- Rewritten optimized queries
- Before/after performance comparison

**Example**:
```
This query is taking 5 seconds. How can I optimize it?
SELECT * FROM orders o JOIN customers c ON c.id = o.customer_id WHERE o.status = 'pending';
```

**Skills**: Reads `query-optimization/SKILL.md` for expert patterns

**Tools**: Read, Write, Bash, Grep, Glob

---

### 3. migration-manager (Haiku)

Generates zero-downtime database migrations with rollback support.

**When to use**:
- Adding/removing columns
- Creating indexes
- Changing column types
- Adding foreign keys or constraints

**What it produces**:
- Migration up script (SQL)
- Migration down script (rollback)
- Migration README with execution plan
- Safety checks and verification queries

**Example**:
```
Create a migration to add a 'status' column to the orders table with values: pending, processing, completed, cancelled.
```

**Skills**: Reads `migration-management/SKILL.md` for expert patterns

**Tools**: Read, Write, Grep, Glob

---

### 4. backup-strategist (Sonnet)

Designs backup and disaster recovery strategies.

**When to use**:
- Planning backup strategy
- Need disaster recovery procedures
- Setting up automated backups
- Defining RPO/RTO requirements

**What it produces**:
- Backup scripts (full, incremental, PITR)
- Recovery procedures
- Disaster recovery plan
- Monitoring and alerting setup

**Example**:
```
Design a backup strategy with RPO=1 hour and RTO=4 hours for a PostgreSQL database.
```

**Tools**: Read, Write, Bash

---

## Skills

### schema-design

Expert patterns for:
- Normalization (1NF, 2NF, 3NF, BCNF)
- Primary key selection (UUID vs auto-increment)
- Foreign key constraints and cascading
- Check constraints for business rules
- Index strategy (B-tree, GIN, GiST, partial, covering)
- Common schema patterns (soft delete, audit trail, many-to-many)
- Database-specific best practices (PostgreSQL, MySQL, SQLite)

### query-optimization

Expert patterns for:
- Reading execution plans (EXPLAIN output)
- Join algorithm selection (nested loop, hash, merge)
- Index selection rules
- Composite index column ordering
- Partial and expression indexes
- Common query anti-patterns (N+1, SELECT *, functions on indexed columns)
- Advanced optimization (materialized views, partitioning, connection pooling)
- Monitoring and diagnostics

### migration-management

Expert patterns for:
- Zero-downtime migration strategies
- Safe column addition/removal
- Index creation (CONCURRENTLY)
- Type changes and renaming
- Foreign key addition (NOT VALID, then VALIDATE)
- Batching large updates
- Framework-specific migrations (Alembic, Liquibase, Rails, Flyway)
- Rollback procedures

## Templates

### schema-template.sql

Complete database schema template with:
- UUID extension setup
- Users and roles tables
- Many-to-many junction table
- Proper indexes and constraints
- Comments and default data

### migration-template.sql

Production-ready migration template with:
- Pre-flight checks
- Transaction handling
- Concurrent index creation
- Batched backfill pattern
- Verification queries
- Rollback script

### er-diagram-template.md

ER diagram template with:
- Mermaid diagram syntax
- Relationship documentation
- Table descriptions
- Index strategy
- Design decisions
- Migration path

## Installation

### User-Level (All Projects)

```bash
# Copy plugin to user plugins directory
cp -r plugins/database-architect ~/.claude/plugins/

# Verify installation
ls ~/.claude/plugins/database-architect/agents/
```

### Project-Level (Single Project)

```bash
# Copy plugin to project .claude directory
cp -r plugins/database-architect .claude/plugins/

# Commit to version control
git add .claude/plugins/database-architect/
git commit -m "Add database-architect plugin"
```

## Usage Examples

### Example 1: Design New Schema

```bash
# Invoke schema-designer
@schema-designer "Design a schema for a blog platform with users, posts, comments, and tags."
```

**Output**:
- ER diagram in Mermaid format
- SQL DDL file: `.claude/database/schema.sql`
- Design documentation: `.claude/database/schema-design.md`

### Example 2: Optimize Slow Query

```bash
# Invoke query-optimizer
@query-optimizer "Optimize this query:
SELECT p.*, u.name as author, COUNT(c.id) as comment_count
FROM posts p
JOIN users u ON u.id = p.user_id
LEFT JOIN comments c ON c.post_id = p.id
WHERE p.published = true
GROUP BY p.id, u.name
ORDER BY p.created_at DESC
LIMIT 20;"
```

**Output**:
- Execution plan analysis
- Index recommendations
- Optimized query
- Expected performance improvement

### Example 3: Create Migration

```bash
# Invoke migration-manager
@migration-manager "Create a migration to add a 'slug' column to the posts table. Should be unique and indexed."
```

**Output**:
- Migration up: `db/migrations/20250120143000_add_slug_to_posts.sql`
- Migration down: `db/migrations/20250120143000_add_slug_to_posts_down.sql`
- Migration README with safety checks

### Example 4: Backup Strategy

```bash
# Invoke backup-strategist
@backup-strategist "Design a backup strategy for PostgreSQL with:
- RPO: 1 hour (max 1 hour data loss)
- RTO: 4 hours (max 4 hour recovery time)
- 30 day retention"
```

**Output**:
- Backup scripts: `ops/backup-scripts/`
- Recovery procedures: `ops/DR-PLAN.md`
- Monitoring setup: `ops/MONITORING.md`

## Workflow

### Complete Feature Development

```bash
# 1. Design schema
@schema-designer "Design schema for user authentication with OAuth providers"

# 2. Review and approve schema

# 3. Create migration
@migration-manager "Create migration for the authentication schema"

# 4. Deploy migration to dev
psql mydb_dev -f db/migrations/20250120_create_auth_schema.sql

# 5. Verify performance
@query-optimizer "Analyze performance of login query:
SELECT u.*, p.provider_name
FROM users u
JOIN auth_providers p ON p.user_id = u.id
WHERE u.email = 'user@example.com';"

# 6. Add recommended indexes
@migration-manager "Create migration to add indexes from query-optimizer recommendations"

# 7. Set up backups
@backup-strategist "Create backup scripts for the authentication database"
```

## Best Practices

### Schema Design

- Always use transactions for DDL changes
- Add foreign keys for referential integrity
- Index all foreign key columns
- Use check constraints for business rules
- Normalize to at least 3NF, denormalize only with justification
- Document design decisions in comments

### Query Optimization

- Use EXPLAIN ANALYZE before optimizing
- Start with schema optimization (indexes, constraints)
- Then optimize queries (rewrite, add LIMIT)
- Finally consider caching or denormalization
- Monitor query performance over time

### Migrations

- Test migrations on production-sized datasets
- Use zero-downtime patterns (CONCURRENTLY, NOT VALID)
- Always create rollback scripts
- Batch large updates to avoid long locks
- Document estimated execution time

### Backups

- Follow 3-2-1 rule: 3 copies, 2 media types, 1 off-site
- Test restore procedures quarterly
- Automate backup verification
- Monitor backup age and success rate
- Document disaster recovery procedures

## Database Support

### PostgreSQL (Primary)

**Fully Supported**:
- UUID extensions
- JSONB columns
- Array types
- Full-text search (tsvector)
- Partial indexes
- Expression indexes
- Concurrent index creation
- Foreign key with NOT VALID
- EXPLAIN ANALYZE with BUFFERS

**Version**: 12+ (14+ recommended)

### MySQL

**Supported**:
- InnoDB engine
- Online DDL (ALGORITHM=INPLACE, LOCK=NONE)
- Full-text search
- JSON columns
- Generated columns
- Partitioning

**Version**: 8.0+

### SQLite

**Supported**:
- STRICT tables (3.37+)
- WITHOUT ROWID optimization
- Triggers for complex constraints
- Partial indexes

**Version**: 3.35+ (3.37+ recommended)

## Troubleshooting

### Schema Designer Not Finding Skills

**Problem**: Agent doesn't read skill file

**Solution**:
```bash
# Verify skill file exists
ls -la .claude/skills/schema-design/SKILL.md
ls -la ~/.claude/skills/schema-design/SKILL.md

# If missing, copy from plugin
cp plugins/database-architect/skills/schema-design/SKILL.md ~/.claude/skills/schema-design/
```

### Migration Fails to Run

**Problem**: Migration script has errors

**Solution**:
1. Test migration on development database first
2. Check transaction block (BEGIN/COMMIT)
3. Verify pre-flight checks pass
4. Review PostgreSQL/MySQL logs for details

### Query Optimizer Suggests Wrong Indexes

**Problem**: Statistics are outdated

**Solution**:
```sql
-- PostgreSQL: Update statistics
ANALYZE orders;

-- MySQL: Update statistics
ANALYZE TABLE orders;

-- Then re-run query optimization
```

### Backup Scripts Don't Run

**Problem**: Permission or path issues

**Solution**:
```bash
# Check execute permissions
chmod +x ops/backup-scripts/backup-full.sh

# Check backup directory exists
mkdir -p /backups/postgres

# Check PostgreSQL user permissions
sudo -u postgres psql -c "SELECT current_user;"
```

## Contributing

Improvements welcome! Key areas:

- Additional schema patterns (temporal tables, event sourcing)
- More optimization techniques (query hints, optimizer statistics)
- Framework integrations (Django, Sequelize, Prisma)
- Cloud-specific guidance (RDS, Cloud SQL, Aurora)

## Resources

### Documentation

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Database Normalization](https://en.wikipedia.org/wiki/Database_normalization)

### Tools

- [pgAdmin](https://www.pgadmin.org/) - PostgreSQL GUI
- [DBeaver](https://dbeaver.io/) - Universal database tool
- [pg_badger](https://github.com/darold/pgbadger) - PostgreSQL log analyzer
- [pt-query-digest](https://www.percona.com/doc/percona-toolkit/LATEST/pt-query-digest.html) - MySQL slow query analyzer

## License

Part of the Puerto plugin ecosystem.

## Issues & Support

For bugs or feature requests related to this plugin, please file an issue in the Puerto repository.

---

**Version**: 1.0.0
**Last Updated**: 2025-01-20
**Maintainer**: database-architect agents
