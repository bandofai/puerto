# Shopping Optimization Skill

**Expert patterns for intelligent grocery list management, store route optimization, and price comparison**

This skill codifies best practices for shopping list optimization, pantry management, store navigation efficiency, and multi-store price comparison strategies.

---

## Core Philosophy

**Smart shopping saves time, money, and reduces waste.**

Effective shopping optimization should:
- Minimize shopping time through efficient routing
- Maximize savings through strategic price comparison
- Reduce food waste via pantry tracking
- Integrate seamlessly with meal planning
- Adapt to individual preferences and constraints

---

## Part 1: Shopping List Organization

### 1.1 Recipe-to-Ingredients Conversion

**Ingredient extraction patterns**:

```markdown
# Recipe Format Recognition

## Markdown recipes
### Ingredients
- 2 cups all-purpose flour
- 1/2 cup sugar
- 3 large eggs

## JSON recipes
{
  "ingredients": [
    {"item": "flour", "quantity": 2, "unit": "cups", "type": "all-purpose"},
    {"item": "sugar", "quantity": 0.5, "unit": "cup"}
  ]
}

## Plain text
Ingredients:
2 cups flour
1/2 cup sugar
3 eggs
```

**Normalization rules**:
- Convert fractions to decimals (1/2 → 0.5)
- Standardize units (tbsp, tsp, cups, oz, lbs, g, kg)
- Remove descriptors but preserve types (e.g., "all-purpose flour" → "flour, all-purpose")
- Handle ranges by using maximum (1-2 cups → 2 cups)
- Interpret "to taste" as optional

**Quantity consolidation**:
```
Recipe 1: 1 cup milk
Recipe 2: 2 cups milk
Recipe 3: 1 pint milk (= 2 cups)
Total: 5 cups = 1.25 quarts
Round up: 2 quarts (safer to have extra)
```

### 1.2 Pantry Deduplication

**Inventory matching algorithm**:
1. Load current pantry inventory
2. Normalize ingredient names (fuzzy matching)
3. Compare required quantity vs. available stock
4. Calculate deficit
5. Add only what's needed to shopping list
6. Update projected pantry levels

**Example deduplication**:
```
Recipe needs: 3 cups flour
Pantry has: 1.5 cups flour
Add to list: 2 cups flour (round up to ensure sufficient)

Recipe needs: 2 cans tomato sauce
Pantry has: 2 cans tomato sauce
Add to list: NONE (already stocked)
```

**Fuzzy matching for variations**:
```
Recipe: "whole milk" → Match: "milk" (if marked as whole)
Recipe: "Roma tomatoes" → Match: "tomatoes"
Recipe: "extra virgin olive oil" → Match: "olive oil"
```

### 1.3 Recurring Items Management

**Frequency-based auto-add**:

```json
{
  "recurring_items": [
    {
      "item": "milk",
      "quantity": "1 gallon",
      "frequency": "weekly",
      "last_purchased": "2025-10-14",
      "auto_add": true,
      "min_stock": "0.5 gallons"
    },
    {
      "item": "eggs",
      "quantity": "1 dozen",
      "frequency": "biweekly",
      "last_purchased": "2025-10-07",
      "auto_add": true
    },
    {
      "item": "coffee",
      "quantity": "1 lb",
      "frequency": "monthly",
      "last_purchased": "2025-09-25",
      "auto_add": true
    }
  ]
}
```

**Auto-add logic**:
```python
def should_add_recurring_item(item):
    days_since_purchase = (today - item.last_purchased).days

    if item.frequency == "weekly" and days_since_purchase >= 7:
        return True
    elif item.frequency == "biweekly" and days_since_purchase >= 14:
        return True
    elif item.frequency == "monthly" and days_since_purchase >= 30:
        return True

    return False
```

**Consumption-based prediction**:
```
Item: Milk
Average consumption: 1 gallon per week
Current stock: 0.25 gallons
Days until next shop: 3 days
Predicted need: 1 gallon (will run out before next shop)
Action: Add to list
```

### 1.4 Category Organization

**Standard category order** (optimized for typical store layout):

```
1. Produce (perishable, entrance area)
2. Bakery (fresh goods, minimal handling)
3. Meat & Seafood (protein, bottom of cart)
4. Deli (prepared items)
5. Dairy (perimeter, refrigerated)
6. Frozen (absolute last, temperature-sensitive)
7. Pantry Staples (center aisles - dry goods)
8. Snacks (packaged, won't crush)
9. Beverages (heavy, stable)
10. Household (cleaning, paper goods)
11. Personal Care (toiletries, health)
12. Other (miscellaneous)
```

**Item-to-category mapping**:
```json
{
  "category_mapping": {
    "produce": ["apples", "bananas", "spinach", "tomatoes", "onions"],
    "bakery": ["bread", "bagels", "muffins", "croissants"],
    "meat": ["chicken", "beef", "pork", "fish", "turkey"],
    "dairy": ["milk", "cheese", "yogurt", "butter", "cream"],
    "frozen": ["ice cream", "frozen vegetables", "frozen pizza"],
    "pantry": ["pasta", "rice", "canned goods", "flour", "sugar"],
    "snacks": ["chips", "crackers", "cookies", "nuts"],
    "beverages": ["juice", "soda", "water", "coffee", "tea"],
    "household": ["paper towels", "dish soap", "laundry detergent"],
    "personal_care": ["shampoo", "toothpaste", "soap", "deodorant"]
  }
}
```

---

## Part 2: Store Layout Optimization

### 2.1 Layout Pattern Recognition

**Common store layout types**:

**Linear/Racetrack Layout** (Whole Foods, Trader Joe's):
```
[Entrance]
    |
[Produce]---[Bakery]
    |           |
[Meat]------[Deli]
    |           |
[Pantry Aisles]
    |           |
[Dairy]----[Frozen]
    |
[Checkout]
```

**Grid Layout** (Walmart, Target):
```
[Entrance]
    |
[Produce][Aisle 1][Aisle 2][Aisle 3]...[Dairy]
         [Aisle 4][Aisle 5][Aisle 6]...[Frozen]
         [Aisle 7][Aisle 8][Aisle 9]...[Meat]
    |
[Checkout]
```

**Boutique Layout** (Specialty stores):
```
[Irregular sections, custom routing required]
```

### 2.2 Efficient Path Planning

**Core optimization principles**:

1. **No backtracking**: Visit each section once
2. **Temperature zones**: Frozen/refrigerated last
3. **Fragile first (then protected)**: Produce early, eggs on top
4. **Heavy late**: Minimize carrying time
5. **Perimeter then center**: Most efficient for linear layouts

**Optimized routing algorithm**:

```python
def optimize_route(shopping_list, store_layout):
    """
    Returns optimized shopping route
    """
    # Step 1: Group items by section
    sections = group_by_section(shopping_list, store_layout)

    # Step 2: Order sections by store layout
    if store_layout.type == "linear":
        # Perimeter first, then aisles, frozen last
        route = [
            sections.get("bakery", []),
            sections.get("meat", []),
            sections.get("deli", []),
            sections.get("produce", []),
            *sections.get("aisles", []),  # sorted by aisle number
            sections.get("dairy", []),
            sections.get("frozen", [])
        ]
    elif store_layout.type == "grid":
        # Serpentine through aisles
        route = serpentine_aisles(sections, store_layout)

    # Step 3: Add navigation instructions
    return add_navigation(route, store_layout)
```

**Example optimization**:

```
Shopping list (unoptimized order):
1. Ice cream (frozen)
2. Bread (bakery)
3. Milk (dairy)
4. Bananas (produce)
5. Pasta (pantry aisle 3)
6. Chicken (meat)

Optimized route:
1. Bakery: Bread
2. Meat: Chicken
3. Produce: Bananas
4. Pantry Aisle 3: Pasta
5. Dairy: Milk
6. Frozen: Ice cream (LAST)

Distance savings: 45%
Time savings: 38%
```

### 2.3 Cart Loading Strategy

**Bottom of cart** (heaviest, most stable):
- Beverages (gallons, cases)
- Canned goods
- Boxed items (cereal, pasta)
- Heavy produce (melons, potatoes)

**Middle of cart**:
- Medium-weight items
- Packaged goods
- Moderately fragile items

**Top/Child seat**:
- Bread (visible, won't get crushed)
- Eggs (careful handling, won't forget)
- Delicate produce (berries, herbs)
- Small items

**Separate basket** (if available):
- Fresh produce (prevent bruising)
- Items for different households
- Returns

### 2.4 Multi-Store Strategy

**Single store vs. multi-store decision matrix**:

```
Consider SINGLE store when:
✓ Time is limited
✓ Savings differential < 15%
✓ All items available at one location
✓ Convenience is priority
✓ Extra driving > 3 miles total

Consider MULTI-STORE when:
✓ Savings differential > 25%
✓ Time is flexible
✓ Stores are close together (< 2 miles)
✓ Specialty items only at certain stores
✓ Bulk purchases justify trip
```

**Multi-store optimization**:
```
Store A: Items 1-8 (closest to home)
Store B: Items 9-15 (on the way, better prices)
Store C: Items 16-20 (specialty items only here)

Route optimization:
Home → Store A → Store B → Store C → Home
Total distance: 8.5 miles
Total time: 75 minutes
Total savings: $32.50
Cost per saved dollar: 2.3 minutes
```

---

## Part 3: Price Comparison Frameworks

### 3.1 Unit Price Calculation

**Standard unit price formula**:
```
Unit Price = Total Price / Quantity in Standard Units
```

**Common conversions**:
```
Volume:
- 1 gallon = 128 fl oz
- 1 quart = 32 fl oz
- 1 pint = 16 fl oz
- 1 cup = 8 fl oz

Weight:
- 1 lb = 16 oz
- 1 kg = 1000 g = 2.2 lbs

Count:
- 1 dozen = 12 units
```

**Example calculations**:
```
Product A: $3.99 for 16 oz
Unit price: $3.99 / 16 oz = $0.249/oz

Product B: $5.49 for 24 oz
Unit price: $5.49 / 24 oz = $0.229/oz

Best value: Product B (saves $0.02/oz = 8% savings)
```

### 3.2 Sale Evaluation

**True savings calculation**:

```python
def calculate_true_savings(item):
    regular_price = item.regular_price
    sale_price = item.sale_price

    # Apply promotions
    if item.promotion == "BOGO":
        effective_price = sale_price / 2
    elif item.promotion == "BOGO 50%":
        effective_price = sale_price * 0.75  # avg of full + half
    elif item.digital_coupon:
        effective_price = sale_price - item.digital_coupon
    else:
        effective_price = sale_price

    savings = regular_price - effective_price
    savings_percent = (savings / regular_price) * 100

    return savings, savings_percent
```

**Stock-up thresholds**:
```
Savings > 40%: STOCK UP (if storage allows)
Savings 25-40%: Buy extra (within reason)
Savings 15-25%: Good deal, buy as needed
Savings < 15%: Normal pricing, no rush
```

### 3.3 Price History Tracking

**Trend analysis**:

```json
{
  "item": "chicken_breast",
  "store": "safeway",
  "price_history": [
    {"date": "2025-10-01", "price": 8.99},
    {"date": "2025-10-08", "price": 8.99},
    {"date": "2025-10-15", "price": 5.99, "sale": true},
    {"date": "2025-10-21", "price": 8.99}
  ],
  "avg_30day": 7.74,
  "avg_90day": 8.24,
  "typical_sale_price": 5.99,
  "sale_frequency": "every 3-4 weeks"
}
```

**Buy-now vs. wait recommendations**:
```
Current price > 30-day avg: Consider waiting
Current price < 30-day avg: Good time to buy
Current price ≤ typical sale price: EXCELLENT time to stock up
```

### 3.4 Total Savings Optimization

**Comprehensive savings calculation**:

```
Base cost (premium store): $150.00

Single-store optimization:
- Switch to value store: $115.00
- Savings: $35.00 (23%)
- Time: 40 minutes
- Convenience: High

Multi-store optimization:
- Store A (bulk items): $65.00
- Store B (produce): $28.00
- Store C (specialty): $18.00
- Subtotal: $111.00
- Savings: $39.00 (26%)
- Gas cost: $3.50
- Net savings: $35.50
- Time: 75 minutes
- Convenience: Medium

With coupons/loyalty:
- Digital coupons: -$8.00
- Loyalty discounts: -$5.00
- Total: $98.00
- Total savings: $52.00 (35%)
- Extra time for coupons: +10 minutes
```

**ROI calculation**:
```
Time investment: 45 minutes (list building + coupon clipping)
Savings: $52.00
Hourly rate: $69/hour

Worth it if your time value < $69/hour
```

---

## Part 4: Pantry Management Best Practices

### 4.1 Inventory Tracking

**Pantry organization system**:

```json
{
  "pantry_id": "home-kitchen",
  "last_updated": "2025-10-21",
  "categories": [
    {
      "category": "grains",
      "items": [
        {
          "item": "white rice",
          "quantity": 3,
          "unit": "lbs",
          "location": "shelf-2",
          "expiration": "2026-08-15",
          "min_stock": 2,
          "status": "adequate"
        },
        {
          "item": "pasta",
          "quantity": 4,
          "unit": "boxes",
          "location": "shelf-2",
          "expiration": "2026-12-31",
          "min_stock": 2,
          "status": "well-stocked"
        }
      ]
    },
    {
      "category": "canned_goods",
      "items": [
        {
          "item": "diced tomatoes",
          "quantity": 1,
          "unit": "cans",
          "location": "shelf-3",
          "expiration": "2026-03-15",
          "min_stock": 3,
          "status": "low"
        }
      ]
    }
  ]
}
```

**Stock level alerts**:
```
Well-stocked: Quantity ≥ min_stock * 1.5
Adequate: Quantity ≥ min_stock
Low: Quantity < min_stock
Out: Quantity = 0
```

### 4.2 Expiration Management

**FIFO (First In, First Out) tracking**:

```json
{
  "item": "milk",
  "containers": [
    {"purchase_date": "2025-10-15", "expiration": "2025-10-29", "opened": false},
    {"purchase_date": "2025-10-18", "expiration": "2025-11-01", "opened": false}
  ],
  "use_order": [
    {"container": 1, "use_by": "2025-10-29"},
    {"container": 2, "use_by": "2025-11-01"}
  ]
}
```

**Expiration alerts**:
```
Expires in 1-3 days: USE IMMEDIATELY
Expires in 4-7 days: Plan meals around this
Expires in 8-14 days: Normal usage
Expires in 15+ days: Good stock
```

### 4.3 Waste Reduction

**Meal planning integration**:

```
Step 1: Check pantry inventory
Step 2: Identify items expiring soon
Step 3: Plan meals using those items
Step 4: Generate shopping list for remaining needs
Step 5: Update pantry after shopping

Example:
- Chicken expires in 3 days → Plan chicken dinner for Tuesday
- Spinach expires in 4 days → Plan salad for Wednesday
- Yogurt expires in 5 days → Plan breakfast parfaits
```

**Leftover management**:
```json
{
  "leftover_id": "lasagna-20251020",
  "meal": "lasagna",
  "date_cooked": "2025-10-20",
  "portions": 3,
  "location": "fridge-shelf-2",
  "consume_by": "2025-10-24",
  "reheating_instructions": "350°F for 20 minutes"
}
```

---

## Part 5: Meal Planning Integration

### 5.1 Week-Ahead Planning

**Weekly meal plan structure**:

```json
{
  "week": "2025-10-21 to 2025-10-27",
  "meals": [
    {
      "day": "Monday",
      "breakfast": "Oatmeal with berries",
      "lunch": "Leftover lasagna",
      "dinner": {
        "recipe": "Grilled chicken with roasted vegetables",
        "servings": 4,
        "ingredients": [
          {"item": "chicken breast", "quantity": 1.5, "unit": "lbs"},
          {"item": "broccoli", "quantity": 1, "unit": "bunch"},
          {"item": "carrots", "quantity": 4, "unit": "count"}
        ]
      }
    },
    {
      "day": "Tuesday",
      "breakfast": "Yogurt parfait",
      "lunch": "Sandwich",
      "dinner": {
        "recipe": "Pasta with marinara",
        "servings": 4,
        "ingredients": [
          {"item": "pasta", "quantity": 1, "unit": "box"},
          {"item": "marinara sauce", "quantity": 1, "unit": "jar"}
        ]
      }
    }
  ]
}
```

**Consolidated shopping list generation**:

```python
def generate_weekly_shopping_list(meal_plan, pantry_inventory):
    all_ingredients = []

    # Extract all ingredients from meal plan
    for day in meal_plan.meals:
        for meal in [day.breakfast, day.lunch, day.dinner]:
            if hasattr(meal, 'ingredients'):
                all_ingredients.extend(meal.ingredients)

    # Consolidate duplicates
    consolidated = consolidate_ingredients(all_ingredients)

    # Deduplicate against pantry
    shopping_list = deduplicate_pantry(consolidated, pantry_inventory)

    # Add recurring items
    shopping_list.extend(get_recurring_items())

    return shopping_list
```

### 5.2 Flexible Substitutions

**Substitution mapping**:

```json
{
  "substitutions": [
    {
      "original": "ground beef",
      "alternatives": [
        {"item": "ground turkey", "ratio": "1:1", "note": "Leaner option"},
        {"item": "ground chicken", "ratio": "1:1", "note": "Lighter flavor"},
        {"item": "lentils", "ratio": "1:1", "note": "Vegetarian"}
      ]
    },
    {
      "original": "all-purpose flour",
      "alternatives": [
        {"item": "whole wheat flour", "ratio": "1:1", "note": "More fiber"},
        {"item": "almond flour", "ratio": "1:1.25", "note": "Gluten-free, adjust liquid"}
      ]
    }
  ]
}
```

**Smart substitution logic**:
```
If item not available:
1. Check for acceptable substitutes
2. Verify dietary restrictions
3. Adjust quantities if needed
4. Update recipe instructions
5. Note substitution in meal plan
```

---

## Part 6: Recurring Item Algorithms

### 6.1 Consumption Prediction

**Usage tracking**:

```json
{
  "item": "coffee",
  "tracking_period": "90 days",
  "purchases": [
    {"date": "2025-07-25", "quantity": 1, "unit": "lb"},
    {"date": "2025-08-22", "quantity": 1, "unit": "lb"},
    {"date": "2025-09-19", "quantity": 1, "unit": "lb"}
  ],
  "average_consumption": {
    "quantity": 1,
    "unit": "lb",
    "period": "28 days"
  },
  "predicted_next_purchase": "2025-10-17",
  "confidence": 0.85
}
```

**Predictive auto-add**:

```python
def predict_reorder_date(item):
    avg_days_between_purchases = calculate_average_interval(item.purchases)
    last_purchase_date = item.purchases[-1].date
    predicted_date = last_purchase_date + avg_days_between_purchases

    # Add buffer for safety (10% of interval)
    buffer = avg_days_between_purchases * 0.10
    reorder_date = predicted_date - buffer

    return reorder_date

def should_reorder_now(item, next_shopping_date):
    predicted_reorder = predict_reorder_date(item)

    # Reorder if we'll run out before next planned shop
    return next_shopping_date >= predicted_reorder
```

### 6.2 Seasonal Adjustments

**Seasonal consumption patterns**:

```json
{
  "item": "ice cream",
  "seasonal_factors": [
    {"season": "winter", "multiplier": 0.6},
    {"season": "spring", "multiplier": 0.9},
    {"season": "summer", "multiplier": 1.5},
    {"season": "fall", "multiplier": 0.8}
  ],
  "base_frequency": "biweekly",
  "adjusted_frequency": {
    "winter": "monthly",
    "spring": "biweekly",
    "summer": "weekly",
    "fall": "biweekly"
  }
}
```

---

## Part 7: Quality Standards

### 7.1 List Building Quality

**Checklist**:
- [ ] All recipe ingredients extracted
- [ ] Quantities normalized to standard units
- [ ] Duplicates consolidated
- [ ] Pantry deduplication applied
- [ ] Recurring items evaluated and added
- [ ] Items categorized correctly
- [ ] Priority items flagged
- [ ] Special dietary needs noted

### 7.2 Route Optimization Quality

**Checklist**:
- [ ] Store layout loaded and validated
- [ ] Route minimizes backtracking
- [ ] Temperature-sensitive items ordered last
- [ ] Fragile items protected
- [ ] Heavy items loaded strategically
- [ ] Navigation instructions clear
- [ ] Time estimate provided
- [ ] Distance calculation included

### 7.3 Price Comparison Quality

**Checklist**:
- [ ] Current prices retrieved
- [ ] Unit prices calculated
- [ ] Sales and promotions applied
- [ ] Multi-store analysis complete
- [ ] Travel costs factored
- [ ] Time value considered
- [ ] Savings accurately calculated
- [ ] Recommendations justified

---

## Part 8: Edge Cases

### 8.1 Missing Data Scenarios

**No pantry inventory**:
- Skip deduplication step
- Generate full list from recipes
- Suggest pantry tracking
- Warn about potential over-purchasing

**No store layout**:
- Use standard category order
- Provide basic grouping
- Suggest creating layout
- Warn about suboptimal routing

**No price data**:
- Proceed with list building
- Skip price comparison
- Suggest price tracking
- Enable future optimizations

### 8.2 Unusual Items

**Specialty items**:
- Mark as "specialty store required"
- Note where available
- Suggest alternatives if needed
- Factor into multi-store routing

**Seasonal unavailability**:
- Flag seasonal items
- Suggest in-season alternatives
- Note typical availability dates
- Update meal plan if needed

**Bulk items**:
- Calculate unit price advantage
- Consider storage capacity
- Evaluate expiration timeline
- Recommend based on consumption rate

---

## Summary: Complete Shopping Optimization Workflow

```
1. MEAL PLANNING
   ↓
2. INGREDIENT EXTRACTION
   ↓
3. PANTRY DEDUPLICATION
   ↓
4. RECURRING ITEMS CHECK
   ↓
5. LIST ORGANIZATION
   ↓
6. PRICE COMPARISON (optional)
   ↓
7. STORE SELECTION
   ↓
8. ROUTE OPTIMIZATION
   ↓
9. SHOPPING EXECUTION
   ↓
10. PANTRY UPDATE
```

**Success metrics**:
- Time saved: 30-40% through optimized routing
- Money saved: 20-30% through price optimization
- Waste reduced: 50% through pantry management
- Convenience: Single workflow from meal plan to shopping

---

## Version History

**Version**: 1.0
**Last Updated**: October 2025
**Author**: Shopping List Optimizer Plugin Team
**Status**: Production Ready

---

## Usage Notes

This skill should be read by ALL shopping optimization agents before performing their specialized tasks. It provides the foundational patterns that ensure consistent, high-quality output across list building, route optimization, and price comparison.

When creating shopping-related outputs, always:
1. Read this skill first
2. Apply relevant patterns
3. Follow quality standards
4. Handle edge cases gracefully
5. Provide clear, actionable outputs
