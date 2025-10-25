# Inventory Management Skill

Expert patterns for inventory tracking, optimization, and warehouse operations.

## Inventory Control Fundamentals

### Core Metrics
```javascript
const inventoryMetrics = {
  // Stock levels
  on_hand: 'Physical inventory in warehouse',
  available: 'on_hand - reserved - safety_stock',
  reserved: 'Allocated to orders not yet shipped',
  safety_stock: 'Buffer for demand variability',

  // Reorder calculations
  reorder_point: '(avg_daily_demand × lead_time_days) + safety_stock',
  reorder_quantity: 'EOQ or min_order_quantity',

  // Performance metrics
  turnover_ratio: 'COGS / average_inventory_value',
  days_on_hand: '365 / turnover_ratio',
  stock_out_rate: 'out_of_stock_days / total_days',
  fill_rate: 'orders_fulfilled_completely / total_orders',

  // Financial metrics
  carrying_cost: 'inventory_value × 0.25',  // 25% annually
  dead_stock_value: 'sum(items with 0 sales in 90 days)'
};
```

### Economic Order Quantity (EOQ)
```python
import math

def calculate_eoq(annual_demand, ordering_cost, holding_cost_per_unit):
    """
    Calculate optimal order quantity to minimize total cost

    Args:
        annual_demand: Units sold per year
        ordering_cost: Fixed cost per order ($)
        holding_cost_per_unit: Annual cost to hold one unit ($)

    Returns:
        Optimal order quantity
    """
    eoq = math.sqrt((2 * annual_demand * ordering_cost) / holding_cost_per_unit)
    return round(eoq)

# Example:
# Annual demand: 1,200 units
# Ordering cost: $50 per order
# Holding cost: $5 per unit per year
eoq = calculate_eoq(1200, 50, 5)  # Result: 155 units

# Total cost analysis
orders_per_year = 1200 / eoq  # 7.7 orders
ordering_cost_total = orders_per_year * 50  # $387
holding_cost_total = (eoq / 2) * 5  # $387
total_cost = ordering_cost_total + holding_cost_total  # $774
```

### Safety Stock Calculation
```python
def calculate_safety_stock(avg_demand, max_demand, avg_lead_time, max_lead_time):
    """
    Safety stock protects against variability in demand and lead time

    Method: Maximum usage during maximum lead time - Average usage during average lead time
    """
    max_usage = max_demand * max_lead_time
    avg_usage = avg_demand * avg_lead_time
    safety_stock = max_usage - avg_usage

    return safety_stock

# Example:
safety_stock = calculate_safety_stock(
    avg_demand=10,      # 10 units/day average
    max_demand=15,      # 15 units/day maximum
    avg_lead_time=7,    # 7 days average
    max_lead_time=10    # 10 days maximum
)
# Result: (15 × 10) - (10 × 7) = 150 - 70 = 80 units
```

### Reorder Point System
```python
def calculate_reorder_point(avg_daily_demand, lead_time_days, safety_stock):
    """
    Reorder point: When to place next order

    ROP = (Average Daily Demand × Lead Time) + Safety Stock
    """
    rop = (avg_daily_demand * lead_time_days) + safety_stock
    return rop

# Example:
rop = calculate_reorder_point(
    avg_daily_demand=10,
    lead_time_days=7,
    safety_stock=80
)
# Result: (10 × 7) + 80 = 150 units

# When inventory drops to 150 units, place new order
```

## ABC Analysis

### Classification Method
```python
def abc_classification(products):
    """
    Classify inventory using Pareto principle (80/20 rule)

    A-items: 20% of SKUs, 80% of revenue (tight control, frequent review)
    B-items: 30% of SKUs, 15% of revenue (moderate control, periodic review)
    C-items: 50% of SKUs, 5% of revenue (minimal control, annual review)
    """

    # Calculate revenue contribution
    for product in products:
        product['annual_revenue'] = product['annual_sales'] * product['unit_price']

    # Sort by revenue (descending)
    products.sort(key=lambda x: x['annual_revenue'], reverse=True)

    # Calculate cumulative percentage
    total_revenue = sum(p['annual_revenue'] for p in products)
    cumulative = 0

    for product in products:
        cumulative += product['annual_revenue']
        cumulative_percent = (cumulative / total_revenue) * 100

        if cumulative_percent <= 80:
            product['category'] = 'A'
            product['review_frequency'] = 'daily'
            product['service_level'] = 99  # %
        elif cumulative_percent <= 95:
            product['category'] = 'B'
            product['review_frequency'] = 'weekly'
            product['service_level'] = 95  # %
        else:
            product['category'] = 'C'
            product['review_frequency'] = 'monthly'
            product['service_level'] = 90  # %

    return products

# Management guidelines:
abc_management = {
    'A-items': {
        'inventory_review': 'Daily',
        'forecasting': 'Detailed statistical methods',
        'ordering': 'Frequent, small batches (JIT if possible)',
        'safety_stock': 'Low (due to frequent ordering)',
        'attention': 'High - track closely, optimize constantly'
    },
    'B-items': {
        'inventory_review': 'Weekly',
        'forecasting': 'Standard methods',
        'ordering': 'Periodic review (weekly/biweekly)',
        'safety_stock': 'Moderate',
        'attention': 'Medium - standard controls'
    },
    'C-items': {
        'inventory_review': 'Monthly or quarterly',
        'forecasting': 'Simple methods or min/max',
        'ordering': 'Bulk orders to minimize ordering cost',
        'safety_stock': 'High (infrequent ordering)',
        'attention': 'Low - automate where possible'
    }
}
```

## Demand Forecasting

### Moving Average
```python
def moving_average_forecast(sales_history, periods=3):
    """
    Simple moving average - good for stable demand

    Args:
        sales_history: List of historical sales (most recent last)
        periods: Number of periods to average
    """
    if len(sales_history) < periods:
        return sum(sales_history) / len(sales_history)

    recent = sales_history[-periods:]
    forecast = sum(recent) / periods

    return forecast

# Example:
sales = [100, 105, 98, 110, 107, 115, 112]
forecast = moving_average_forecast(sales, periods=3)
# Result: (115 + 112 + 107) / 3 = 111.33
```

### Exponential Smoothing
```python
def exponential_smoothing_forecast(sales_history, alpha=0.3):
    """
    Exponential smoothing - more weight to recent data

    Args:
        sales_history: List of historical sales
        alpha: Smoothing constant (0-1), higher = more reactive
               0.1-0.3: Stable products
               0.3-0.5: Moderate variation
               0.5-0.7: High variation
    """
    if len(sales_history) == 0:
        return 0

    forecast = sales_history[0]  # Start with first actual

    for actual in sales_history[1:]:
        forecast = alpha * actual + (1 - alpha) * forecast

    return forecast

# Example:
sales = [100, 105, 98, 110, 107, 115, 112]
forecast = exponential_smoothing_forecast(sales, alpha=0.3)
# Recent sales get more weight than older sales
```

### Trend Analysis
```python
def linear_regression_forecast(sales_history, periods_ahead=1):
    """
    Linear regression for trending demand

    Good for products with clear upward or downward trend
    """
    import numpy as np

    n = len(sales_history)
    x = np.array(range(1, n + 1))
    y = np.array(sales_history)

    # Calculate slope (m) and intercept (b)
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)

    slope = numerator / denominator
    intercept = y_mean - slope * x_mean

    # Forecast
    next_period = n + periods_ahead
    forecast = slope * next_period + intercept

    return {
        'forecast': forecast,
        'slope': slope,  # Units per period
        'trend': 'increasing' if slope > 0 else 'decreasing'
    }
```

### Seasonality Adjustment
```python
def calculate_seasonal_index(monthly_sales, years=2):
    """
    Calculate seasonal index for demand with recurring patterns

    Example: Retail with holiday peaks, summer slowdowns
    """
    # Calculate average sales per month across years
    seasonal_index = {}

    for month in range(1, 13):
        month_sales = [monthly_sales[i] for i in range(month-1, len(monthly_sales), 12)]
        avg_for_month = sum(month_sales) / len(month_sales)

        overall_avg = sum(monthly_sales) / len(monthly_sales)
        seasonal_index[month] = avg_for_month / overall_avg

    return seasonal_index

# Example:
monthly_sales = [100, 95, 110, 105, 120, 130, 140, 135, 115, 110, 180, 200,  # Year 1
                 105, 100, 115, 110, 125, 135, 145, 140, 120, 115, 190, 210]  # Year 2

seasonal_idx = calculate_seasonal_index(monthly_sales)
# Results:
# Jan: 1.0 (baseline)
# Nov: 1.7 (70% above average - holiday season)
# Dec: 2.0 (100% above average - peak)

# Apply to forecast:
base_forecast = 100
nov_forecast = base_forecast * seasonal_idx[11]  # 170 units
dec_forecast = base_forecast * seasonal_idx[12]  # 200 units
```

## Stock Replenishment Strategies

### Min-Max System
```python
def min_max_replenishment(current_stock, min_level, max_level):
    """
    Simple replenishment: Order up to max when below min

    Good for C-items with low value and stable demand
    """
    if current_stock < min_level:
        order_quantity = max_level - current_stock
        return {
            'action': 'order',
            'quantity': order_quantity,
            'reason': f'Stock {current_stock} below min {min_level}'
        }
    else:
        return {
            'action': 'no_action',
            'quantity': 0,
            'reason': f'Stock {current_stock} above min {min_level}'
        }

# Example:
result = min_max_replenishment(
    current_stock=15,
    min_level=20,
    max_level=100
)
# Result: Order 85 units (100 - 15)
```

### Periodic Review System
```python
def periodic_review_order(current_stock, target_level, lead_time, review_period, avg_demand):
    """
    Review inventory at fixed intervals (e.g., every Monday)
    Order enough to reach target level considering demand during review + lead time

    Good for multiple items from same supplier (consolidate orders)
    """
    # Demand during review period + lead time
    protection_period = review_period + lead_time
    expected_demand = avg_demand * protection_period

    # Order up to target level
    order_quantity = target_level - current_stock + expected_demand

    return max(0, order_quantity)

# Example:
order = periodic_review_order(
    current_stock=50,
    target_level=200,
    lead_time=7,      # days
    review_period=7,  # weekly review
    avg_demand=10     # units/day
)
# Result: 200 - 50 + (10 × 14) = 290 units
```

### Just-In-Time (JIT)
```python
jit_principles = {
    'philosophy': 'Pull system - produce/order only what is needed, when needed',

    'requirements': [
        'Reliable suppliers with short lead times',
        'Consistent quality (no defects)',
        'Frequent, small deliveries',
        'Strong supplier relationships',
        'Predictable demand'
    ],

    'benefits': [
        'Minimal inventory carrying costs',
        'Reduced warehouse space needs',
        'Less capital tied up in inventory',
        'Fresher products (important for perishables)'
    ],

    'risks': [
        'Vulnerable to supply chain disruptions',
        'No buffer for demand spikes',
        'Requires excellent demand forecasting',
        'Higher ordering costs (frequent orders)'
    ],

    'best_for': [
        'High-value A-items',
        'Perishable goods',
        'Fashion items (short lifecycle)',
        'Made-to-order products'
    ]
}
```

## Inventory Tracking Methods

### FIFO (First-In, First-Out)
```python
def fifo_valuation(inventory_layers):
    """
    FIFO: Sell oldest inventory first

    Use cases:
    - Perishable goods
    - Items with expiration dates
    - Fashion/seasonal items

    Accounting: Oldest costs match with revenue
    """
    cogs = 0
    remaining_inventory = inventory_layers.copy()

    # Sell from oldest layer first
    for layer in remaining_inventory:
        if layer['quantity'] > 0:
            sold_from_layer = min(layer['quantity'], units_to_sell)
            cogs += sold_from_layer * layer['unit_cost']
            layer['quantity'] -= sold_from_layer
            units_to_sell -= sold_from_layer

            if units_to_sell == 0:
                break

    return {
        'cogs': cogs,
        'remaining_layers': [l for l in remaining_inventory if l['quantity'] > 0]
    }
```

### LIFO (Last-In, First-Out)
```python
# Note: LIFO not allowed under IFRS, allowed in US GAAP

def lifo_valuation(inventory_layers, units_to_sell):
    """
    LIFO: Sell newest inventory first

    Accounting implications:
    - In rising prices: Higher COGS, lower profit, lower taxes
    - In falling prices: Lower COGS, higher profit, higher taxes
    """
    cogs = 0
    remaining_inventory = inventory_layers.copy()

    # Sell from newest layer first
    for layer in reversed(remaining_inventory):
        if layer['quantity'] > 0:
            sold_from_layer = min(layer['quantity'], units_to_sell)
            cogs += sold_from_layer * layer['unit_cost']
            layer['quantity'] -= sold_from_layer
            units_to_sell -= sold_from_layer

            if units_to_sell == 0:
                break

    return {
        'cogs': cogs,
        'remaining_layers': [l for l in remaining_inventory if l['quantity'] > 0]
    }
```

### Weighted Average
```python
def weighted_average_valuation(inventory_layers):
    """
    Weighted average: Average cost of all units

    Simple, smooth cost variations
    """
    total_units = sum(layer['quantity'] for layer in inventory_layers)
    total_cost = sum(layer['quantity'] * layer['unit_cost'] for layer in inventory_layers)

    if total_units == 0:
        return 0

    avg_cost = total_cost / total_units

    return {
        'average_unit_cost': avg_cost,
        'total_inventory_value': total_cost,
        'total_units': total_units
    }
```

## Cycle Counting

### Cycle Count Strategy
```python
def generate_cycle_count_schedule(products, abc_classification):
    """
    Physical inventory counts performed regularly instead of annual full count

    Frequency by ABC classification:
    - A-items: Count weekly or biweekly (52-26 times/year)
    - B-items: Count monthly (12 times/year)
    - C-items: Count quarterly (4 times/year)
    """
    schedule = []

    for product in products:
        if product['category'] == 'A':
            frequency_days = 7  # Weekly
        elif product['category'] == 'B':
            frequency_days = 30  # Monthly
        else:
            frequency_days = 90  # Quarterly

        schedule.append({
            'sku': product['sku'],
            'category': product['category'],
            'frequency_days': frequency_days,
            'next_count_date': today() + timedelta(days=frequency_days)
        })

    return schedule
```

### Cycle Count Process
```markdown
1. **Select items** for count (from schedule)
2. **Freeze transactions** during count (or use snapshot)
3. **Physical count** by staff (blind count - no system qty shown)
4. **Compare** physical vs system quantity
5. **Investigate discrepancies**:
   - Count again if >5% variance
   - Check recent transactions
   - Look for common issues:
     - Receiving not recorded
     - Shipments not deducted
     - Returns not processed
     - Theft/damage
6. **Adjust** system quantity if confirmed
7. **Analyze trends**:
   - High variance SKUs need investigation
   - Patterns indicate process problems
8. **Update** next count date

## Accuracy targets:
- A-items: 98-99% accuracy
- B-items: 95-97% accuracy
- C-items: 90-95% accuracy
```

## Warehouse Organization

### Bin Location System
```python
def generate_bin_location(warehouse_zones):
    """
    Structured bin location naming for easy picking

    Format: ZONE-AISLE-RACK-SHELF-BIN
    Example: A-12-03-02-B

    Zones:
    - A: Fast-moving items (near packing)
    - B: Medium-moving
    - C: Slow-moving
    - R: Receiving area
    - Q: Quality control
    - D: Damaged/returns
    """

    location_format = {
        'zone': 'A-Z',           # Warehouse zone
        'aisle': '01-99',        # Aisle number
        'rack': '01-20',         # Rack number in aisle
        'shelf': '01-10',        # Shelf level (01=bottom)
        'bin': 'A-Z',            # Bin position on shelf

        'example': 'A-12-03-02-B'
    }

    # Picking optimization
    optimization = {
        'fast_movers': 'Zone A, lower shelves, near packing',
        'bulky_items': 'Lower shelves only',
        'small_items': 'Upper shelves OK',
        'slow_movers': 'Zone C, can be higher/further',
        'hazardous': 'Separate zone with special handling'
    }

    return location_format
```

### Slotting Optimization
```python
def optimize_warehouse_slotting(products):
    """
    Assign products to locations based on velocity and characteristics

    Goals:
    1. Minimize travel time for pickers
    2. Maximize space utilization
    3. Group complementary items
    4. Ensure safe and efficient picking
    """

    # Sort by velocity (picks per day)
    products.sort(key=lambda x: x['picks_per_day'], reverse=True)

    # Zone assignment rules
    for product in products:
        if product['picks_per_day'] >= 50:
            product['zone'] = 'A'  # Hot zone
            product['shelf_level'] = 'waist'  # Ergonomic
        elif product['picks_per_day'] >= 10:
            product['zone'] = 'B'  # Medium zone
            product['shelf_level'] = 'any'
        else:
            product['zone'] = 'C'  # Slow zone
            product['shelf_level'] = 'any'

        # Size considerations
        if product['cubic_feet'] > 5:
            product['shelf_level'] = 'bottom'
        if product['weight_lbs'] > 50:
            product['handling'] = 'team_lift'

    return products
```

## KPIs and Performance Tracking

### Essential Inventory KPIs
```python
inventory_kpis = {
    'inventory_accuracy': {
        'formula': '(correct_count / total_count) × 100',
        'target': '95% or higher',
        'frequency': 'Weekly'
    },

    'inventory_turnover': {
        'formula': 'COGS / average_inventory_value',
        'target': '4-6× annually (varies by industry)',
        'frequency': 'Monthly'
    },

    'days_inventory_outstanding': {
        'formula': '365 / inventory_turnover',
        'target': '60-90 days (varies by industry)',
        'frequency': 'Monthly'
    },

    'fill_rate': {
        'formula': '(orders_fulfilled / total_orders) × 100',
        'target': '95% or higher',
        'frequency': 'Daily'
    },

    'stock_out_rate': {
        'formula': '(stock_out_events / total_sku_days) × 100',
        'target': 'Less than 2%',
        'frequency': 'Weekly'
    },

    'carrying_cost': {
        'formula': 'inventory_value × 0.25',
        'components': 'Storage + insurance + obsolescence + capital cost',
        'target': 'Minimize while maintaining service level',
        'frequency': 'Quarterly'
    },

    'dead_stock_percentage': {
        'formula': '(dead_stock_value / total_inventory_value) × 100',
        'dead_stock_definition': 'No sales in 90+ days',
        'target': 'Less than 5%',
        'frequency': 'Monthly'
    },

    'order_accuracy': {
        'formula': '(perfect_orders / total_orders) × 100',
        'perfect_order': 'Correct items, quantity, no damage, on time',
        'target': '99% or higher',
        'frequency': 'Daily'
    }
}
```

This skill provides comprehensive inventory management patterns for e-commerce operations.
