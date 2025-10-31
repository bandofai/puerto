# Database Design Skill

**Expert patterns for relational and NoSQL database design, schema optimization, and performance tuning**

## Core Principles

1. **Normalize Then Denormalize**: Start with proper normalization, denormalize only when performance demands
2. **Index Strategically**: Index for queries, not for tables
3. **Choose Right Data Types**: Storage and performance implications
4. **Plan for Growth**: Sharding, partitioning, archiving strategies
5. **Constraints Enforce Integrity**: Use foreign keys, checks, unique constraints

---

## Normalization Forms

### First Normal Form (1NF)

**Rules**:
- Each column contains atomic values (no arrays, no lists)
- Each column has a unique name
- Order of rows/columns doesn't matter
- Each row is unique (has primary key)

**Example**:

❌ **Not in 1NF**:
```
users
| id | name | phones                     |
|----|------|----------------------------|
| 1  | John | 555-1234, 555-5678        |
| 2  | Jane | 555-9999                  |
```

✅ **In 1NF**:
```
users
| id | name |
|----|------|
| 1  | John |
| 2  | Jane |

user_phones
| user_id | phone    |
|---------|----------|
| 1       | 555-1234 |
| 1       | 555-5678 |
| 2       | 555-9999 |
```

### Second Normal Form (2NF)

**Rules**:
- Must be in 1NF
- All non-key columns must depend on the **entire** primary key (no partial dependencies)

**Example**:

❌ **Not in 2NF** (composite key with partial dependency):
```
order_items
| order_id | product_id | product_name | quantity | price |
|----------|------------|--------------|----------|-------|
| 1        | 101        | Widget       | 5        | 10.00 |
| 1        | 102        | Gadget       | 2        | 20.00 |

Problem: product_name depends only on product_id, not on (order_id, product_id)
```

✅ **In 2NF**:
```
products
| product_id | product_name |
|------------|--------------|
| 101        | Widget       |
| 102        | Gadget       |

order_items
| order_id | product_id | quantity | price |
|----------|------------|----------|-------|
| 1        | 101        | 5        | 10.00 |
| 1        | 102        | 2        | 20.00 |
```

### Third Normal Form (3NF)

**Rules**:
- Must be in 2NF
- No transitive dependencies (non-key columns depend only on primary key, not on other non-key columns)

**Example**:

❌ **Not in 3NF**:
```
employees
| id | name  | department_id | department_name |
|----|-------|---------------|-----------------|
| 1  | John  | 10            | Engineering     |
| 2  | Jane  | 20            | Sales           |

Problem: department_name depends on department_id, not directly on id
```

✅ **In 3NF**:
```
employees
| id | name  | department_id |
|----|-------|---------------|
| 1  | John  | 10            |
| 2  | Jane  | 20            |

departments
| id | name        |
|----|-------------|
| 10 | Engineering |
| 20 | Sales       |
```

### When to Denormalize

**Reasons to denormalize**:
1. **Read performance**: Avoid complex joins
2. **Aggregations**: Pre-calculate sums, counts
3. **Historical data**: Snapshot data at point in time
4. **Reporting**: Separate OLAP tables from OLTP

**Example - Denormalized for Performance**:
```sql
-- Normalized (3 joins for every query)
SELECT o.id, u.name, u.email, p.name as product_name, oi.quantity
FROM orders o
JOIN users u ON o.user_id = u.id
JOIN order_items oi ON oi.order_id = o.id
JOIN products p ON oi.product_id = p.id;

-- Denormalized (no joins, faster)
order_summary
| id | user_name | user_email      | product_name | quantity |
|----|-----------|-----------------|--------------|----------|
| 1  | John      | john@example.com| Widget       | 5        |

-- Trade-off: Data redundancy, update complexity
```

---

## Primary Keys

### UUID vs Auto-Increment

**UUID (Universally Unique Identifier)**:
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) NOT NULL
);
```

**Pros**:
- Globally unique (distributed systems)
- Generate client-side
- No central coordination
- Merge databases easily
- No enumeration attacks

**Cons**:
- 16 bytes (vs 4 bytes for INT, 8 for BIGINT)
- Random order affects B-tree inserts
- Less human-readable
- Slightly slower joins

**Auto-Increment (SERIAL/IDENTITY)**:
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,  -- PostgreSQL
    -- id INT AUTO_INCREMENT PRIMARY KEY,  -- MySQL
    email VARCHAR(255) NOT NULL
);
```

**Pros**:
- Smaller (4 or 8 bytes)
- Sequential (B-tree friendly)
- Human-readable
- Sortable by creation order

**Cons**:
- Not globally unique
- Reveals business metrics (user count)
- Coordination in distributed systems
- ID reuse issues

**Recommendation**:
- **UUID**: Microservices, distributed systems, multi-region
- **Auto-increment**: Single server, simple apps, internal tools

### Composite Primary Keys

**For junction tables**:
```sql
CREATE TABLE user_roles (
    user_id UUID NOT NULL REFERENCES users(id),
    role_id UUID NOT NULL REFERENCES roles(id),
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, role_id)
);
```

**For time-series data**:
```sql
CREATE TABLE metrics (
    device_id UUID NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    value FLOAT NOT NULL,
    PRIMARY KEY (device_id, timestamp)
);
```

---

## Foreign Keys and Relationships

### One-to-One

**Use case**: User profile, settings

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE user_profiles (
    id UUID PRIMARY KEY,
    user_id UUID UNIQUE NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    bio TEXT,
    avatar_url VARCHAR(512)
);
```

**Design choice**: Sometimes better as same table with nullable columns

### One-to-Many

**Use case**: User has many posts

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE posts (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    content TEXT
);

-- Index foreign key for join performance
CREATE INDEX idx_posts_user_id ON posts(user_id);
```

### Many-to-Many

**Use case**: Posts have many tags, tags have many posts

```sql
CREATE TABLE posts (
    id UUID PRIMARY KEY,
    title VARCHAR(255) NOT NULL
);

CREATE TABLE tags (
    id UUID PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- Junction table
CREATE TABLE post_tags (
    post_id UUID NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
    tag_id UUID NOT NULL REFERENCES tags(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (post_id, tag_id)
);

-- Indexes for both directions of join
CREATE INDEX idx_post_tags_tag_id ON post_tags(tag_id);
```

### Referential Actions

```sql
CREATE TABLE posts (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES users(id)
        ON DELETE CASCADE      -- Delete posts when user deleted
        ON UPDATE CASCADE      -- Update posts if user ID changes
);

-- Options:
-- CASCADE: Propagate change/delete
-- SET NULL: Set foreign key to NULL
-- SET DEFAULT: Set to default value
-- RESTRICT: Prevent change/delete (default)
-- NO ACTION: Same as RESTRICT
```

---

## Indexing Strategy

### Index Types

**B-Tree (Default)**:
```sql
-- Good for: =, <, >, <=, >=, BETWEEN, ORDER BY
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_posts_created_at ON posts(created_at DESC);
```

**Partial Index**:
```sql
-- Index only subset of rows
CREATE INDEX idx_published_posts ON posts(published_at)
WHERE status = 'published';

-- Smaller index, faster queries for published posts
```

**Composite Index**:
```sql
-- For queries with multiple WHERE conditions
CREATE INDEX idx_posts_user_status ON posts(user_id, status);

-- Order matters! Useful for:
-- WHERE user_id = ? AND status = ?
-- WHERE user_id = ?
-- But NOT for: WHERE status = ? (alone)
```

**Unique Index**:
```sql
-- Enforce uniqueness
CREATE UNIQUE INDEX idx_users_email ON users(email);

-- Case-insensitive unique
CREATE UNIQUE INDEX idx_users_email_lower ON users(LOWER(email));
```

**Full-Text Search (PostgreSQL)**:
```sql
-- GIN index for full-text search
CREATE INDEX idx_posts_search ON posts
USING GIN (to_tsvector('english', title || ' ' || content));

-- Query:
SELECT * FROM posts
WHERE to_tsvector('english', title || ' ' || content) @@ to_tsquery('postgresql & performance');
```

**JSON Index (PostgreSQL)**:
```sql
-- For JSONB columns
CREATE INDEX idx_metadata ON users USING GIN (metadata);

-- Query:
SELECT * FROM users WHERE metadata @> '{"premium": true}';
```

### Indexing Best Practices

**DO index**:
- Primary keys (automatic)
- Foreign keys (CRITICAL for joins!)
- Columns in WHERE clauses
- Columns in JOIN conditions
- Columns in ORDER BY
- High cardinality columns (many distinct values)

**DON'T index**:
- Small tables (<1000 rows)
- Low cardinality columns (gender, boolean)
- Columns rarely queried
- Write-heavy tables (indexes slow writes)

**Index Maintenance**:
```sql
-- Find unused indexes (PostgreSQL)
SELECT
    schemaname || '.' || tablename as table,
    indexname as index,
    idx_scan as scans,
    pg_size_pretty(pg_relation_size(indexrelid)) as size
FROM pg_stat_user_indexes
WHERE idx_scan = 0
  AND indexrelname NOT LIKE '%_pkey'
ORDER BY pg_relation_size(indexrelid) DESC;

-- Find missing indexes (high seq scans)
SELECT
    schemaname || '.' || tablename as table,
    seq_scan,
    seq_tup_read,
    idx_scan,
    seq_tup_read / seq_scan as avg_seq_read
FROM pg_stat_user_tables
WHERE seq_scan > 0
ORDER BY seq_tup_read DESC
LIMIT 20;
```

---

## Data Types

### PostgreSQL Data Types

| Category | Type | Size | Use Case |
|----------|------|------|----------|
| **Integers** | SMALLINT | 2 bytes | -32K to 32K |
| | INTEGER | 4 bytes | -2B to 2B (most common) |
| | BIGINT | 8 bytes | Large numbers |
| **Decimals** | NUMERIC(p,s) | Variable | Exact decimals (money) |
| | REAL | 4 bytes | Approximate (6 digits) |
| | DOUBLE PRECISION | 8 bytes | Approximate (15 digits) |
| **Strings** | VARCHAR(n) | Variable | Variable length, limit |
| | TEXT | Variable | Unlimited text |
| | CHAR(n) | Fixed | Fixed length, padded |
| **Binary** | BYTEA | Variable | Binary data |
| **Boolean** | BOOLEAN | 1 byte | TRUE/FALSE |
| **Date/Time** | DATE | 4 bytes | Date only |
| | TIME | 8 bytes | Time only |
| | TIMESTAMP | 8 bytes | Date + time |
| | TIMESTAMPTZ | 8 bytes | Date + time + timezone ✅ |
| **JSON** | JSON | Variable | JSON text |
| | JSONB | Variable | Binary JSON (indexed) ✅ |
| **Arrays** | type[] | Variable | Array of any type |
| **UUID** | UUID | 16 bytes | Unique identifiers |

### Type Selection Guidelines

**Money**: Always use NUMERIC
```sql
price NUMERIC(10, 2)  -- Max $99,999,999.99
```
❌ Never use FLOAT/REAL for money (rounding errors)

**Timestamps**: Always use TIMESTAMPTZ
```sql
created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
```
✅ Stores in UTC, converts to client timezone

**Enums**: Use VARCHAR with CHECK constraint or native ENUM
```sql
-- Option 1: VARCHAR with CHECK
status VARCHAR(20) NOT NULL CHECK (status IN ('draft', 'published', 'archived'))

-- Option 2: Native ENUM (harder to modify)
CREATE TYPE post_status AS ENUM ('draft', 'published', 'archived');
status post_status NOT NULL DEFAULT 'draft'
```

**JSON**: Use JSONB for flexible schema
```sql
metadata JSONB

-- Query:
SELECT * FROM users WHERE metadata->>'plan' = 'premium';
SELECT * FROM users WHERE metadata @> '{"features": {"analytics": true}}';
```

---

## Constraints

### NOT NULL

```sql
email VARCHAR(255) NOT NULL
```
Always enforce required fields

### UNIQUE

```sql
email VARCHAR(255) UNIQUE NOT NULL

-- or explicitly:
CONSTRAINT unique_email UNIQUE (email)
```

### CHECK

```sql
age INTEGER CHECK (age >= 0 AND age <= 150)

price NUMERIC(10,2) CHECK (price > 0)

status VARCHAR(20) CHECK (status IN ('active', 'inactive', 'suspended'))
```

### DEFAULT

```sql
created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
status VARCHAR(20) DEFAULT 'active'
is_verified BOOLEAN DEFAULT FALSE
```

### Foreign Key

```sql
user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE
```

---

## Performance Optimization

### Query Optimization

**Use EXPLAIN ANALYZE**:
```sql
EXPLAIN ANALYZE
SELECT u.name, COUNT(p.id) as post_count
FROM users u
LEFT JOIN posts p ON p.user_id = u.id
GROUP BY u.id, u.name
ORDER BY post_count DESC
LIMIT 10;
```

**Optimization Techniques**:

1. **Add indexes for WHERE, JOIN, ORDER BY**
2. **Use covering indexes** (include all query columns)
3. **Avoid SELECT ***, select only needed columns
4. **Use EXISTS instead of COUNT** for existence checks
5. **Batch inserts** instead of individual
6. **Use connection pooling**
7. **Partition large tables**

**Example - Covering Index**:
```sql
-- Query:
SELECT id, email, name FROM users WHERE status = 'active' ORDER BY created_at;

-- Covering index (no table lookup needed):
CREATE INDEX idx_active_users_covering
ON users(status, created_at, id, email, name)
WHERE status = 'active';
```

### N+1 Query Problem

❌ **N+1 Queries** (BAD):
```python
# 1 query for users
users = db.query(User).all()

# N queries for posts (one per user)
for user in users:
    posts = db.query(Post).filter_by(user_id=user.id).all()
```

✅ **Single Query with JOIN** (GOOD):
```python
# 1 query total
users_with_posts = db.query(User).options(
    joinedload(User.posts)
).all()
```

### Connection Pooling

```python
# SQLAlchemy example
from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://user:pass@localhost/db',
    pool_size=10,              # Persistent connections
    max_overflow=20,           # Additional connections when pool full
    pool_timeout=30,           # Wait 30s for connection
    pool_recycle=3600,         # Recycle connections every hour
    pool_pre_ping=True         # Verify connection before use
)
```

**Pool Size Calculation**:
```
Recommended pool size = (num_CPUs * 2) + 1
Example: 4 CPUs → pool_size = 9
```

---

## Migration Patterns

### Zero-Downtime Migrations

**Add Column**:
```sql
-- Step 1: Add column as nullable
ALTER TABLE users ADD COLUMN full_name VARCHAR(200);

-- Step 2: Backfill data (in batches)
UPDATE users SET full_name = first_name || ' ' || last_name
WHERE full_name IS NULL;

-- Step 3: Make NOT NULL after backfill
ALTER TABLE users ALTER COLUMN full_name SET NOT NULL;
```

**Remove Column**:
```sql
-- Step 1: Stop writing to column (deploy code)
-- Step 2: Drop column
ALTER TABLE users DROP COLUMN middle_name;
```

**Rename Column**:
```sql
-- Step 1: Add new column
ALTER TABLE users ADD COLUMN email_address VARCHAR(255);

-- Step 2: Copy data
UPDATE users SET email_address = email;

-- Step 3: Deploy code using both columns

-- Step 4: Drop old column
ALTER TABLE users DROP COLUMN email;

-- Step 5: Rename new column (optional)
ALTER TABLE users RENAME COLUMN email_address TO email;
```

**Add Index** (without blocking writes):
```sql
-- PostgreSQL
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);

-- MySQL
ALTER TABLE users ADD INDEX idx_users_email (email), ALGORITHM=INPLACE, LOCK=NONE;
```

### Migration File Template

```sql
-- Migration: 20250120_add_user_roles
-- Description: Add role-based access control

-- Up Migration
BEGIN;

-- 1. Create roles table
CREATE TABLE roles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- 2. Create user_roles junction table
CREATE TABLE user_roles (
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    role_id UUID NOT NULL REFERENCES roles(id) ON DELETE CASCADE,
    assigned_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, role_id)
);

-- 3. Add indexes
CREATE INDEX idx_user_roles_role_id ON user_roles(role_id);

-- 4. Insert default roles
INSERT INTO roles (name, description) VALUES
    ('admin', 'Administrator with full access'),
    ('user', 'Regular user'),
    ('guest', 'Guest with limited access');

COMMIT;

-- Down Migration (commented for safety)
-- BEGIN;
-- DROP TABLE user_roles;
-- DROP TABLE roles;
-- COMMIT;
```

---

## Partitioning

### When to Partition

**Use partitioning when**:
- Table > 10M rows
- Time-series data
- Clear partitioning key
- Old data rarely accessed

### Partition Types

**Range Partitioning** (by date):
```sql
CREATE TABLE metrics (
    id BIGSERIAL,
    device_id UUID NOT NULL,
    value FLOAT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL
) PARTITION BY RANGE (created_at);

-- Create partitions
CREATE TABLE metrics_2025_01 PARTITION OF metrics
    FOR VALUES FROM ('2025-01-01') TO ('2025-02-01');

CREATE TABLE metrics_2025_02 PARTITION OF metrics
    FOR VALUES FROM ('2025-02-01') TO ('2025-03-01');

-- Queries automatically route to correct partition
SELECT * FROM metrics WHERE created_at >= '2025-01-15';
```

**List Partitioning** (by region):
```sql
CREATE TABLE users (
    id UUID,
    region VARCHAR(20) NOT NULL,
    name VARCHAR(100)
) PARTITION BY LIST (region);

CREATE TABLE users_us PARTITION OF users
    FOR VALUES IN ('US', 'CA', 'MX');

CREATE TABLE users_eu PARTITION OF users
    FOR VALUES IN ('UK', 'FR', 'DE');
```

**Hash Partitioning** (by ID):
```sql
CREATE TABLE orders (
    id UUID NOT NULL,
    amount NUMERIC(10,2)
) PARTITION BY HASH (id);

CREATE TABLE orders_0 PARTITION OF orders FOR VALUES WITH (MODULUS 4, REMAINDER 0);
CREATE TABLE orders_1 PARTITION OF orders FOR VALUES WITH (MODULUS 4, REMAINDER 1);
CREATE TABLE orders_2 PARTITION OF orders FOR VALUES WITH (MODULUS 4, REMAINDER 2);
CREATE TABLE orders_3 PARTITION OF orders FOR VALUES WITH (MODULUS 4, REMAINDER 3);
```

---

## Best Practices Checklist

- [ ] All tables have primary keys
- [ ] Foreign key constraints defined
- [ ] Indexes on all foreign keys
- [ ] NOT NULL on required fields
- [ ] Appropriate data types chosen
- [ ] Timestamps (created_at, updated_at) on all tables
- [ ] Use TIMESTAMPTZ, not TIMESTAMP
- [ ] Money stored as NUMERIC, not FLOAT
- [ ] UUIDs for distributed systems
- [ ] Schema normalized to 3NF (then denormalize if needed)
- [ ] Soft deletes considered (deleted_at column)
- [ ] Migration files for all schema changes
- [ ] Indexes reviewed with EXPLAIN ANALYZE
- [ ] Connection pooling configured
- [ ] Backup and recovery plan

---

**Version**: 1.0
**Last Updated**: January 2025
**Use Cases**: Database schema design, optimization, migrations
