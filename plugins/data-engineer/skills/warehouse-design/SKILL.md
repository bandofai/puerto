# Warehouse Design Skill

This skill provides comprehensive patterns for dimensional modeling, star/snowflake schemas, and data warehouse architecture.

## Dimensional Modeling Fundamentals

### Star Schema vs Snowflake Schema

**Star Schema**: Denormalized dimensions connected directly to fact table
- Simpler queries (fewer joins)
- Better query performance
- More data redundancy
- Easier to understand

**Snowflake Schema**: Normalized dimensions with sub-dimensions
- Reduced data redundancy
- More complex queries (more joins)
- Easier to maintain dimensional attributes
- Better for very large dimensions

## Fact Table Patterns

### 1. Transaction Fact Table
Records individual business events at the most atomic level.

```sql
-- One row per order line item
CREATE TABLE fact_sales (
    -- Surrogate key
    sales_key BIGINT PRIMARY KEY,

    -- Foreign keys to dimensions
    date_key INT NOT NULL,
    customer_key INT NOT NULL,
    product_key INT NOT NULL,
    store_key INT NOT NULL,
    promotion_key INT,

    -- Degenerate dimensions (transaction identifiers)
    order_id VARCHAR(50) NOT NULL,
    line_number INT NOT NULL,

    -- Additive measures (can be summed)
    quantity_sold DECIMAL(10,2) NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    discount_amount DECIMAL(10,2) DEFAULT 0,
    tax_amount DECIMAL(10,2) NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,

    -- Non-additive measures (can't be summed)
    unit_cost DECIMAL(10,2),
    profit_margin DECIMAL(5,2),  -- Percentage

    -- Metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Foreign key constraints
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key),
    FOREIGN KEY (product_key) REFERENCES dim_product(product_key),
    FOREIGN KEY (store_key) REFERENCES dim_store(store_key),
    FOREIGN KEY (promotion_key) REFERENCES dim_promotion(promotion_key)
);

-- Indexes for query performance
CREATE INDEX idx_fact_sales_date ON fact_sales(date_key);
CREATE INDEX idx_fact_sales_customer ON fact_sales(customer_key);
CREATE INDEX idx_fact_sales_product ON fact_sales(product_key);
CREATE INDEX idx_fact_sales_order ON fact_sales(order_id);
```

### 2. Periodic Snapshot Fact Table
Records the state of measurements at regular intervals.

```sql
-- Daily inventory snapshot
CREATE TABLE fact_inventory_snapshot (
    snapshot_key BIGINT PRIMARY KEY,

    -- Time dimension (daily snapshot)
    date_key INT NOT NULL,

    -- Dimensions
    product_key INT NOT NULL,
    warehouse_key INT NOT NULL,

    -- Semi-additive measures (can be summed across dimensions but not time)
    quantity_on_hand INT NOT NULL,
    quantity_allocated INT NOT NULL,
    quantity_available INT NOT NULL,

    -- Additive measures
    units_received_today INT DEFAULT 0,
    units_shipped_today INT DEFAULT 0,

    -- Non-additive measures
    unit_cost DECIMAL(10,2),
    inventory_value DECIMAL(12,2),  -- quantity * cost

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (product_key) REFERENCES dim_product(product_key),
    FOREIGN KEY (warehouse_key) REFERENCES dim_warehouse(warehouse_key),

    -- Unique constraint to prevent duplicate snapshots
    UNIQUE(date_key, product_key, warehouse_key)
);
```

### 3. Accumulating Snapshot Fact Table
Records the complete lifecycle of a process with multiple milestones.

```sql
-- Order fulfillment lifecycle
CREATE TABLE fact_order_fulfillment (
    fulfillment_key BIGINT PRIMARY KEY,

    -- Multiple date dimensions for milestones
    order_date_key INT NOT NULL,
    payment_date_key INT,
    shipment_date_key INT,
    delivery_date_key INT,

    -- Other dimensions
    customer_key INT NOT NULL,
    product_key INT NOT NULL,

    -- Degenerate dimension
    order_id VARCHAR(50) NOT NULL,

    -- Measures
    order_amount DECIMAL(10,2) NOT NULL,
    shipping_cost DECIMAL(10,2),

    -- Lag measures (days between milestones)
    days_to_payment INT,
    days_to_shipment INT,
    days_to_delivery INT,

    -- Status
    current_status VARCHAR(50),
    is_completed BOOLEAN DEFAULT FALSE,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (order_date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (payment_date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (shipment_date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (delivery_date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key),
    FOREIGN KEY (product_key) REFERENCES dim_product(product_key)
);
```

### 4. Factless Fact Table
Records events without measures (captures relationships).

```sql
-- Student course attendance (event tracking)
CREATE TABLE fact_student_attendance (
    attendance_key BIGINT PRIMARY KEY,

    -- Dimensions
    date_key INT NOT NULL,
    student_key INT NOT NULL,
    course_key INT NOT NULL,
    instructor_key INT NOT NULL,

    -- Optional flag
    is_present BOOLEAN NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (student_key) REFERENCES dim_student(student_key),
    FOREIGN KEY (course_key) REFERENCES dim_course(course_key),
    FOREIGN KEY (instructor_key) REFERENCES dim_instructor(instructor_key)
);
```

## Dimension Table Patterns

### 1. Type 0: Retain Original
Never changes - fixed reference data.

```sql
CREATE TABLE dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE NOT NULL,
    day_of_week VARCHAR(10) NOT NULL,
    day_of_month INT NOT NULL,
    day_of_year INT NOT NULL,
    week_of_year INT NOT NULL,
    month_number INT NOT NULL,
    month_name VARCHAR(10) NOT NULL,
    quarter INT NOT NULL,
    year INT NOT NULL,
    is_weekend BOOLEAN NOT NULL,
    is_holiday BOOLEAN NOT NULL,
    holiday_name VARCHAR(100),
    fiscal_year INT,
    fiscal_quarter INT,

    UNIQUE(full_date)
);
```

### 2. Type 1: Overwrite
Updates current record, no history preserved.

```sql
CREATE TABLE dim_product_type1 (
    product_key INT PRIMARY KEY,

    -- Natural key
    product_id VARCHAR(50) NOT NULL UNIQUE,

    -- Attributes (overwritten on change)
    product_name VARCHAR(200) NOT NULL,
    category VARCHAR(100),
    brand VARCHAR(100),
    unit_price DECIMAL(10,2),
    is_active BOOLEAN DEFAULT TRUE,

    -- Metadata
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Update logic (overwrites existing record)
-- UPDATE dim_product_type1
-- SET product_name = 'New Name', updated_at = CURRENT_TIMESTAMP
-- WHERE product_id = 'PROD123';
```

### 3. Type 2: Add New Row
Creates new record for changes, preserves full history (MOST COMMON).

```sql
CREATE TABLE dim_customer (
    customer_key INT PRIMARY KEY,  -- Surrogate key (auto-increment)

    -- Natural key
    customer_id VARCHAR(50) NOT NULL,

    -- Attributes (tracked for changes)
    customer_name VARCHAR(200) NOT NULL,
    email VARCHAR(200),
    phone VARCHAR(20),
    address VARCHAR(500),
    city VARCHAR(100),
    state VARCHAR(50),
    country VARCHAR(50),
    zip_code VARCHAR(20),
    customer_segment VARCHAR(50),

    -- SCD Type 2 tracking columns
    effective_date DATE NOT NULL,
    expiration_date DATE NOT NULL DEFAULT '9999-12-31',
    is_current BOOLEAN NOT NULL DEFAULT TRUE,

    -- Metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for Type 2 queries
CREATE INDEX idx_customer_id_current ON dim_customer(customer_id, is_current);
CREATE INDEX idx_customer_effective ON dim_customer(effective_date);

-- Type 2 insert logic
-- 1. Expire current record
UPDATE dim_customer
SET expiration_date = CURRENT_DATE - 1,
    is_current = FALSE,
    updated_at = CURRENT_TIMESTAMP
WHERE customer_id = 'CUST123' AND is_current = TRUE;

-- 2. Insert new record
INSERT INTO dim_customer (
    customer_id, customer_name, email, address,
    effective_date, expiration_date, is_current
) VALUES (
    'CUST123', 'John Smith', 'john.new@email.com', '456 New St',
    CURRENT_DATE, '9999-12-31', TRUE
);
```

### 4. Type 3: Add New Column
Tracks limited history with additional columns.

```sql
CREATE TABLE dim_product_type3 (
    product_key INT PRIMARY KEY,
    product_id VARCHAR(50) NOT NULL UNIQUE,

    -- Current attributes
    product_name VARCHAR(200) NOT NULL,
    current_category VARCHAR(100),
    current_price DECIMAL(10,2),

    -- Previous values (limited history)
    previous_category VARCHAR(100),
    previous_price DECIMAL(10,2),
    category_change_date DATE,
    price_change_date DATE,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 5. Type 6: Hybrid (Type 1 + 2 + 3)
Combines current and historical tracking.

```sql
CREATE TABLE dim_customer_type6 (
    customer_key INT PRIMARY KEY,
    customer_id VARCHAR(50) NOT NULL,

    -- Historical attributes (Type 2)
    historical_name VARCHAR(200) NOT NULL,
    historical_segment VARCHAR(50),

    -- Current attributes (Type 1) - always updated
    current_name VARCHAR(200) NOT NULL,
    current_segment VARCHAR(50),

    -- Previous values (Type 3)
    previous_segment VARCHAR(50),

    -- SCD Type 2 tracking
    effective_date DATE NOT NULL,
    expiration_date DATE NOT NULL DEFAULT '9999-12-31',
    is_current BOOLEAN NOT NULL DEFAULT TRUE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 6. Junk Dimension
Groups low-cardinality flags and indicators.

```sql
CREATE TABLE dim_transaction_flags (
    transaction_flag_key INT PRIMARY KEY,

    -- Low-cardinality flags (create row for each combination)
    is_online_order BOOLEAN NOT NULL,
    is_gift_wrapped BOOLEAN NOT NULL,
    is_expedited_shipping BOOLEAN NOT NULL,
    payment_method VARCHAR(20) NOT NULL,  -- Cash, Card, PayPal
    shipping_method VARCHAR(20) NOT NULL,  -- Standard, Express, Overnight

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Ensure unique combinations
    UNIQUE(is_online_order, is_gift_wrapped, is_expedited_shipping,
           payment_method, shipping_method)
);

-- Pre-populate with all combinations
-- INSERT INTO dim_transaction_flags (is_online_order, is_gift_wrapped, ...)
-- SELECT t1.val, t2.val, t3.val, ...
-- FROM (VALUES (TRUE), (FALSE)) AS t1(val)
-- CROSS JOIN (VALUES (TRUE), (FALSE)) AS t2(val)
-- ...
```

### 7. Role-Playing Dimension
One dimension used multiple times with different contexts.

```sql
-- Single date dimension
CREATE TABLE dim_date (...);

-- Fact table references it multiple times
CREATE TABLE fact_order (
    order_key BIGINT PRIMARY KEY,

    -- Same dimension, different roles
    order_date_key INT NOT NULL,
    ship_date_key INT NOT NULL,
    delivery_date_key INT NOT NULL,

    ...

    FOREIGN KEY (order_date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (ship_date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (delivery_date_key) REFERENCES dim_date(date_key)
);
```

### 8. Mini-Dimension
Splits frequently changing attributes from large dimension.

```sql
-- Main customer dimension (slowly changing)
CREATE TABLE dim_customer (
    customer_key INT PRIMARY KEY,
    customer_id VARCHAR(50) NOT NULL,
    customer_name VARCHAR(200) NOT NULL,
    email VARCHAR(200),
    -- Stable attributes only
    ...
);

-- Mini-dimension for frequently changing attributes
CREATE TABLE dim_customer_profile (
    profile_key INT PRIMARY KEY,

    -- Demographic bands (change frequently)
    age_range VARCHAR(20),  -- 18-24, 25-34, etc.
    income_range VARCHAR(20),  -- <30K, 30K-50K, etc.
    credit_score_range VARCHAR(20),  -- Poor, Fair, Good, Excellent

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(age_range, income_range, credit_score_range)
);

-- Fact table references both
CREATE TABLE fact_transaction (
    transaction_key BIGINT PRIMARY KEY,
    customer_key INT NOT NULL,
    profile_key INT NOT NULL,  -- Points to mini-dimension
    ...
    FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key),
    FOREIGN KEY (profile_key) REFERENCES dim_customer_profile(profile_key)
);
```

## Complete Star Schema Example

```sql
-- ============================================
-- DIMENSION TABLES
-- ============================================

-- Date Dimension (Type 0)
CREATE TABLE dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE NOT NULL UNIQUE,
    day_of_week VARCHAR(10) NOT NULL,
    day_name VARCHAR(10) NOT NULL,
    day_of_month INT NOT NULL,
    day_of_year INT NOT NULL,
    week_of_year INT NOT NULL,
    month_number INT NOT NULL,
    month_name VARCHAR(10) NOT NULL,
    quarter INT NOT NULL,
    year INT NOT NULL,
    is_weekend BOOLEAN NOT NULL,
    is_holiday BOOLEAN NOT NULL
);

-- Customer Dimension (Type 2)
CREATE TABLE dim_customer (
    customer_key INT PRIMARY KEY,
    customer_id VARCHAR(50) NOT NULL,
    customer_name VARCHAR(200) NOT NULL,
    email VARCHAR(200),
    phone VARCHAR(20),
    city VARCHAR(100),
    state VARCHAR(50),
    country VARCHAR(50),
    customer_segment VARCHAR(50),
    effective_date DATE NOT NULL,
    expiration_date DATE NOT NULL DEFAULT '9999-12-31',
    is_current BOOLEAN NOT NULL DEFAULT TRUE
);

-- Product Dimension (Type 2)
CREATE TABLE dim_product (
    product_key INT PRIMARY KEY,
    product_id VARCHAR(50) NOT NULL,
    product_name VARCHAR(200) NOT NULL,
    product_description TEXT,
    category VARCHAR(100),
    subcategory VARCHAR(100),
    brand VARCHAR(100),
    unit_cost DECIMAL(10,2),
    unit_price DECIMAL(10,2),
    is_active BOOLEAN DEFAULT TRUE,
    effective_date DATE NOT NULL,
    expiration_date DATE NOT NULL DEFAULT '9999-12-31',
    is_current BOOLEAN NOT NULL DEFAULT TRUE
);

-- Store Dimension (Type 1)
CREATE TABLE dim_store (
    store_key INT PRIMARY KEY,
    store_id VARCHAR(50) NOT NULL UNIQUE,
    store_name VARCHAR(200) NOT NULL,
    store_type VARCHAR(50),
    address VARCHAR(500),
    city VARCHAR(100),
    state VARCHAR(50),
    country VARCHAR(50),
    zip_code VARCHAR(20),
    manager_name VARCHAR(200),
    phone VARCHAR(20),
    is_active BOOLEAN DEFAULT TRUE,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- FACT TABLE
-- ============================================

CREATE TABLE fact_sales (
    sales_key BIGINT PRIMARY KEY,

    -- Dimension foreign keys
    date_key INT NOT NULL,
    customer_key INT NOT NULL,
    product_key INT NOT NULL,
    store_key INT NOT NULL,

    -- Degenerate dimensions
    order_id VARCHAR(50) NOT NULL,
    line_number INT NOT NULL,

    -- Measures
    quantity_sold DECIMAL(10,2) NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    discount_amount DECIMAL(10,2) DEFAULT 0,
    tax_amount DECIMAL(10,2) NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    unit_cost DECIMAL(10,2),
    profit_amount DECIMAL(10,2),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Foreign keys
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key),
    FOREIGN KEY (product_key) REFERENCES dim_product(product_key),
    FOREIGN KEY (store_key) REFERENCES dim_store(store_key)
);

-- Performance indexes
CREATE INDEX idx_fact_sales_date ON fact_sales(date_key);
CREATE INDEX idx_fact_sales_customer ON fact_sales(customer_key);
CREATE INDEX idx_fact_sales_product ON fact_sales(product_key);
CREATE INDEX idx_fact_sales_store ON fact_sales(store_key);
CREATE INDEX idx_fact_sales_order ON fact_sales(order_id);
```

## Cloud Warehouse Optimizations

### Snowflake

```sql
-- Clustering for large tables
CREATE TABLE fact_sales (
    ...
) CLUSTER BY (date_key, customer_key);

-- Time travel for historical queries
SELECT * FROM dim_customer
AT(TIMESTAMP => '2024-01-01 00:00:00'::TIMESTAMP);

-- Use VARIANT for semi-structured data
CREATE TABLE dim_product (
    product_key INT PRIMARY KEY,
    product_id VARCHAR(50),
    product_attributes VARIANT  -- JSON data
);
```

### BigQuery

```sql
-- Partitioning by date
CREATE TABLE fact_sales
PARTITION BY date_key
CLUSTER BY customer_key, product_key
AS SELECT ...;

-- Nested and repeated fields
CREATE TABLE fact_order (
    order_id STRING,
    customer_id STRING,
    line_items ARRAY<STRUCT<
        product_id STRING,
        quantity INT64,
        amount FLOAT64
    >>
);
```

### Redshift

```sql
-- Distribution key for joins
CREATE TABLE fact_sales (
    ...
    customer_key INT DISTKEY,  -- Distribute by customer
    ...
) SORTKEY (date_key);  -- Sort by date for range queries

-- Columnar compression
CREATE TABLE dim_product (
    product_key INT ENCODE az64,
    product_name VARCHAR(200) ENCODE lzo,
    ...
);
```

## Best Practices

### 1. Grain Definition
- Define the grain (level of detail) first
- Make grain as atomic as practical
- Keep grain consistent within fact table
- Document grain clearly

### 2. Surrogate Keys
- Use integer surrogate keys for all dimensions
- Faster joins than natural keys
- Handles Type 2 changes
- Protects from source system key changes

### 3. Naming Conventions
- Facts: `fact_<business_process>`
- Dimensions: `dim_<entity>`
- Keys: `<table>_key` (surrogate), `<table>_id` (natural)
- Dates: `effective_date`, `expiration_date`, `is_current`

### 4. Indexes and Partitioning
- Index foreign keys in fact tables
- Partition large fact tables by date
- Cluster on frequently filtered columns
- Monitor query patterns and adjust

### 5. Data Quality
- Enforce referential integrity with foreign keys
- Use NOT NULL for required fields
- Add check constraints for business rules
- Implement data quality checks in ETL

### 6. Documentation
- Document grain for each fact table
- Document SCD type for each dimension
- Document business definitions
- Maintain data dictionary

### 7. Incremental Loading
- Load only changed/new records
- Use staging tables for transformation
- Implement watermark tracking
- Design for idempotent loads

## Common Patterns Summary

1. **Transaction Fact**: One row per business event (orders, transactions)
2. **Periodic Snapshot**: State at regular intervals (inventory, balances)
3. **Accumulating Snapshot**: Process lifecycle with milestones (order fulfillment)
4. **Type 2 Dimension**: Most common for tracking history
5. **Type 1 Dimension**: For reference data that rarely changes
6. **Junk Dimension**: Group low-cardinality flags
7. **Role-Playing Dimension**: Reuse dimension in multiple contexts
8. **Mini-Dimension**: Split frequently changing attributes
9. **Bridge Table**: Handle many-to-many relationships
10. **Conformed Dimension**: Shared across multiple fact tables
