# Backend Architecture

**Comprehensive patterns for APIs, databases, and server-side systems**

Consolidated from:
- backend-architect skills
- api-developer skills
- database-architect skills

---





# Schema Design Skill

Expert patterns for relational database schema design, normalization, and constraint management.

## Core Principles

### 1. Normalization Levels

**1NF (First Normal Form)**:
- Atomic values only (no arrays, no comma-separated lists)
- Each column contains single value
- No repeating groups

**2NF (Second Normal Form)**:
- Must be in 1NF
- No partial dependencies on composite primary keys
- Every non-key column depends on the entire primary key

**3NF (Third Normal Form)**:
- Must be in 2NF
- No transitive dependencies
- Every non-key column depends only on the primary key

**BCNF (Boyce-Codd Normal Form)**:
- Must be in 3NF
- Every determinant is a candidate key

**Strategic Denormalization**:
- Only denormalize with performance data justification
- Document the trade-off
- Consider materialized views instead
- Plan for data consistency maintenance

### 2. Primary Key Selection

**UUID (Recommended for distributed systems)**:
```sql
id UUID PRIMARY KEY DEFAULT uuid_generate_v4()
```
- Pros: Globally unique, no coordination needed, harder to enumerate
- Cons: Larger storage (16 bytes), random order (index fragmentation)

**Auto-increment Integer**:
```sql
id SERIAL PRIMARY KEY  -- PostgreSQL
id INT AUTO_INCREMENT PRIMARY KEY  -- MySQL
id INTEGER PRIMARY KEY AUTOINCREMENT  -- SQLite
```
- Pros: Small storage (4-8 bytes), sequential (better index performance)
- Cons: Coordination needed, easy to enumerate, not globally unique

**Composite Keys** (for junction tables):
```sql
PRIMARY KEY (user_id, role_id)
```

### 3. Foreign Key Constraints

**Always define foreign keys** for referential integrity:

```sql
CONSTRAINT fk_orders_customer
    FOREIGN KEY (customer_id)
    REFERENCES customers(id)
    ON DELETE CASCADE  -- or RESTRICT, SET NULL
    ON UPDATE CASCADE
```

**ON DELETE options**:
- `CASCADE`: Delete child rows when parent deleted
- `RESTRICT`: Prevent delete if children exist
- `SET NULL`: Set foreign key to NULL
- `NO ACTION`: Similar to RESTRICT (database-specific)

### 4. Check Constraints

**Use check constraints for business rules**:

```sql
-- Email format validation
CONSTRAINT email_format CHECK (
    email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
)

-- Positive values
CONSTRAINT total_positive CHECK (total >= 0)

-- Enum-like values
CONSTRAINT valid_status CHECK (
    status IN ('pending', 'processing', 'completed', 'cancelled')
)

-- Date ranges
CONSTRAINT valid_date_range CHECK (end_date > start_date)
```

### 5. Index Strategy

**Index Types and When to Use**:

**B-Tree (Default)**:
- WHERE clauses: `WHERE status = 'active'`
- ORDER BY: `ORDER BY created_at DESC`
- Range queries: `WHERE price BETWEEN 10 AND 100`
- Joins: Foreign key columns

**GIN (PostgreSQL - Generalized Inverted Index)**:
- JSONB columns: `WHERE data @> '{"key": "value"}'`
- Arrays: `WHERE tags @> ARRAY['postgresql']`
- Full-text search: `WHERE to_tsvector(text) @@ to_tsquery('search')`

**GiST (PostgreSQL - Generalized Search Tree)**:
- Geometric data: `WHERE location && box '((0,0),(1,1))'`
- Full-text search: Alternative to GIN
- Range types: `WHERE daterange && '[2025-01-01, 2025-12-31]'`

**Hash (Limited use)**:
- Equality only: `WHERE id = 123`
- Not recommended (B-tree usually better)

**Composite Index Column Order**:
```sql
-- Rule: Most selective column first, or most commonly filtered
CREATE INDEX idx_orders_status_created ON orders(status, created_at DESC);

-- Works for:
-- WHERE status = 'pending'  ✅
-- WHERE status = 'pending' AND created_at > NOW() - INTERVAL '7 days'  ✅
-- WHERE status = 'pending' ORDER BY created_at DESC  ✅

-- Does NOT work for:
-- WHERE created_at > NOW() - INTERVAL '7 days'  ❌ (doesn't start with status)
```

## Schema Patterns

### Pattern 1: Soft Delete

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    deleted_at TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Partial unique index (only for non-deleted rows)
CREATE UNIQUE INDEX idx_users_email_active
ON users(email)
WHERE deleted_at IS NULL;

-- Query pattern: Always filter deleted
SELECT * FROM users WHERE deleted_at IS NULL;
```

### Pattern 2: Audit Trail

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by UUID REFERENCES users(id),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by UUID REFERENCES users(id)
);

-- Separate audit log table for full history
CREATE TABLE users_audit (
    audit_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL,
    operation VARCHAR(10) NOT NULL,  -- INSERT, UPDATE, DELETE
    old_values JSONB,
    new_values JSONB,
    changed_by UUID REFERENCES users(id),
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Pattern 3: Many-to-Many with Metadata

```sql
-- Junction table with additional attributes
CREATE TABLE user_roles (
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    role_id UUID REFERENCES roles(id) ON DELETE CASCADE,
    granted_by UUID REFERENCES users(id),
    granted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP,

    PRIMARY KEY (user_id, role_id)
);

CREATE INDEX idx_user_roles_user ON user_roles(user_id);
CREATE INDEX idx_user_roles_role ON user_roles(role_id);
CREATE INDEX idx_user_roles_expires ON user_roles(expires_at)
WHERE expires_at IS NOT NULL;
```

### Pattern 4: Hierarchical Data (Adjacency List)

```sql
CREATE TABLE categories (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    parent_id UUID REFERENCES categories(id),
    path TEXT,  -- Materialized path: /electronics/computers/laptops
    level INT,  -- Denormalized for performance
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_categories_parent ON categories(parent_id);
CREATE INDEX idx_categories_path ON categories(path);
```

### Pattern 5: Polymorphic Associations (Avoid if Possible)

**❌ Problematic Approach**:
```sql
-- Weak referential integrity
CREATE TABLE comments (
    id UUID PRIMARY KEY,
    content TEXT NOT NULL,
    commentable_type VARCHAR(50),  -- 'Post' or 'Photo'
    commentable_id UUID,           -- No real foreign key!
    created_at TIMESTAMP
);
```

**✅ Better Approach (Exclusive Arcs)**:
```sql
CREATE TABLE comments (
    id UUID PRIMARY KEY,
    content TEXT NOT NULL,
    post_id UUID REFERENCES posts(id) ON DELETE CASCADE,
    photo_id UUID REFERENCES photos(id) ON DELETE CASCADE,
    created_at TIMESTAMP,

    -- Exactly one must be set
    CONSTRAINT one_commentable CHECK (
        (post_id IS NOT NULL AND photo_id IS NULL) OR
        (post_id IS NULL AND photo_id IS NOT NULL)
    )
);

CREATE INDEX idx_comments_post ON comments(post_id);
CREATE INDEX idx_comments_photo ON comments(photo_id);
```

## Naming Conventions

**Tables**: Plural nouns, lowercase, underscores
```
users, orders, order_items, user_preferences
```

**Columns**: Singular nouns, lowercase, underscores
```
id, email, first_name, created_at, customer_id
```

**Primary Keys**: Always `id`
```
id UUID PRIMARY KEY
```

**Foreign Keys**: `{referenced_table_singular}_id`
```
customer_id, product_id, user_id
```

**Indexes**: `idx_{table}_{column(s)}[_{condition}]`
```
idx_users_email
idx_orders_customer_id
idx_orders_status_created
idx_users_email_active (partial index)
```

**Constraints**: `{type}_{table}_{description}`
```
pk_users (primary key)
fk_orders_customer (foreign key)
uq_users_email (unique)
ck_orders_total_positive (check)
```

## Common Anti-Patterns to Avoid

**❌ Generic JSON Columns (EAV Pattern)**:
```sql
-- Bad: No schema, no constraints, no indexes
CREATE TABLE entities (
    id UUID PRIMARY KEY,
    type VARCHAR(50),
    attributes JSONB
);
```

**❌ Comma-Separated Lists**:
```sql
-- Bad: Violates 1NF, can't join efficiently
CREATE TABLE users (
    id UUID PRIMARY KEY,
    tags TEXT  -- 'javascript,python,sql'
);
```

**✅ Use junction table instead**:
```sql
CREATE TABLE user_tags (
    user_id UUID REFERENCES users(id),
    tag_id UUID REFERENCES tags(id),
    PRIMARY KEY (user_id, tag_id)
);
```

**❌ Nullable Boolean Columns**:
```sql
-- Bad: Three states (true, false, null) - ambiguous
is_active BOOLEAN NULL
```

**✅ Be explicit**:
```sql
-- Good: Two clear states
is_active BOOLEAN NOT NULL DEFAULT true
```

## ER Diagram Notation (Mermaid)

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER {
        uuid id PK "Primary Key"
        string email UK "Unique Key"
        string name
        timestamp created_at
    }

    ORDER ||--|{ LINE_ITEM : contains
    ORDER {
        uuid id PK
        uuid customer_id FK
        decimal total
        string status
    }

    PRODUCT ||--o{ LINE_ITEM : "ordered in"
    LINE_ITEM {
        uuid id PK
        uuid order_id FK
        uuid product_id FK
        int quantity
        decimal unit_price
    }
```

**Cardinality Symbols**:
- `||--||` : One to exactly one
- `||--o|` : One to zero or one
- `||--o{` : One to zero or more
- `}|--|{` : One or more to one or more

## Database-Specific Best Practices

### PostgreSQL

```sql
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Use JSONB (not JSON) for better performance
metadata JSONB

-- Use array types when appropriate
tags TEXT[]

-- Use full-text search
CREATE INDEX idx_products_search ON products
USING GIN (to_tsvector('english', name || ' ' || description));

-- Use enums for fixed sets
CREATE TYPE order_status AS ENUM ('pending', 'processing', 'completed', 'cancelled');
```

### MySQL

```sql
-- Use InnoDB engine (default in 8.0+)
ENGINE=InnoDB

-- Use UTF8MB4 for full Unicode support (including emoji)
DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci

-- Use generated columns for computed values
price_with_tax DECIMAL(10,2) GENERATED ALWAYS AS (price * 1.20) STORED

-- Partition large tables
PARTITION BY RANGE (YEAR(created_at)) (
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p2024 VALUES LESS THAN (2025),
    PARTITION p2025 VALUES LESS THAN (2026)
);
```

### SQLite

```sql
-- Use STRICT tables for type enforcement (3.37+)
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL,
    age INTEGER NOT NULL
) STRICT;

-- Use WITHOUT ROWID for space efficiency
CREATE TABLE user_settings (
    user_id INTEGER PRIMARY KEY,
    theme TEXT NOT NULL,
    locale TEXT NOT NULL
) WITHOUT ROWID;

-- Use triggers for complex constraints
CREATE TRIGGER check_age_before_insert
BEFORE INSERT ON users
FOR EACH ROW
WHEN NEW.age < 18
BEGIN
    SELECT RAISE(ABORT, 'Users must be 18 or older');
END;
```

## Quality Checklist

**Schema Completeness**:
- [ ] All tables have primary keys
- [ ] All relationships have foreign keys
- [ ] Appropriate NOT NULL constraints
- [ ] Check constraints for business rules
- [ ] Default values where appropriate
- [ ] Created_at/updated_at timestamps

**Normalization**:
- [ ] Schema is at least 3NF
- [ ] No repeating groups
- [ ] No partial dependencies
- [ ] No transitive dependencies
- [ ] Denormalization justified and documented

**Performance**:
- [ ] Indexes on all foreign keys
- [ ] Indexes on commonly filtered columns
- [ ] Composite indexes for multi-column queries
- [ ] Covering indexes for frequent queries
- [ ] Partial indexes where appropriate

**Maintainability**:
- [ ] Consistent naming conventions
- [ ] Clear table and column names
- [ ] Comments on complex structures
- [ ] ER diagram provided
- [ ] Design decisions documented

---

## MCP-Enhanced Schema Design

### PostgreSQL MCP for Schema Validation

When PostgreSQL MCP is available, validate schema designs directly against production databases:

```typescript
// Runtime detection - no configuration needed
const hasPostgres = typeof mcp__postgres__query !== 'undefined';

if (hasPostgres) {
  console.log("✓ Using PostgreSQL MCP for schema design validation");

  // Validate schema against existing database
  const schemaCheck = await mcp__postgres__query({
    sql: `
      SELECT
        table_name,
        column_name,
        data_type,
        is_nullable,
        column_default,
        character_maximum_length
      FROM information_schema.columns
      WHERE table_schema = 'public'
        AND table_name IN ('users', 'orders', 'products')
      ORDER BY table_name, ordinal_position
    `
  });

  console.log(`✓ Retrieved schema for ${schemaCheck.rows.length} columns`);

  // Check constraints
  const constraints = await mcp__postgres__query({
    sql: `
      SELECT
        tc.table_name,
        tc.constraint_name,
        tc.constraint_type,
        kcu.column_name,
        ccu.table_name AS foreign_table_name,
        ccu.column_name AS foreign_column_name
      FROM information_schema.table_constraints tc
      LEFT JOIN information_schema.key_column_usage kcu
        ON tc.constraint_name = kcu.constraint_name
      LEFT JOIN information_schema.constraint_column_usage ccu
        ON tc.constraint_name = ccu.constraint_name
      WHERE tc.table_schema = 'public'
      ORDER BY tc.table_name, tc.constraint_type
    `
  });

  console.log(`✓ Found ${constraints.rows.length} constraints`);

  // Validate foreign key relationships
  const orphanedRecords = await mcp__postgres__query({
    sql: `
      SELECT
        'orders' as table_name,
        COUNT(*) as orphaned_count
      FROM orders o
      LEFT JOIN users u ON o.user_id = u.id
      WHERE u.id IS NULL
    `
  });

  if (orphanedRecords.rows[0].orphaned_count > 0) {
    console.log(`⚠️  Found ${orphanedRecords.rows[0].orphaned_count} orphaned records`);
  } else {
    console.log("✓ All foreign key relationships valid");
  }

  // Test DDL before executing
  const ddlTest = await mcp__postgres__query({
    sql: `
      BEGIN;
      -- Test adding new column
      ALTER TABLE users ADD COLUMN test_column VARCHAR(100);
      -- Check table size after change
      SELECT pg_size_pretty(pg_relation_size('users')) as table_size;
      ROLLBACK;
    `
  });

  console.log(`✓ DDL validated (would not break existing data)`);

} else {
  console.log("ℹ️  PostgreSQL MCP not available");
  console.log("   Install for schema validation:");
  console.log("   npm install -g @modelcontextprotocol/server-postgres");
}
```

### Benefits Comparison

| Aspect | With PostgreSQL MCP | Without MCP (Traditional) |
|--------|-------------------|--------------------------|
| **Schema Exploration** | Query information_schema instantly | Request schema dump → wait |
| **Constraint Validation** | Check FK relationships on real data | Assume constraints work |
| **DDL Testing** | Test ALTER statements with ROLLBACK | Deploy and hope |
| **Data Distribution** | Analyze with pg_stats | Guess cardinality |
| **Impact Analysis** | Query actual table sizes | Estimate impact |
| **Normalization Check** | Find duplicates in production | Theoretical analysis |
| **Migration Safety** | Test on production replica | Cross fingers |

**When to use PostgreSQL MCP:**
- Designing schema for existing database
- Validating normalization against real data
- Testing DDL changes before deployment
- Analyzing data distribution for index design
- Finding schema anomalies
- Planning migrations
- Reverse engineering existing schemas

**When traditional approach needed:**
- Greenfield database design
- Designing for future data
- Theoretical schema modeling
- No database access

### Real-World Example: Adding User Preferences

**With PostgreSQL MCP (15 minutes):**

```typescript
// 1. Analyze current users table
const currentSchema = await mcp__postgres__query({
  sql: `
    SELECT
      column_name,
      data_type,
      is_nullable
    FROM information_schema.columns
    WHERE table_name = 'users'
    ORDER BY ordinal_position
  `
});

console.log(`✓ Users table has ${currentSchema.rows.length} columns`);

// 2. Check for existing preference data
const preferencesCheck = await mcp__postgres__query({
  sql: `
    SELECT
      COUNT(DISTINCT user_id) as users_with_prefs,
      COUNT(*) as total_prefs,
      AVG(array_length(string_to_array(preferences, ','), 1)) as avg_prefs_per_user
    FROM user_metadata
    WHERE preferences IS NOT NULL
  `
});

console.log(`✓ ${preferencesCheck.rows[0].users_with_prefs} users have preferences`);

// 3. Design decision: Separate table vs JSONB column
const tableSize = await mcp__postgres__query({
  sql: `
    SELECT
      pg_size_pretty(pg_relation_size('users')) as current_size,
      pg_size_pretty(pg_relation_size('users') * 1.2) as estimated_with_jsonb
  `
});

console.log(`✓ Adding JSONB column would increase size to ${tableSize.rows[0].estimated_with_jsonb}`);

// 4. Test the migration (with ROLLBACK)
const migrationTest = await mcp__postgres__query({
  sql: `
    BEGIN;

    -- Add preferences column
    ALTER TABLE users ADD COLUMN preferences JSONB DEFAULT '{}'::jsonb;

    -- Add GIN index for JSONB queries
    CREATE INDEX idx_users_preferences ON users USING GIN (preferences);

    -- Test query performance
    EXPLAIN ANALYZE
    SELECT * FROM users
    WHERE preferences @> '{"theme": "dark"}'::jsonb;

    ROLLBACK;
  `
});

console.log("✓ Migration tested successfully");

// Decision: Use JSONB column (flexible, good performance with GIN index)
```

**Without MCP (2 hours):**

1. Request schema documentation (15 min wait)
2. Analyze schema manually (20 min)
3. Make design decision based on assumptions (15 min)
4. Write migration script (15 min)
5. Deploy to test database (10 min)
6. Load test data (20 min)
7. Test queries (10 min)
8. Find issues (15 min)
9. Revise and redeploy (15 min)

### Schema Validation Patterns

```typescript
// Comprehensive schema validation
async function validateSchema() {
  const hasPostgres = typeof mcp__postgres__query !== 'undefined';

  if (hasPostgres) {
    // 1. Check for missing indexes on foreign keys
    const missingIndexes = await mcp__postgres__query({
      sql: `
        SELECT
          tc.table_name,
          kcu.column_name
        FROM information_schema.table_constraints tc
        JOIN information_schema.key_column_usage kcu
          ON tc.constraint_name = kcu.constraint_name
        WHERE tc.constraint_type = 'FOREIGN KEY'
          AND NOT EXISTS (
            SELECT 1
            FROM pg_indexes
            WHERE tablename = tc.table_name
              AND indexdef LIKE '%' || kcu.column_name || '%'
          )
      `
    });

    if (missingIndexes.rows.length > 0) {
      console.log("⚠️  Missing indexes on foreign keys:");
      missingIndexes.rows.forEach(row => {
        console.log(`  ${row.table_name}.${row.column_name}`);
      });
    }

    // 2. Check for columns that should be NOT NULL
    const nullableColumns = await mcp__postgres__query({
      sql: `
        SELECT
          table_name,
          column_name,
          COUNT(*) FILTER (WHERE value IS NULL) as null_count,
          COUNT(*) as total_count
        FROM (
          SELECT 'users' as table_name, 'email' as column_name, email as value FROM users
          UNION ALL
          SELECT 'orders' as table_name, 'user_id' as column_name, user_id::text as value FROM orders
        ) data
        GROUP BY table_name, column_name
        HAVING COUNT(*) FILTER (WHERE value IS NULL) = 0
          AND EXISTS (
            SELECT 1
            FROM information_schema.columns
            WHERE table_name = data.table_name
              AND column_name = data.column_name
              AND is_nullable = 'YES'
          )
      `
    });

    if (nullableColumns.rows.length > 0) {
      console.log("⚠️  Columns that could be NOT NULL:");
      nullableColumns.rows.forEach(row => {
        console.log(`  ${row.table_name}.${row.column_name} (0 NULLs in ${row.total_count} rows)`);
      });
    }

    // 3. Check for denormalization opportunities
    const duplicateData = await mcp__postgres__query({
      sql: `
        SELECT
          user_id,
          email,
          COUNT(*) as duplicate_count
        FROM users
        GROUP BY user_id, email
        HAVING COUNT(*) > 1
      `
    });

    return {
      missingIndexes: missingIndexes.rows,
      nullableColumns: nullableColumns.rows,
      duplicates: duplicateData.rows
    };
  }
}
```

### PostgreSQL MCP Installation

```bash
# Install PostgreSQL MCP
npm install -g @modelcontextprotocol/server-postgres

# Configure for schema design
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "postgresql://schema_designer:pass@db.company.com:5432/production"
      }
    }
  }
}
```

Once installed, all agents reading this skill automatically validate schemas against live databases.

### Schema Design Workflow with MCP

1. **Explore Existing Schema**: Query information_schema
2. **Analyze Data Distribution**: Use pg_stats
3. **Check Constraints**: Validate FK relationships
4. **Test DDL Changes**: Use BEGIN...ROLLBACK
5. **Estimate Impact**: Query table/index sizes
6. **Validate Normalization**: Find duplicates
7. **Plan Indexes**: Analyze query patterns
8. **Generate Migration**: Create safe DDL scripts

---

**Version**: 1.0
**Last Updated**: January 2025
**MCP Enhancement**: PostgreSQL for data-driven schema design
**Best Practices**: Industry-proven schema design patterns
