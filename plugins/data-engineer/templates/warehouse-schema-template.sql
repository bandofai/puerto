-- ============================================
-- DATA WAREHOUSE SCHEMA TEMPLATE
-- Star Schema Example for E-Commerce Analytics
-- ============================================

-- This template demonstrates a complete star schema design
-- with fact tables and dimension tables following best practices

-- ============================================
-- DIMENSION TABLES
-- ============================================

-- Date Dimension (Type 0 - Static, Pre-populated)
-- Contains all dates for the business lifecycle
CREATE TABLE dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE NOT NULL UNIQUE,

    -- Day attributes
    day_of_week INT NOT NULL,
    day_name VARCHAR(10) NOT NULL,
    day_of_month INT NOT NULL,
    day_of_year INT NOT NULL,

    -- Week attributes
    week_of_year INT NOT NULL,
    week_of_month INT NOT NULL,

    -- Month attributes
    month_number INT NOT NULL,
    month_name VARCHAR(10) NOT NULL,
    month_name_short VARCHAR(3) NOT NULL,

    -- Quarter attributes
    quarter INT NOT NULL,
    quarter_name VARCHAR(2) NOT NULL,

    -- Year attributes
    year INT NOT NULL,
    fiscal_year INT NOT NULL,
    fiscal_quarter INT NOT NULL,

    -- Special indicators
    is_weekend BOOLEAN NOT NULL,
    is_holiday BOOLEAN NOT NULL,
    holiday_name VARCHAR(100),
    is_business_day BOOLEAN NOT NULL,

    -- Relative dates
    is_current_day BOOLEAN NOT NULL DEFAULT FALSE,
    is_current_month BOOLEAN NOT NULL DEFAULT FALSE,
    is_current_quarter BOOLEAN NOT NULL DEFAULT FALSE,
    is_current_year BOOLEAN NOT NULL DEFAULT FALSE
);

-- Create indexes for common query patterns
CREATE INDEX idx_dim_date_year_month ON dim_date(year, month_number);
CREATE INDEX idx_dim_date_fiscal ON dim_date(fiscal_year, fiscal_quarter);

-- Customer Dimension (Type 2 - Track Historical Changes)
-- Tracks customer attributes with full history
CREATE TABLE dim_customer (
    customer_key BIGSERIAL PRIMARY KEY,

    -- Natural key (business key from source system)
    customer_id VARCHAR(50) NOT NULL,

    -- Customer attributes
    customer_name VARCHAR(200) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(200),
    phone VARCHAR(20),

    -- Address attributes
    address_line1 VARCHAR(500),
    address_line2 VARCHAR(500),
    city VARCHAR(100),
    state VARCHAR(50),
    country VARCHAR(50),
    zip_code VARCHAR(20),
    region VARCHAR(50),

    -- Demographic attributes
    gender VARCHAR(20),
    age_range VARCHAR(20),
    income_range VARCHAR(50),

    -- Customer classification
    customer_segment VARCHAR(50),  -- Bronze, Silver, Gold, Platinum
    customer_type VARCHAR(50),     -- Individual, Business
    acquisition_channel VARCHAR(50),

    -- Status
    is_active BOOLEAN DEFAULT TRUE,
    account_status VARCHAR(50),

    -- SCD Type 2 tracking columns
    effective_date DATE NOT NULL,
    expiration_date DATE NOT NULL DEFAULT '9999-12-31',
    is_current BOOLEAN NOT NULL DEFAULT TRUE,

    -- Metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    source_system VARCHAR(50) DEFAULT 'CRM'
);

-- Indexes for Type 2 dimension queries
CREATE INDEX idx_dim_customer_id ON dim_customer(customer_id);
CREATE INDEX idx_dim_customer_current ON dim_customer(customer_id, is_current) WHERE is_current = TRUE;
CREATE INDEX idx_dim_customer_effective ON dim_customer(effective_date, expiration_date);
CREATE INDEX idx_dim_customer_segment ON dim_customer(customer_segment);

-- Product Dimension (Type 2 - Track Product Changes)
CREATE TABLE dim_product (
    product_key BIGSERIAL PRIMARY KEY,

    -- Natural key
    product_id VARCHAR(50) NOT NULL,

    -- Product attributes
    product_name VARCHAR(200) NOT NULL,
    product_description TEXT,
    sku VARCHAR(100),
    barcode VARCHAR(100),

    -- Product hierarchy
    category VARCHAR(100),
    subcategory VARCHAR(100),
    department VARCHAR(100),
    brand VARCHAR(100),
    manufacturer VARCHAR(100),

    -- Pricing
    unit_cost DECIMAL(10,2),
    list_price DECIMAL(10,2),
    current_price DECIMAL(10,2),

    -- Product attributes
    size VARCHAR(50),
    color VARCHAR(50),
    weight DECIMAL(10,2),
    weight_unit VARCHAR(20),

    -- Status
    is_active BOOLEAN DEFAULT TRUE,
    product_status VARCHAR(50),

    -- SCD Type 2 tracking
    effective_date DATE NOT NULL,
    expiration_date DATE NOT NULL DEFAULT '9999-12-31',
    is_current BOOLEAN NOT NULL DEFAULT TRUE,

    -- Metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX idx_dim_product_id ON dim_product(product_id);
CREATE INDEX idx_dim_product_current ON dim_product(product_id, is_current) WHERE is_current = TRUE;
CREATE INDEX idx_dim_product_category ON dim_product(category, subcategory);
CREATE INDEX idx_dim_product_brand ON dim_product(brand);

-- Store/Location Dimension (Type 1 - Overwrite)
-- Store attributes change infrequently
CREATE TABLE dim_store (
    store_key SERIAL PRIMARY KEY,

    -- Natural key
    store_id VARCHAR(50) NOT NULL UNIQUE,

    -- Store attributes
    store_name VARCHAR(200) NOT NULL,
    store_number VARCHAR(50),
    store_type VARCHAR(50),  -- Retail, Warehouse, Distribution Center

    -- Location
    address VARCHAR(500),
    city VARCHAR(100),
    state VARCHAR(50),
    country VARCHAR(50),
    zip_code VARCHAR(20),
    region VARCHAR(50),
    timezone VARCHAR(50),

    -- Store details
    square_footage INT,
    open_date DATE,
    manager_name VARCHAR(200),
    phone VARCHAR(20),
    email VARCHAR(200),

    -- Status
    is_active BOOLEAN DEFAULT TRUE,
    store_status VARCHAR(50),

    -- Metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX idx_dim_store_location ON dim_store(country, state, city);
CREATE INDEX idx_dim_store_region ON dim_store(region);

-- Promotion Dimension (Type 2 - Track Promotion Changes)
CREATE TABLE dim_promotion (
    promotion_key SERIAL PRIMARY KEY,

    -- Natural key
    promotion_id VARCHAR(50) NOT NULL,

    -- Promotion attributes
    promotion_name VARCHAR(200) NOT NULL,
    promotion_description TEXT,
    promotion_type VARCHAR(50),  -- Percentage, Fixed Amount, BOGO
    discount_percentage DECIMAL(5,2),
    discount_amount DECIMAL(10,2),

    -- Promotion period
    start_date DATE,
    end_date DATE,

    -- Conditions
    minimum_purchase DECIMAL(10,2),
    maximum_discount DECIMAL(10,2),

    -- Status
    is_active BOOLEAN DEFAULT TRUE,

    -- SCD Type 2 tracking
    effective_date DATE NOT NULL,
    expiration_date DATE NOT NULL DEFAULT '9999-12-31',
    is_current BOOLEAN NOT NULL DEFAULT TRUE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_dim_promotion_dates ON dim_promotion(start_date, end_date);

-- Junk Dimension - Groups low-cardinality transaction flags
CREATE TABLE dim_transaction_flags (
    transaction_flag_key SERIAL PRIMARY KEY,

    -- Low-cardinality flags (pre-populate all combinations)
    is_online_order BOOLEAN NOT NULL,
    is_gift_wrapped BOOLEAN NOT NULL,
    is_express_shipping BOOLEAN NOT NULL,
    is_first_purchase BOOLEAN NOT NULL,
    payment_method VARCHAR(20) NOT NULL,  -- Cash, Credit, Debit, PayPal
    order_channel VARCHAR(20) NOT NULL,   -- Web, Mobile, Store, Phone

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Unique constraint for combinations
    UNIQUE(is_online_order, is_gift_wrapped, is_express_shipping,
           is_first_purchase, payment_method, order_channel)
);

-- ============================================
-- FACT TABLES
-- ============================================

-- Fact Sales (Transaction Grain - One row per order line item)
CREATE TABLE fact_sales (
    sales_key BIGSERIAL PRIMARY KEY,

    -- Foreign keys to dimensions
    date_key INT NOT NULL,
    customer_key BIGINT NOT NULL,
    product_key BIGINT NOT NULL,
    store_key INT NOT NULL,
    promotion_key INT,
    transaction_flag_key INT NOT NULL,

    -- Degenerate dimensions (transaction identifiers stored in fact)
    order_id VARCHAR(50) NOT NULL,
    line_number INT NOT NULL,

    -- Additive measures (can be summed)
    quantity_sold DECIMAL(10,2) NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    discount_amount DECIMAL(10,2) DEFAULT 0,
    tax_amount DECIMAL(10,2) NOT NULL,
    shipping_amount DECIMAL(10,2) DEFAULT 0,
    total_amount DECIMAL(10,2) NOT NULL,

    -- Cost and profit measures
    unit_cost DECIMAL(10,2),
    total_cost DECIMAL(10,2),
    gross_profit DECIMAL(10,2),

    -- Non-additive measures (ratios, percentages)
    profit_margin DECIMAL(5,2),  -- Percentage
    discount_percentage DECIMAL(5,2),

    -- Metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    source_system VARCHAR(50) DEFAULT 'POS',

    -- Foreign key constraints
    CONSTRAINT fk_sales_date FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    CONSTRAINT fk_sales_customer FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key),
    CONSTRAINT fk_sales_product FOREIGN KEY (product_key) REFERENCES dim_product(product_key),
    CONSTRAINT fk_sales_store FOREIGN KEY (store_key) REFERENCES dim_store(store_key),
    CONSTRAINT fk_sales_promotion FOREIGN KEY (promotion_key) REFERENCES dim_promotion(promotion_key),
    CONSTRAINT fk_sales_flags FOREIGN KEY (transaction_flag_key) REFERENCES dim_transaction_flags(transaction_flag_key),

    -- Business rule constraints
    CONSTRAINT chk_sales_quantity CHECK (quantity_sold > 0),
    CONSTRAINT chk_sales_amounts CHECK (total_amount >= 0)
);

-- Indexes for query performance
CREATE INDEX idx_fact_sales_date ON fact_sales(date_key);
CREATE INDEX idx_fact_sales_customer ON fact_sales(customer_key);
CREATE INDEX idx_fact_sales_product ON fact_sales(product_key);
CREATE INDEX idx_fact_sales_store ON fact_sales(store_key);
CREATE INDEX idx_fact_sales_order ON fact_sales(order_id);

-- Composite indexes for common query patterns
CREATE INDEX idx_fact_sales_date_customer ON fact_sales(date_key, customer_key);
CREATE INDEX idx_fact_sales_date_product ON fact_sales(date_key, product_key);

-- Partitioning by date (for large tables)
-- ALTER TABLE fact_sales PARTITION BY RANGE (date_key);

-- Fact Inventory Snapshot (Periodic Snapshot - Daily inventory levels)
CREATE TABLE fact_inventory_snapshot (
    inventory_snapshot_key BIGSERIAL PRIMARY KEY,

    -- Foreign keys
    date_key INT NOT NULL,
    product_key BIGINT NOT NULL,
    store_key INT NOT NULL,

    -- Semi-additive measures (sum across dimensions but not time)
    quantity_on_hand INT NOT NULL,
    quantity_allocated INT NOT NULL,
    quantity_available INT NOT NULL,
    quantity_on_order INT NOT NULL,

    -- Additive measures (changes during the day)
    units_received_today INT DEFAULT 0,
    units_shipped_today INT DEFAULT 0,
    units_sold_today INT DEFAULT 0,
    units_adjusted_today INT DEFAULT 0,

    -- Value measures
    unit_cost DECIMAL(10,2),
    inventory_value DECIMAL(12,2),

    -- Metadata
    snapshot_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Foreign keys
    CONSTRAINT fk_inventory_date FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    CONSTRAINT fk_inventory_product FOREIGN KEY (product_key) REFERENCES dim_product(product_key),
    CONSTRAINT fk_inventory_store FOREIGN KEY (store_key) REFERENCES dim_store(store_key),

    -- Unique constraint to prevent duplicate snapshots
    UNIQUE(date_key, product_key, store_key)
);

-- Indexes
CREATE INDEX idx_fact_inventory_date ON fact_inventory_snapshot(date_key);
CREATE INDEX idx_fact_inventory_product ON fact_inventory_snapshot(product_key);
CREATE INDEX idx_fact_inventory_store ON fact_inventory_snapshot(store_key);

-- Fact Customer Activity (Accumulating Snapshot - Customer lifecycle)
CREATE TABLE fact_customer_activity (
    customer_activity_key BIGSERIAL PRIMARY KEY,

    -- Customer dimension
    customer_key BIGINT NOT NULL,

    -- Multiple date dimensions for milestones
    registration_date_key INT NOT NULL,
    first_purchase_date_key INT,
    last_purchase_date_key INT,

    -- Activity metrics
    total_orders INT DEFAULT 0,
    total_items_purchased INT DEFAULT 0,
    total_revenue DECIMAL(12,2) DEFAULT 0,
    average_order_value DECIMAL(10,2),

    -- Engagement metrics
    days_since_last_purchase INT,
    purchase_frequency DECIMAL(10,2),  -- Orders per month

    -- Customer lifetime value
    lifetime_value DECIMAL(12,2),

    -- Status
    customer_status VARCHAR(50),  -- Active, Churned, At Risk
    last_updated_date DATE,

    -- Metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Foreign keys
    CONSTRAINT fk_activity_customer FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key),
    CONSTRAINT fk_activity_reg_date FOREIGN KEY (registration_date_key) REFERENCES dim_date(date_key),
    CONSTRAINT fk_activity_first_date FOREIGN KEY (first_purchase_date_key) REFERENCES dim_date(date_key),
    CONSTRAINT fk_activity_last_date FOREIGN KEY (last_purchase_date_key) REFERENCES dim_date(date_key)
);

-- Indexes
CREATE INDEX idx_fact_activity_customer ON fact_customer_activity(customer_key);
CREATE INDEX idx_fact_activity_status ON fact_customer_activity(customer_status);

-- ============================================
-- HELPER TABLES
-- ============================================

-- ETL Watermark Table (track incremental loads)
CREATE TABLE etl_watermarks (
    pipeline_name VARCHAR(100) PRIMARY KEY,
    watermark_value TIMESTAMP NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Data Quality Metrics (track quality over time)
CREATE TABLE data_quality_metrics (
    metric_id BIGSERIAL PRIMARY KEY,
    table_name VARCHAR(100) NOT NULL,
    metric_date DATE NOT NULL,
    row_count BIGINT,
    null_percentage DECIMAL(5,2),
    duplicate_percentage DECIMAL(5,2),
    quality_score DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- VIEWS FOR COMMON QUERIES
-- ============================================

-- Sales Summary by Date and Product
CREATE VIEW vw_sales_by_product AS
SELECT
    d.full_date,
    d.year,
    d.month_name,
    p.product_name,
    p.category,
    p.brand,
    SUM(f.quantity_sold) as total_quantity,
    SUM(f.total_amount) as total_revenue,
    SUM(f.gross_profit) as total_profit,
    AVG(f.profit_margin) as avg_profit_margin,
    COUNT(DISTINCT f.order_id) as order_count
FROM fact_sales f
JOIN dim_date d ON f.date_key = d.date_key
JOIN dim_product p ON f.product_key = p.product_key
WHERE p.is_current = TRUE
GROUP BY d.full_date, d.year, d.month_name, p.product_name, p.category, p.brand;

-- Customer Segmentation View
CREATE VIEW vw_customer_segmentation AS
SELECT
    c.customer_key,
    c.customer_name,
    c.customer_segment,
    ca.total_orders,
    ca.total_revenue,
    ca.lifetime_value,
    ca.customer_status,
    ca.days_since_last_purchase
FROM dim_customer c
JOIN fact_customer_activity ca ON c.customer_key = ca.customer_key
WHERE c.is_current = TRUE;

-- ============================================
-- COMMENTS FOR DOCUMENTATION
-- ============================================

COMMENT ON TABLE fact_sales IS 'Transaction fact table storing one row per order line item';
COMMENT ON TABLE fact_inventory_snapshot IS 'Daily inventory snapshot at product/store level';
COMMENT ON TABLE dim_customer IS 'Customer dimension with Type 2 SCD for historical tracking';
COMMENT ON TABLE dim_product IS 'Product dimension with Type 2 SCD for price/attribute changes';
COMMENT ON TABLE dim_date IS 'Date dimension pre-populated with calendar attributes';

-- ============================================
-- SAMPLE QUERIES
-- ============================================

-- Example: Sales by Category and Month
-- SELECT
--     d.year,
--     d.month_name,
--     p.category,
--     SUM(f.total_amount) as revenue,
--     SUM(f.quantity_sold) as units_sold
-- FROM fact_sales f
-- JOIN dim_date d ON f.date_key = d.date_key
-- JOIN dim_product p ON f.product_key = p.product_key AND p.is_current = TRUE
-- WHERE d.year = 2024
-- GROUP BY d.year, d.month_name, p.category
-- ORDER BY d.year, d.month_name, revenue DESC;

-- Example: Top Customers by Revenue
-- SELECT
--     c.customer_name,
--     c.customer_segment,
--     SUM(f.total_amount) as total_revenue,
--     COUNT(DISTINCT f.order_id) as order_count
-- FROM fact_sales f
-- JOIN dim_customer c ON f.customer_key = c.customer_key AND c.is_current = TRUE
-- JOIN dim_date d ON f.date_key = d.date_key
-- WHERE d.year = 2024
-- GROUP BY c.customer_name, c.customer_segment
-- ORDER BY total_revenue DESC
-- LIMIT 10;
