# E-commerce Operations Skill

Comprehensive patterns for managing online store operations across platforms.

## Platform APIs

### Shopify
```javascript
// Admin API v2024-01
const shopify = {
  graphql: 'https://{shop}.myshopify.com/admin/api/2024-01/graphql.json',
  rest: 'https://{shop}.myshopify.com/admin/api/2024-01/',

  auth: {
    type: 'OAuth 2.0' or 'Private App',
    headers: {
      'X-Shopify-Access-Token': token,
      'Content-Type': 'application/json'
    }
  },

  rate_limits: {
    rest: '2 requests/second',
    graphql: '50 points/second'
  }
};

// Create product (GraphQL - preferred)
mutation productCreate($input: ProductInput!) {
  productCreate(input: $input) {
    product {
      id
      title
      handle
      variants(first: 5) {
        edges {
          node {
            id
            price
            inventoryQuantity
          }
        }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

### WooCommerce
```php
// WooCommerce REST API v3
$woo = [
    'url' => 'https://example.com/wp-json/wc/v3/',
    'auth' => [
        'consumer_key' => $key,
        'consumer_secret' => $secret
    ],
    'version' => 'wc/v3'
];

// Create product
POST /wp-json/wc/v3/products
{
  "name": "Product Name",
  "type": "simple",
  "regular_price": "29.99",
  "description": "Product description",
  "short_description": "Short description",
  "categories": [
    { "id": 9 }
  ],
  "images": [
    { "src": "https://example.com/image.jpg" }
  ]
}
```

### BigCommerce
```javascript
// BigCommerce API v3
const bigcommerce = {
  url: 'https://api.bigcommerce.com/stores/{store_hash}/v3/',
  auth: {
    'X-Auth-Token': token,
    'Content-Type': 'application/json'
  },

  // Catalog API
  products: '/catalog/products',
  variants: '/catalog/products/{product_id}/variants',
  brands: '/catalog/brands',
  categories: '/catalog/categories'
};
```

## Product Data Structure

### Complete Product Schema
```json
{
  "sku": "PROD-001",
  "name": "Product Name",
  "type": "simple|variable|grouped|bundle",
  "status": "active|draft|archived",

  "description": {
    "long": "Full product description with HTML",
    "short": "Brief description for cards/lists",
    "features": ["Feature 1", "Feature 2"]
  },

  "pricing": {
    "regular_price": 29.99,
    "compare_at_price": 39.99,
    "cost": 15.00,
    "margin_percent": 50.0,
    "tax_code": "P0000000",
    "currency": "USD"
  },

  "inventory": {
    "quantity": 100,
    "track_inventory": true,
    "allow_backorder": false,
    "low_stock_threshold": 10,
    "reorder_point": 20,
    "reorder_quantity": 50,
    "warehouse_location": "A1-B2-C3"
  },

  "shipping": {
    "weight": 1.5,
    "weight_unit": "lb",
    "dimensions": {
      "length": 10,
      "width": 8,
      "height": 3,
      "unit": "in"
    },
    "requires_shipping": true,
    "shipping_class": "standard"
  },

  "categories": [
    {
      "id": 123,
      "name": "Electronics",
      "path": "Electronics > Audio > Headphones"
    }
  ],

  "tags": ["wireless", "bluetooth", "sale"],

  "images": [
    {
      "src": "https://cdn.example.com/image1.jpg",
      "position": 1,
      "alt": "Product main view",
      "width": 2048,
      "height": 2048
    }
  ],

  "variants": [
    {
      "sku": "PROD-001-BLK-M",
      "name": "Black / Medium",
      "options": [
        {"name": "Color", "value": "Black"},
        {"name": "Size", "value": "Medium"}
      ],
      "price": 29.99,
      "inventory_quantity": 25,
      "image_id": 1
    }
  ],

  "seo": {
    "title": "Product Name - Brand | Store Name",
    "meta_description": "Buy Product Name. Free shipping on orders over $50.",
    "url_handle": "product-name",
    "keywords": ["keyword1", "keyword2"]
  },

  "metadata": {
    "brand": "Brand Name",
    "manufacturer": "Manufacturer Inc",
    "mpn": "MPN-12345",
    "gtin": "012345678905",
    "condition": "new",
    "age_group": "adult",
    "gender": "unisex"
  },

  "timestamps": {
    "created_at": "2025-01-15T10:00:00Z",
    "updated_at": "2025-01-15T10:00:00Z",
    "published_at": "2025-01-15T10:00:00Z"
  }
}
```

## Product Management Best Practices

### SKU Naming Conventions
```
Format: [CATEGORY]-[PRODUCT]-[VARIANT]-[SIZE]

Examples:
- ELE-HEADPHONE-BT-001     (Electronics - Bluetooth Headphones)
- APP-TSHIRT-BLK-M         (Apparel - T-Shirt, Black, Medium)
- HOME-LAMP-DESK-LED       (Home - LED Desk Lamp)

Rules:
- Use uppercase
- Hyphens for readability
- Keep under 20 characters
- Must be unique across catalog
- No special characters (except hyphens)
```

### Product Titles (SEO-Optimized)
```
Format: [Brand] [Product Name] [Key Feature] - [Size/Color/Variant]

Good examples:
✅ "Apple iPhone 15 Pro Max - 256GB - Titanium Blue"
✅ "Nike Air Max 270 Running Shoes - Men's Size 10 - Black/White"
✅ "KitchenAid Professional Stand Mixer - 5 Qt - Empire Red"

Bad examples:
❌ "Awesome Phone!!!" (exclamation marks, not descriptive)
❌ "iPhone" (too short, missing details)
❌ "APPLE IPHONE 15 PRO MAX 256GB TITANIUM BLUE OMG BEST DEAL" (all caps, spam)

Rules:
- 60-70 characters optimal
- Include brand name
- Specify key features
- Clear variant info
- No ALL CAPS or excessive punctuation
```

### Product Descriptions
```markdown
**Structure**:

1. **Opening Hook** (1-2 sentences)
   - Highlight main benefit
   - Create desire

2. **Key Features** (bullet points)
   - 5-7 most important features
   - Focus on benefits, not just specs
   - Use specific numbers/measurements

3. **Detailed Description** (2-3 paragraphs)
   - Materials and construction
   - Use cases and applications
   - Compatibility information

4. **Specifications** (table or list)
   - Technical details
   - Dimensions and weight
   - What's included

5. **Trust Signals** (1 paragraph)
   - Warranty information
   - Return policy
   - Customer service availability

**SEO Best Practices**:
- Include target keyword 2-3 times naturally
- Use semantic keywords (synonyms, related terms)
- 300+ words for main products
- 150+ words for variants
- Include FAQ schema if possible
```

### Image Requirements
```javascript
const imageStandards = {
  product_images: {
    min_resolution: '1200x1200',
    recommended: '2048x2048',
    format: 'JPG or PNG',
    background: 'White (#FFFFFF) for main image',
    file_size: 'Under 500KB (optimized)',
    dpi: '72 for web',

    image_types: {
      main: 'Product on white background, front view',
      alt_1: 'Side or back view',
      alt_2: 'Detail shots (texture, features)',
      lifestyle: 'Product in use, styled setting',
      size_guide: 'Dimensions or size comparison',
      infographic: 'Key features highlighted'
    },

    naming: 'sku-image-type-number.jpg',
    // Example: PROD-001-main-1.jpg
  },

  optimization: {
    tools: ['ImageOptim', 'TinyPNG', 'Squoosh'],
    compression: 'Lossy 85% quality',
    format_choice: {
      photos: 'JPG',
      graphics: 'PNG',
      transparency: 'PNG',
      animation: 'GIF or MP4'
    }
  }
};
```

## Inventory Management Patterns

### Stock Synchronization
```python
# Multi-channel inventory sync
def sync_inventory(sku, quantity, warehouse='main'):
    channels = ['shopify', 'woocommerce', 'amazon', 'ebay']

    # Calculate available quantity across all channels
    reserved = get_reserved_quantity(sku)  # Orders not yet shipped
    safety_stock = get_safety_stock(sku)   # Buffer for demand fluctuations
    available = quantity - reserved - safety_stock

    # Distribute inventory across channels
    for channel in channels:
        channel_allocation = calculate_allocation(channel, available)
        update_channel_inventory(channel, sku, channel_allocation)

    # Log sync operation
    log_inventory_sync(sku, quantity, channels, timestamp=now())
```

### Inventory Allocation Strategy
```javascript
// Priority-based allocation
function allocateInventory(sku, total_quantity) {
  const rules = {
    // Reserve for high-priority
    vip_customers: Math.min(10, total_quantity * 0.05),
    subscription_orders: Math.min(20, total_quantity * 0.10),

    // Allocate to channels by performance
    shopify: total_quantity * 0.40,      // 40% - main storefront
    amazon: total_quantity * 0.30,       // 30% - high volume
    ebay: total_quantity * 0.15,         // 15% - secondary
    wholesale: total_quantity * 0.10,    // 10% - B2B
    safety_stock: total_quantity * 0.05  // 5% - buffer
  };

  return rules;
}
```

## Order Processing Workflow

### Order State Machine
```
┌──────────┐
│  PENDING │  ← Order created, awaiting payment
└────┬─────┘
     │ Payment successful
     ↓
┌──────────┐
│   PAID   │  ← Payment captured
└────┬─────┘
     │ Stock verified
     ↓
┌────────────┐
│ PROCESSING │  ← Order being prepared
└────┬───────┘
     │ Shipped
     ↓
┌──────────┐
│ SHIPPED  │  ← Package in transit
└────┬─────┘
     │ Delivered
     ↓
┌───────────┐
│ DELIVERED │  ← Customer received
└────┬──────┘
     │ After return window
     ↓
┌───────────┐
│ COMPLETED │  ← Final state
└───────────┘

Alternative paths:
- Any state → CANCELLED (before shipping)
- DELIVERED → RETURN_REQUESTED
- RETURN_REQUESTED → REFUNDED
- PAID/PROCESSING → ON_HOLD (issues detected)
```

### Order Validation Rules
```javascript
const orderValidation = {
  customer: {
    email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
    phone: /^\+?[\d\s\-\(\)]+$/,
    required: ['email', 'first_name', 'last_name']
  },

  shipping_address: {
    required: ['address1', 'city', 'province', 'zip', 'country'],
    validate_against: 'address_verification_service',
    allow_po_box: false,  // configurable
    international: {
      require_phone: true,
      require_customs_info: true
    }
  },

  line_items: {
    min_quantity: 1,
    max_quantity: 999,
    validate_inventory: true,
    check_restrictions: ['age_verification', 'hazmat', 'prescription']
  },

  payment: {
    required_status: ['authorized', 'paid'],
    verify_amount: true,  // calculated total = payment amount
    check_fraud_score: true,
    max_fraud_score: 0.7
  },

  totals: {
    subtotal: 'sum(line_items.price * line_items.quantity)',
    discount: 'apply_discounts()',
    tax: 'calculate_tax()',
    shipping: 'get_shipping_rate()',
    total: 'subtotal - discount + tax + shipping'
  }
};
```

## Customer Management

### Customer Lifetime Value (CLV)
```python
def calculate_clv(customer_id):
    """Calculate Customer Lifetime Value"""

    orders = get_customer_orders(customer_id)

    # Historical metrics
    total_revenue = sum(order.total for order in orders)
    total_orders = len(orders)
    avg_order_value = total_revenue / total_orders if total_orders > 0 else 0

    # Time metrics
    first_order = min(order.created_at for order in orders)
    last_order = max(order.created_at for order in orders)
    customer_lifespan_days = (last_order - first_order).days

    # Purchase frequency
    purchase_frequency = total_orders / (customer_lifespan_days / 365) if customer_lifespan_days > 0 else 0

    # Projected CLV (simplified)
    # CLV = Average Order Value × Purchase Frequency × Customer Lifespan
    avg_lifespan_years = 3  # industry dependent
    clv = avg_order_value * purchase_frequency * avg_lifespan_years

    return {
        'clv': clv,
        'total_revenue': total_revenue,
        'total_orders': total_orders,
        'avg_order_value': avg_order_value,
        'purchase_frequency': purchase_frequency,
        'segment': classify_customer(clv)
    }

def classify_customer(clv):
    if clv >= 1000:
        return 'VIP'
    elif clv >= 500:
        return 'high_value'
    elif clv >= 200:
        return 'medium_value'
    else:
        return 'low_value'
```

## Analytics and Reporting

### Key E-commerce Metrics
```javascript
const ecommerceMetrics = {
  conversion_metrics: {
    conversion_rate: 'orders / sessions * 100',
    add_to_cart_rate: 'add_to_carts / product_views * 100',
    cart_abandonment_rate: '(carts_created - orders) / carts_created * 100',
    checkout_abandonment_rate: '(checkouts_started - orders) / checkouts_started * 100'
  },

  financial_metrics: {
    revenue: 'sum(orders.total)',
    aov: 'revenue / orders',                    // Average Order Value
    gross_profit: 'revenue - cogs',
    gross_margin: 'gross_profit / revenue * 100'
  },

  customer_metrics: {
    cac: 'marketing_spend / new_customers',    // Customer Acquisition Cost
    clv: 'calculated per customer (see above)',
    clv_cac_ratio: 'clv / cac',               // Should be > 3:1
    retention_rate: 'returning_customers / total_customers * 100'
  },

  inventory_metrics: {
    inventory_turnover: 'cogs / avg_inventory_value',
    days_inventory: '365 / inventory_turnover',
    stock_out_rate: 'out_of_stock_events / total_sku_days * 100',
    sell_through_rate: 'units_sold / units_received * 100'
  },

  benchmarks: {
    good_conversion_rate: '2-3%',
    good_aov_growth: '+10% YoY',
    good_clv_cac: '3:1 or higher',
    good_inventory_turnover: '4-6x per year'
  }
};
```

## Security Best Practices

### PCI DSS Compliance
```javascript
const pciCompliance = {
  never_store: [
    'Full credit card number (except last 4)',
    'CVV/CVC code',
    'PIN numbers',
    'Card magnetic strip data'
  ],

  tokenization: {
    use: 'Payment gateway tokens',
    example: {
      stored: 'tok_1234567890abcdef',
      display: '**** **** **** 1234',
      vault: 'payment_gateway'
    }
  },

  secure_transmission: {
    protocol: 'TLS 1.2 or higher',
    certificate: 'Valid SSL certificate',
    endpoints: 'All payment endpoints over HTTPS'
  },

  access_control: {
    principle: 'Least privilege',
    mfa: 'Required for admin access',
    audit_logs: 'Track all payment data access'
  }
};
```

### Fraud Prevention
```python
def assess_fraud_risk(order):
    """Fraud detection scoring"""

    risk_score = 0

    # High-risk indicators (+20 points each)
    if order.billing_address != order.shipping_address:
        risk_score += 20
    if order.shipping_country != order.billing_country:
        risk_score += 20
    if order.total > 500 and customer.total_orders == 0:
        risk_score += 20

    # Medium-risk indicators (+10 points each)
    if order.ip_country != order.billing_country:
        risk_score += 10
    if customer.created_at > now() - timedelta(hours=24):
        risk_score += 10
    if len(customer.orders_today) > 3:
        risk_score += 10

    # Low-risk indicators (+5 points each)
    if order.email in disposable_email_domains:
        risk_score += 5
    if order.shipping_speed == 'overnight':
        risk_score += 5

    # Risk classification
    if risk_score >= 50:
        return {'risk': 'high', 'action': 'manual_review'}
    elif risk_score >= 30:
        return {'risk': 'medium', 'action': 'verify_address'}
    else:
        return {'risk': 'low', 'action': 'process'}
```

## Integration Patterns

### Webhook Handling
```javascript
// Shopify webhook handler example
app.post('/webhooks/orders/create', async (req, res) => {
  // Verify webhook authenticity
  const hmac = req.headers['x-shopify-hmac-sha256'];
  const verified = verifyWebhook(req.body, hmac);

  if (!verified) {
    return res.status(401).send('Unauthorized');
  }

  // Process order
  const order = req.body;

  try {
    // Update internal systems
    await syncOrderToDatabase(order);
    await updateInventory(order.line_items);
    await notifyFulfillment(order.id);

    res.status(200).send('OK');
  } catch (error) {
    // Shopify will retry on non-200 response
    res.status(500).send('Error processing webhook');
  }
});
```

This skill provides comprehensive e-commerce operation patterns. Apply these guidelines when managing online stores.
