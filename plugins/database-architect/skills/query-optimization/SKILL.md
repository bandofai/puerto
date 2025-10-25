# Query Optimization Skill

Expert patterns for analyzing, optimizing, and troubleshooting database query performance.

## Core Principles

### 1. Query Execution Process

**PostgreSQL Query Execution**:
1. **Parser**: Validates syntax
2. **Planner**: Analyzes statistics, estimates costs, chooses plan
3. **Executor**: Runs the plan
4. **Returns**: Results to client

**Key Insight**: Planner decisions are based on statistics. Outdated statistics → bad plans.

### 2. Reading Execution Plans

**PostgreSQL EXPLAIN Output**:

```sql
EXPLAIN (ANALYZE, BUFFERS, VERBOSE)
SELECT o.id, c.name
FROM orders o
JOIN customers c ON c.id = o.customer_id
WHERE o.status = 'pending'
ORDER BY o.created_at DESC
LIMIT 100;
```

**Sample Output**:
```
Limit  (cost=0.42..123.45 rows=100 width=48) (actual time=0.12..5.67 rows=100 loops=1)
  Buffers: shared hit=245
  ->  Nested Loop  (cost=0.42..12345.67 rows=10000 width=48) (actual time=0.12..5.65 rows=100 loops=1)
        Buffers: shared hit=245
        ->  Index Scan using idx_orders_status_created on orders o
              (cost=0.42..5678.90 rows=10000 width=24) (actual time=0.11..2.34 rows=100 loops=1)
              Index Cond: (status = 'pending')
              Buffers: shared hit=145
        ->  Index Scan using customers_pkey on customers c
              (cost=0.42..0.67 rows=1 width=24) (actual time=0.03..0.03 rows=1 loops=100)
              Index Cond: (id = o.customer_id)
              Buffers: shared hit=100
Planning Time: 1.23 ms
Execution Time: 5.78 ms
```

**Key Metrics**:
- **cost**: Estimated query cost (arbitrary units, lower is better)
  - First number: Startup cost (before first row)
  - Second number: Total cost (all rows)
- **rows**: Estimated number of rows
- **actual time**: Real execution time (ms)
- **actual rows**: Actual number of rows returned
- **loops**: Number of times this node was executed
- **Buffers**: Memory/disk I/O
  - **shared hit**: Found in cache (fast)
  - **shared read**: Read from disk (slow)

**Red Flags**:
- `Seq Scan` on tables with >10k rows
- `actual rows >> rows` (statistics need updating)
- `actual time >> cost` (query needs tuning)
- High `shared read` values (disk I/O bottleneck)
- `Nested Loop` with high loops count

### 3. Join Algorithms

**Nested Loop**:
- Best for: Small datasets, good indexes
- How it works: For each row in outer table, scan inner table
- Cost: O(n × m)

```
Nested Loop
  ->  Seq Scan on orders (10 rows)
  ->  Index Scan on customers (loops=10)
```

**Hash Join**:
- Best for: Medium to large datasets, no suitable indexes
- How it works: Build hash table from smaller table, probe with larger
- Cost: O(n + m)

```
Hash Join
  Hash Cond: (o.customer_id = c.id)
  ->  Seq Scan on orders
  ->  Hash
        ->  Seq Scan on customers
```

**Merge Join**:
- Best for: Large pre-sorted datasets
- How it works: Merge two sorted inputs
- Cost: O(n + m) if already sorted, O(n log n + m log m) if sorting needed

```
Merge Join
  Merge Cond: (o.customer_id = c.id)
  ->  Index Scan on orders (sorted by customer_id)
  ->  Index Scan on customers (sorted by id)
```

## Indexing Strategies

### Index Selection Rules

**1. Index WHERE Clause Columns**:
```sql
-- Query
SELECT * FROM orders WHERE status = 'pending' AND created_at > NOW() - INTERVAL '7 days';

-- Index (composite)
CREATE INDEX idx_orders_status_created ON orders(status, created_at);
```

**2. Index Foreign Keys** (always):
```sql
-- Query
SELECT * FROM orders o JOIN customers c ON c.id = o.customer_id;

-- Index
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
```

**3. Index ORDER BY Columns**:
```sql
-- Query
SELECT * FROM orders WHERE status = 'pending' ORDER BY created_at DESC LIMIT 100;

-- Index (with DESC)
CREATE INDEX idx_orders_status_created ON orders(status, created_at DESC);
```

**4. Covering Indexes (Include Columns)**:
```sql
-- Query
SELECT id, total, status FROM orders WHERE customer_id = '...';

-- Covering index (PostgreSQL 11+)
CREATE INDEX idx_orders_customer_covering
ON orders(customer_id) INCLUDE (total, status);

-- No need to access table (index-only scan)
```

### Composite Index Column Order

**Rule of Thumb**: Most selective column first, or most commonly filtered

```sql
-- Good: status filtered first, then sorted by created_at
CREATE INDEX idx_orders_status_created ON orders(status, created_at DESC);

-- Works efficiently for:
WHERE status = 'pending'  ✅
WHERE status = 'pending' AND created_at > '2025-01-01'  ✅
WHERE status = 'pending' ORDER BY created_at DESC  ✅

-- Does NOT use index efficiently:
WHERE created_at > '2025-01-01'  ❌ (skips first column)
```

**Exception**: Equality first, then range

```sql
-- Optimal order
CREATE INDEX idx_orders_status_created_total
ON orders(status, created_at, total);

-- Works for:
WHERE status = 'pending' AND created_at > '2025-01-01' AND total > 100  ✅
WHERE status = 'pending' AND created_at > '2025-01-01'  ✅
WHERE status = 'pending'  ✅
```

### Partial Indexes

**Use when filtering a subset**:

```sql
-- Only index pending orders
CREATE INDEX idx_orders_pending
ON orders(created_at DESC)
WHERE status = 'pending';

-- Smaller index, faster updates, same query performance for pending orders
```

### Expression Indexes

**Use for computed values**:

```sql
-- Case-insensitive search
CREATE INDEX idx_users_email_lower ON users(LOWER(email));

-- Query must match expression
SELECT * FROM users WHERE LOWER(email) = 'user@example.com';
```

## Common Query Patterns and Optimizations

### Pattern 1: N+1 Queries

**❌ Problem**:
```python
# ORM code that generates N+1 queries
orders = Order.all()  # 1 query
for order in orders:
    print(order.customer.name)  # N queries (one per order)
```

**✅ Solution**:
```python
# Eager loading with JOIN
orders = Order.select_related('customer').all()  # 1 query with JOIN
for order in orders:
    print(order.customer.name)  # No additional query
```

**SQL**:
```sql
-- Bad: Application makes N+1 queries
SELECT * FROM orders;  -- Returns 100 rows
SELECT * FROM customers WHERE id = 1;
SELECT * FROM customers WHERE id = 2;
-- ... 98 more queries

-- Good: Single JOIN
SELECT o.*, c.name
FROM orders o
JOIN customers c ON c.id = o.customer_id;
```

### Pattern 2: SELECT *

**❌ Problem**:
```sql
-- Fetches unnecessary columns
SELECT * FROM products WHERE category = 'electronics';
```

**✅ Solution**:
```sql
-- Only needed columns
SELECT id, name, price FROM products WHERE category = 'electronics';

-- Benefits:
-- - Less data transferred
-- - Can use covering indexes
-- - Better for network/memory
```

### Pattern 3: Functions on Indexed Columns

**❌ Problem**:
```sql
-- Function prevents index use
SELECT * FROM users WHERE YEAR(created_at) = 2025;
```

**✅ Solution**:
```sql
-- Rewrite to use range
SELECT * FROM users
WHERE created_at >= '2025-01-01'
  AND created_at < '2026-01-01';

-- Can use index on created_at
```

### Pattern 4: OR Conditions

**❌ Problem**:
```sql
-- OR can prevent index use
SELECT * FROM orders
WHERE status = 'pending' OR status = 'processing';
```

**✅ Solution**:
```sql
-- Use IN (can use index)
SELECT * FROM orders
WHERE status IN ('pending', 'processing');

-- Or UNION for complex cases
SELECT * FROM orders WHERE status = 'pending'
UNION ALL
SELECT * FROM orders WHERE status = 'processing';
```

### Pattern 5: Subqueries vs JOINs

**❌ Slow** (correlated subquery):
```sql
SELECT *
FROM orders o
WHERE total > (
    SELECT AVG(total)
    FROM orders
    WHERE customer_id = o.customer_id  -- Runs for EACH order
);
```

**✅ Fast** (JOIN):
```sql
SELECT o.*
FROM orders o
JOIN (
    SELECT customer_id, AVG(total) as avg_total
    FROM orders
    GROUP BY customer_id
) avg_orders ON o.customer_id = avg_orders.customer_id
WHERE o.total > avg_orders.avg_total;
```

### Pattern 6: Counting Large Tables

**❌ Slow**:
```sql
-- Full table scan
SELECT COUNT(*) FROM orders;
```

**✅ Fast** (approximate):
```sql
-- PostgreSQL: Use statistics (instant)
SELECT reltuples::bigint AS estimate
FROM pg_class
WHERE relname = 'orders';

-- MySQL: Use information schema
SELECT table_rows
FROM information_schema.tables
WHERE table_name = 'orders';
```

## Advanced Optimization Techniques

### 1. Materialized Views

**Use case**: Complex aggregations queried frequently

```sql
-- Create materialized view
CREATE MATERIALIZED VIEW daily_sales AS
SELECT
    DATE(created_at) as sale_date,
    COUNT(*) as order_count,
    SUM(total) as total_sales,
    AVG(total) as avg_order_value
FROM orders
GROUP BY DATE(created_at);

-- Add index
CREATE INDEX idx_daily_sales_date ON daily_sales(sale_date);

-- Refresh periodically
REFRESH MATERIALIZED VIEW CONCURRENTLY daily_sales;

-- Query is now instant
SELECT * FROM daily_sales WHERE sale_date = '2025-01-20';
```

### 2. Partitioning

**Use case**: Very large tables (>10M rows), time-series data

```sql
-- Create partitioned table (PostgreSQL)
CREATE TABLE events (
    id UUID,
    event_type VARCHAR(50),
    data JSONB,
    created_at TIMESTAMP
) PARTITION BY RANGE (created_at);

-- Create partitions
CREATE TABLE events_2024_q1 PARTITION OF events
FOR VALUES FROM ('2024-01-01') TO ('2024-04-01');

CREATE TABLE events_2024_q2 PARTITION OF events
FOR VALUES FROM ('2024-04-01') TO ('2024-07-01');

-- Queries automatically use partition pruning
SELECT * FROM events WHERE created_at >= '2024-03-01' AND created_at < '2024-04-01';
-- Only scans events_2024_q1
```

### 3. Query Hints (Use Sparingly)

**PostgreSQL** (via comments):
```sql
-- Force index usage (not standard, database-specific)
/*+ IndexScan(orders idx_orders_status) */
SELECT * FROM orders WHERE status = 'pending';
```

**MySQL**:
```sql
-- Force index
SELECT * FROM orders FORCE INDEX (idx_orders_status) WHERE status = 'pending';

-- Ignore index
SELECT * FROM orders IGNORE INDEX (idx_orders_email) WHERE email = 'user@example.com';
```

**Warning**: Hints override planner. Only use when you've proven the planner is wrong.

### 4. Connection Pooling

**Why**: Creating connections is expensive (100-200ms each)

```python
# Bad: New connection per query
import psycopg2
for i in range(100):
    conn = psycopg2.connect(...)  # 100-200ms each = 10-20 seconds total!
    cursor = conn.cursor()
    cursor.execute("SELECT ...")
    conn.close()

# Good: Connection pool
from psycopg2 import pool
connection_pool = pool.SimpleConnectionPool(5, 20, ...)

for i in range(100):
    conn = connection_pool.getconn()  # <1ms from pool
    cursor = conn.cursor()
    cursor.execute("SELECT ...")
    connection_pool.putconn(conn)
```

### 5. Batch Operations

**Inserts**:
```sql
-- Bad: 1000 individual INSERTs
INSERT INTO users (name, email) VALUES ('User 1', 'user1@example.com');
INSERT INTO users (name, email) VALUES ('User 2', 'user2@example.com');
-- ... 998 more

-- Good: Bulk INSERT
INSERT INTO users (name, email) VALUES
    ('User 1', 'user1@example.com'),
    ('User 2', 'user2@example.com'),
    ...
    ('User 1000', 'user1000@example.com');

-- Or COPY (PostgreSQL) - fastest
COPY users (name, email) FROM '/path/to/data.csv' WITH CSV;
```

## Monitoring and Diagnostics

### Slow Query Log

**PostgreSQL**:
```sql
-- Enable slow query log
ALTER SYSTEM SET log_min_duration_statement = 100;  -- Log queries >100ms
SELECT pg_reload_conf();

-- View current queries
SELECT
    pid,
    now() - query_start as duration,
    query
FROM pg_stat_activity
WHERE state = 'active'
ORDER BY duration DESC;

-- Kill slow query
SELECT pg_terminate_backend(pid);
```

**MySQL**:
```sql
-- Enable slow query log
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 0.1;  -- 100ms

-- View current queries
SHOW FULL PROCESSLIST;

-- Kill query
KILL QUERY 12345;
```

### Index Usage Statistics

**PostgreSQL**:
```sql
-- Find unused indexes
SELECT
    schemaname,
    tablename,
    indexname,
    idx_scan,
    idx_tup_read,
    idx_tup_fetch,
    pg_size_pretty(pg_relation_size(indexrelid)) as size
FROM pg_stat_user_indexes
WHERE idx_scan = 0  -- Never used
  AND schemaname = 'public'
ORDER BY pg_relation_size(indexrelid) DESC;

-- Find indexes on most scanned tables
SELECT
    schemaname,
    tablename,
    indexname,
    idx_scan,
    pg_size_pretty(pg_relation_size(indexrelid)) as size
FROM pg_stat_user_indexes
WHERE schemaname = 'public'
ORDER BY idx_scan DESC
LIMIT 20;
```

### Statistics Maintenance

**PostgreSQL**:
```sql
-- Update statistics (important!)
ANALYZE orders;  -- Specific table
ANALYZE;  -- All tables

-- Vacuum to reclaim space
VACUUM orders;  -- Specific table
VACUUM;  -- All tables

-- Full vacuum (locks table, use during maintenance)
VACUUM FULL orders;

-- Autovacuum settings
ALTER TABLE orders SET (autovacuum_vacuum_scale_factor = 0.05);  -- More aggressive
```

**MySQL**:
```sql
-- Update statistics
ANALYZE TABLE orders;

-- Optimize table (rebuilds indexes, reclaims space)
OPTIMIZE TABLE orders;
```

## Performance Tuning Checklist

**Query Level**:
- [ ] Avoid SELECT *
- [ ] Use appropriate indexes
- [ ] Use LIMIT for pagination
- [ ] Avoid functions on indexed columns
- [ ] Use prepared statements
- [ ] Batch operations (avoid N+1)

**Index Level**:
- [ ] Indexes on foreign keys
- [ ] Composite indexes for multi-column queries
- [ ] Covering indexes for frequent queries
- [ ] Partial indexes for filtered queries
- [ ] Remove unused indexes

**Schema Level**:
- [ ] Normalize to reduce redundancy
- [ ] Strategic denormalization for performance
- [ ] Partitioning for very large tables
- [ ] Materialized views for aggregations

**Database Level**:
- [ ] Vacuum/analyze regularly
- [ ] Statistics up-to-date
- [ ] Connection pooling configured
- [ ] Appropriate shared_buffers
- [ ] Appropriate work_mem
- [ ] Slow query log enabled

## Common Mistakes to Avoid

**❌ Premature Optimization**:
- Don't add indexes blindly
- Measure first, then optimize
- Each index slows writes

**❌ Over-Indexing**:
- Too many indexes slow INSERT/UPDATE/DELETE
- Remove unused indexes
- Combine into composite indexes

**❌ Ignoring Statistics**:
- Outdated statistics → bad query plans
- Run ANALYZE regularly
- Especially after large data changes

**❌ Not Using EXPLAIN**:
- Always check execution plan
- Before and after optimization
- Compare actual vs estimated rows

This skill represents industry best practices for database query optimization.
