# Migration Management Skill

Expert patterns for zero-downtime database migrations, versioning, and rollback strategies.

## Core Principles

### 1. Zero-Downtime Migration Strategy

**The Golden Rule**: Never break backward compatibility during a migration.

**Multi-Step Approach**:
1. **Expand**: Add new structures (columns, tables, indexes) without removing old
2. **Migrate**: Dual-write to both old and new, backfill data
3. **Contract**: Remove old structures after confirming new ones work

### 2. Migration Safety Rules

**Always**:
- ✅ Test migrations on production-like data
- ✅ Use transactions (BEGIN/COMMIT) when possible
- ✅ Create rollback scripts
- ✅ Document estimated execution time
- ✅ Use CONCURRENTLY for index creation (PostgreSQL)
- ✅ Add foreign keys with NOT VALID, then validate
- ✅ Batch large updates (avoid long locks)

**Never**:
- ❌ Run untested migrations in production
- ❌ Drop columns/tables without multi-step process
- ❌ Add NOT NULL without default value first
- ❌ Change column types directly on large tables
- ❌ Create indexes without CONCURRENTLY on production
- ❌ Run long-running migrations during peak hours

## Safe Migration Patterns

### Pattern 1: Adding a Column

**✅ SAFE (three-step process)**:

**Step 1: Add column as nullable**
```sql
-- Migration: 20250120_01_add_status_column.sql
BEGIN;

ALTER TABLE orders
ADD COLUMN status VARCHAR(50);  -- Nullable initially

ALTER TABLE orders
ALTER COLUMN status SET DEFAULT 'pending';  -- Default for new rows

COMMIT;
```

**Step 2: Backfill existing rows** (run during low traffic)
```sql
-- Migration: 20250120_02_backfill_status.sql
-- Batch updates to avoid long locks
DO $$
DECLARE
    batch_size INT := 10000;
    updated INT;
BEGIN
    LOOP
        UPDATE orders
        SET status = 'pending'
        WHERE status IS NULL
          AND id IN (
              SELECT id FROM orders
              WHERE status IS NULL
              LIMIT batch_size
          );

        GET DIAGNOSTICS updated = ROW_COUNT;
        EXIT WHEN updated = 0;

        -- Brief pause between batches
        PERFORM pg_sleep(0.1);
    END LOOP;
END $$;
```

**Step 3: Add NOT NULL constraint** (after backfill complete)
```sql
-- Migration: 20250120_03_make_status_not_null.sql
BEGIN;

-- Verify no NULLs remain
DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM orders WHERE status IS NULL) THEN
        RAISE EXCEPTION 'Cannot add NOT NULL: NULL values still exist';
    END IF;
END $$;

ALTER TABLE orders
ALTER COLUMN status SET NOT NULL;

COMMIT;
```

### Pattern 2: Adding an Index

**✅ SAFE (PostgreSQL)**:
```sql
-- Use CONCURRENTLY to avoid table locks
-- Note: Cannot be run inside transaction block
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_orders_status
ON orders(status);

-- Verify index was created
SELECT schemaname, tablename, indexname, indexdef
FROM pg_indexes
WHERE indexname = 'idx_orders_status';
```

**✅ SAFE (MySQL)**:
```sql
-- MySQL 5.6+ supports online DDL for many operations
ALTER TABLE orders
ADD INDEX idx_orders_status (status),
ALGORITHM=INPLACE, LOCK=NONE;
```

**Rollback**:
```sql
-- PostgreSQL
DROP INDEX CONCURRENTLY IF EXISTS idx_orders_status;

-- MySQL
ALTER TABLE orders DROP INDEX idx_orders_status;
```

### Pattern 3: Renaming a Column

**❌ DANGEROUS (breaks application code)**:
```sql
-- One-step rename breaks all queries using old name
ALTER TABLE users RENAME COLUMN name TO full_name;
```

**✅ SAFE (four-step process)**:

**Step 1: Add new column**
```sql
BEGIN;
ALTER TABLE users ADD COLUMN full_name VARCHAR(255);
COMMIT;
```

**Step 2: Dual-write in application code**
```python
# Update application to write to both columns
user.name = "John Doe"
user.full_name = "John Doe"  # Also write to new column
user.save()
```

**Step 3: Backfill data**
```sql
-- Batch update
UPDATE users
SET full_name = name
WHERE full_name IS NULL
  AND id IN (SELECT id FROM users WHERE full_name IS NULL LIMIT 10000);
```

**Step 4: Deploy application to use new column**
```python
# Application now reads from full_name
user = User.query.get(123)
print(user.full_name)  # Use new column
```

**Step 5: Drop old column** (after confirming new column works)
```sql
BEGIN;
ALTER TABLE users DROP COLUMN name;
COMMIT;
```

### Pattern 4: Changing Column Type

**❌ DANGEROUS (may lock table for hours)**:
```sql
-- Direct type change can rewrite entire table
ALTER TABLE users ALTER COLUMN age TYPE BIGINT;
```

**✅ SAFE (PostgreSQL - compatible type changes)**:
```sql
-- These are fast (metadata-only changes):

-- VARCHAR to larger VARCHAR
ALTER TABLE users ALTER COLUMN name TYPE VARCHAR(500);  -- Fast if no check needed

-- NUMERIC to larger precision
ALTER TABLE products ALTER COLUMN price TYPE NUMERIC(12, 2);  -- From NUMERIC(10, 2)

-- Integer to larger integer (PostgreSQL 12+)
ALTER TABLE users ALTER COLUMN age TYPE BIGINT;  -- Fast in PG 12+ if values fit
```

**✅ SAFE (incompatible type changes - multi-step)**:

**Step 1: Add new column**
```sql
ALTER TABLE users ADD COLUMN age_bigint BIGINT;
```

**Step 2: Dual-write in application**
```python
user.age = 25  # Old column
user.age_bigint = 25  # New column
```

**Step 3: Backfill**
```sql
UPDATE users SET age_bigint = age::BIGINT WHERE age_bigint IS NULL;
```

**Step 4: Swap columns**
```sql
BEGIN;
ALTER TABLE users DROP COLUMN age;
ALTER TABLE users RENAME COLUMN age_bigint TO age;
COMMIT;
```

### Pattern 5: Adding Foreign Key

**❌ DANGEROUS (locks both tables)**:
```sql
-- Immediately validates all existing rows (long lock)
ALTER TABLE orders
ADD CONSTRAINT fk_orders_customer
FOREIGN KEY (customer_id) REFERENCES customers(id);
```

**✅ SAFE (PostgreSQL - two-step process)**:

**Step 1: Add constraint as NOT VALID**
```sql
-- Does NOT validate existing rows (no lock)
BEGIN;

ALTER TABLE orders
ADD CONSTRAINT fk_orders_customer
FOREIGN KEY (customer_id)
REFERENCES customers(id)
NOT VALID;  -- Key: don't validate existing rows

COMMIT;
```

**Step 2: Validate constraint** (run during low traffic)
```sql
-- Validates existing rows (brief lock, can run concurrently with queries)
ALTER TABLE orders
VALIDATE CONSTRAINT fk_orders_customer;
```

**Pre-check** (run before adding FK):
```sql
-- Find orphaned rows that would violate FK
SELECT COUNT(*)
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.id
WHERE c.id IS NULL AND o.customer_id IS NOT NULL;
```

### Pattern 6: Dropping a Column

**❌ DANGEROUS (immediate removal)**:
```sql
-- Breaks application code immediately
ALTER TABLE users DROP COLUMN deprecated_field;
```

**✅ SAFE (three-step process)**:

**Step 1: Stop using column in application code**
```python
# Remove all references to deprecated_field
# Deploy application
```

**Step 2: Wait for rollback safety period** (24-48 hours)
```
# Ensure no need to rollback to code using the column
```

**Step 3: Drop column** (during maintenance window)
```sql
BEGIN;
ALTER TABLE users DROP COLUMN deprecated_field;
COMMIT;
```

## Migration File Structure

### Naming Convention

**Format**: `YYYYMMDDHHMMSS_descriptive_name.{sql|py}`

**Examples**:
- `20250120143000_create_users_table.sql`
- `20250120143100_add_email_index_to_users.sql`
- `20250120143200_add_status_column_to_orders.sql`

### File Template

```sql
-- Migration: 20250120143200_add_status_column_to_orders.sql
-- Description: Add status tracking to orders table
-- Author: migration-manager agent
-- Date: 2025-01-20
-- Estimated time: < 1 second (adding nullable column)
-- Rollback safe: YES
-- Dependencies: None

-- =============================================================================
-- PRE-FLIGHT CHECKS
-- =============================================================================

-- Verify column doesn't already exist
DO $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name = 'orders' AND column_name = 'status'
    ) THEN
        RAISE EXCEPTION 'Column status already exists on orders table';
    END IF;
END $$;

-- =============================================================================
-- UP MIGRATION
-- =============================================================================

BEGIN;

-- Add status column
ALTER TABLE orders
ADD COLUMN status VARCHAR(50);

-- Set default for new rows
ALTER TABLE orders
ALTER COLUMN status SET DEFAULT 'pending';

-- Add index
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_orders_status ON orders(status);

-- Add check constraint
ALTER TABLE orders
ADD CONSTRAINT ck_orders_status_valid
CHECK (status IN ('pending', 'processing', 'completed', 'cancelled'));

COMMIT;

-- =============================================================================
-- VERIFICATION
-- =============================================================================

-- Verify column exists
SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'orders' AND column_name = 'status';

-- Verify index exists
SELECT indexname FROM pg_indexes
WHERE tablename = 'orders' AND indexname = 'idx_orders_status';

-- =============================================================================
-- ROLLBACK (create separate down migration file)
-- =============================================================================

-- File: 20250120143200_add_status_column_to_orders_down.sql
-- BEGIN;
-- ALTER TABLE orders DROP CONSTRAINT IF EXISTS ck_orders_status_valid;
-- DROP INDEX CONCURRENTLY IF EXISTS idx_orders_status;
-- ALTER TABLE orders DROP COLUMN IF EXISTS status;
-- COMMIT;
```

## Batching Large Updates

**Problem**: Large UPDATE/DELETE locks table for long time

**Solution**: Batch into smaller transactions

```sql
-- Bad: Updates 1 million rows in single transaction (locks for minutes)
UPDATE orders SET status = 'archived' WHERE created_at < '2020-01-01';

-- Good: Batch updates (brief locks, can be interrupted)
DO $$
DECLARE
    batch_size INT := 10000;
    updated INT;
    total_updated INT := 0;
BEGIN
    LOOP
        -- Update batch
        UPDATE orders
        SET status = 'archived'
        WHERE created_at < '2020-01-01'
          AND status != 'archived'  -- Skip already updated
          AND id IN (
              SELECT id FROM orders
              WHERE created_at < '2020-01-01'
                AND status != 'archived'
              LIMIT batch_size
          );

        GET DIAGNOSTICS updated = ROW_COUNT;
        total_updated := total_updated + updated;

        -- Log progress
        RAISE NOTICE 'Updated % rows (total: %)', updated, total_updated;

        EXIT WHEN updated = 0;

        -- Brief pause between batches (allow other queries)
        PERFORM pg_sleep(0.1);
    END LOOP;

    RAISE NOTICE 'Migration complete. Total rows updated: %', total_updated;
END $$;
```

## Framework-Specific Patterns

### Alembic (Python/SQLAlchemy)

```python
"""add status column to orders

Revision ID: abc123
Revises: xyz789
Create Date: 2025-01-20 14:32:00
"""
from alembic import op
import sqlalchemy as sa

revision = 'abc123'
down_revision = 'xyz789'

def upgrade():
    # Add column
    op.add_column('orders',
        sa.Column('status', sa.String(50), nullable=True, server_default='pending')
    )

    # Create index (use raw SQL for CONCURRENTLY)
    op.execute('CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_orders_status ON orders(status)')

    # Add check constraint
    op.create_check_constraint(
        'ck_orders_status_valid',
        'orders',
        "status IN ('pending', 'processing', 'completed', 'cancelled')"
    )

def downgrade():
    op.drop_constraint('ck_orders_status_valid', 'orders')
    op.execute('DROP INDEX CONCURRENTLY IF EXISTS idx_orders_status')
    op.drop_column('orders', 'status')
```

### Liquibase (Java)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog>
    <changeSet id="20250120-add-status-column" author="migration-manager">
        <addColumn tableName="orders">
            <column name="status" type="varchar(50)" defaultValue="pending">
                <constraints nullable="true"/>
            </column>
        </addColumn>

        <createIndex indexName="idx_orders_status" tableName="orders">
            <column name="status"/>
        </createIndex>

        <sql>
            ALTER TABLE orders
            ADD CONSTRAINT ck_orders_status_valid
            CHECK (status IN ('pending', 'processing', 'completed', 'cancelled'))
        </sql>

        <rollback>
            <sql>ALTER TABLE orders DROP CONSTRAINT ck_orders_status_valid</sql>
            <dropIndex indexName="idx_orders_status" tableName="orders"/>
            <dropColumn tableName="orders" columnName="status"/>
        </rollback>
    </changeSet>
</databaseChangeLog>
```

### Rails (Ruby)

```ruby
class AddStatusToOrders < ActiveRecord::Migration[7.0]
  disable_ddl_transaction!  # Required for CONCURRENTLY

  def up
    add_column :orders, :status, :string, default: 'pending'

    # Add index concurrently
    add_index :orders, :status, algorithm: :concurrently

    # Add check constraint (PostgreSQL)
    execute <<-SQL
      ALTER TABLE orders
      ADD CONSTRAINT ck_orders_status_valid
      CHECK (status IN ('pending', 'processing', 'completed', 'cancelled'))
    SQL
  end

  def down
    execute 'ALTER TABLE orders DROP CONSTRAINT ck_orders_status_valid'
    remove_index :orders, :status, algorithm: :concurrently
    remove_column :orders, :status
  end
end
```

## Rollback Strategies

### Automatic Rollback (Transactions)

```sql
BEGIN;

-- Migration steps
ALTER TABLE orders ADD COLUMN status VARCHAR(50);

-- Verify migration succeeded
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name = 'orders' AND column_name = 'status'
    ) THEN
        RAISE EXCEPTION 'Migration verification failed';
    END IF;
END $$;

COMMIT;  -- Only commits if all steps succeeded
-- If exception raised, entire transaction rolls back automatically
```

### Manual Rollback Script

```sql
-- Migration down: 20250120143200_add_status_column_to_orders_down.sql
-- Rollback for: add_status_column_to_orders

BEGIN;

-- Remove constraint
ALTER TABLE orders DROP CONSTRAINT IF EXISTS ck_orders_status_valid;

-- Drop index (use CONCURRENTLY to avoid locks)
DROP INDEX CONCURRENTLY IF EXISTS idx_orders_status;

-- Drop column
ALTER TABLE orders DROP COLUMN IF EXISTS status;

-- Verify rollback
DO $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name = 'orders' AND column_name = 'status'
    ) THEN
        RAISE EXCEPTION 'Rollback verification failed: column still exists';
    END IF;
END $$;

COMMIT;
```

## Migration Testing

### Test Checklist

**Before Production**:
- [ ] Run migration on copy of production data
- [ ] Verify migration completes in acceptable time
- [ ] Test rollback procedure
- [ ] Verify application works with migrated schema
- [ ] Check for lock conflicts
- [ ] Review execution plan (EXPLAIN)

### Test Script Template

```bash
#!/bin/bash
# test-migration.sh

set -e  # Exit on error

MIGRATION_FILE="$1"
TEST_DB="migration_test_$(date +%s)"

echo "Creating test database: $TEST_DB"
createdb $TEST_DB

echo "Restoring production snapshot..."
pg_restore --dbname=$TEST_DB /backups/production_snapshot.dump

echo "Running migration..."
time psql $TEST_DB -f "$MIGRATION_FILE"

echo "Verifying migration..."
psql $TEST_DB -c "\d orders"  # Show table structure

echo "Testing rollback..."
time psql $TEST_DB -f "${MIGRATION_FILE%.*}_down.sql"

echo "Cleanup"
dropdb $TEST_DB

echo "✅ Migration test passed"
```

## Common Migration Mistakes

### Mistake 1: Not Using Transactions

**❌ Bad**:
```sql
ALTER TABLE orders ADD COLUMN status VARCHAR(50);
ALTER TABLE orders ADD COLUMN priority INT;  -- If this fails, first statement already committed!
```

**✅ Good**:
```sql
BEGIN;
ALTER TABLE orders ADD COLUMN status VARCHAR(50);
ALTER TABLE orders ADD COLUMN priority INT;
COMMIT;  -- Both succeed or both rollback
```

### Mistake 2: Creating Indexes Without CONCURRENTLY

**❌ Bad** (locks table for entire index build):
```sql
CREATE INDEX idx_orders_status ON orders(status);  -- Locks table during build
```

**✅ Good**:
```sql
CREATE INDEX CONCURRENTLY idx_orders_status ON orders(status);  -- Allows queries during build
```

### Mistake 3: Adding NOT NULL Without Default

**❌ Bad** (fails if table has rows):
```sql
ALTER TABLE orders ADD COLUMN status VARCHAR(50) NOT NULL;  -- Error: null value in column "status"
```

**✅ Good**:
```sql
-- Step 1: Add as nullable with default
ALTER TABLE orders ADD COLUMN status VARCHAR(50) DEFAULT 'pending';

-- Step 2: Backfill existing rows
UPDATE orders SET status = 'pending' WHERE status IS NULL;

-- Step 3: Add NOT NULL
ALTER TABLE orders ALTER COLUMN status SET NOT NULL;
```

## Quality Checklist

**Before Running Migration**:
- [ ] Migration tested on production-like data
- [ ] Estimated execution time < 1 minute (or scheduled maintenance)
- [ ] Rollback script created and tested
- [ ] No data loss possible
- [ ] Compatible with current application code
- [ ] Uses transactions where possible
- [ ] Uses CONCURRENTLY for indexes
- [ ] Large updates are batched
- [ ] Pre-flight checks included

**After Running Migration**:
- [ ] Verify migration succeeded (query new structures)
- [ ] Application still works
- [ ] No performance degradation
- [ ] Rollback script works (test on copy)
- [ ] Documentation updated
- [ ] Team notified

This skill represents industry best practices for database migration management.
