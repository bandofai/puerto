-- Migration: YYYYMMDDHHMMSS_descriptive_name.sql
-- Description: [What this migration does and why]
-- Author: [Your name or migration-manager agent]
-- Date: YYYY-MM-DD
-- Estimated time: [< 1s / ~5s / ~30s / >1min]
-- Rollback safe: [YES / NO / PARTIAL]
-- Dependencies: [List any required prior migrations]

-- =============================================================================
-- PRE-FLIGHT CHECKS
-- =============================================================================

-- Example: Verify table exists
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.tables
        WHERE table_name = 'users'
    ) THEN
        RAISE EXCEPTION 'Table users does not exist. Run prerequisite migration first.';
    END IF;
END $$;

-- Example: Verify column doesn't already exist
DO $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name = 'users' AND column_name = 'new_column'
    ) THEN
        RAISE EXCEPTION 'Column new_column already exists on users table';
    END IF;
END $$;

-- Example: Check for data that would violate new constraints
DO $$
DECLARE
    violation_count INT;
BEGIN
    SELECT COUNT(*) INTO violation_count
    FROM users
    WHERE email IS NULL;

    IF violation_count > 0 THEN
        RAISE EXCEPTION '% rows have NULL email, cannot add NOT NULL constraint', violation_count;
    END IF;
END $$;

-- =============================================================================
-- UP MIGRATION
-- =============================================================================

BEGIN;

-- Add new column (nullable initially)
ALTER TABLE users
ADD COLUMN status VARCHAR(50);

-- Set default for new rows
ALTER TABLE users
ALTER COLUMN status SET DEFAULT 'active';

-- Add check constraint
ALTER TABLE users
ADD CONSTRAINT ck_users_status_valid
CHECK (status IN ('active', 'inactive', 'suspended'));

COMMIT;

-- Create index CONCURRENTLY (must be outside transaction)
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_users_status
ON users(status);

-- =============================================================================
-- BACKFILL (if needed for existing rows)
-- =============================================================================

-- Batch updates to avoid long locks
DO $$
DECLARE
    batch_size INT := 10000;
    updated INT;
    total_updated INT := 0;
BEGIN
    LOOP
        UPDATE users
        SET status = 'active'
        WHERE status IS NULL
          AND id IN (
              SELECT id FROM users
              WHERE status IS NULL
              LIMIT batch_size
          );

        GET DIAGNOSTICS updated = ROW_COUNT;
        total_updated := total_updated + updated;

        RAISE NOTICE 'Updated % rows (total: %)', updated, total_updated;

        EXIT WHEN updated = 0;

        -- Brief pause between batches
        PERFORM pg_sleep(0.1);
    END LOOP;

    RAISE NOTICE 'Backfill complete. Total rows updated: %', total_updated;
END $$;

-- =============================================================================
-- POST-MIGRATION STEPS (if needed)
-- =============================================================================

-- Example: Add NOT NULL after backfill
-- BEGIN;
-- ALTER TABLE users ALTER COLUMN status SET NOT NULL;
-- COMMIT;

-- =============================================================================
-- VERIFICATION
-- =============================================================================

-- Verify column exists with correct type
SELECT
    column_name,
    data_type,
    is_nullable,
    column_default
FROM information_schema.columns
WHERE table_name = 'users' AND column_name = 'status';

-- Verify index exists
SELECT
    schemaname,
    tablename,
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename = 'users' AND indexname = 'idx_users_status';

-- Verify constraint exists
SELECT
    conname,
    contype,
    pg_get_constraintdef(oid)
FROM pg_constraint
WHERE conrelid = 'users'::regclass
  AND conname = 'ck_users_status_valid';

-- Verify data looks correct
SELECT status, COUNT(*) as count
FROM users
GROUP BY status
ORDER BY count DESC;

-- =============================================================================
-- ROLLBACK (create separate down migration file)
-- =============================================================================

-- File: YYYYMMDDHHMMSS_descriptive_name_down.sql

-- BEGIN;
--
-- -- Remove check constraint
-- ALTER TABLE users DROP CONSTRAINT IF EXISTS ck_users_status_valid;
--
-- COMMIT;
--
-- -- Drop index concurrently
-- DROP INDEX CONCURRENTLY IF EXISTS idx_users_status;
--
-- BEGIN;
--
-- -- Drop column
-- ALTER TABLE users DROP COLUMN IF EXISTS status;
--
-- COMMIT;

-- =============================================================================
-- NOTES
-- =============================================================================

-- [Any important notes about this migration]
-- - Remember to update application code before deploying
-- - Monitor performance after deployment
-- - Consider adding this index: ...
