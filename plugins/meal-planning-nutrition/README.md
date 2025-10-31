# Meal Planning & Nutrition Plugin

> Meal planning and nutrition analysis specialist - Weekly meal planning, nutrition tracking, recipe organization, and grocery automation

## Overview

The Meal Planning & Nutrition plugin helps you plan healthy, delicious meals while tracking nutrition goals. It provides intelligent meal planning, nutrition analysis, recipe organization, and automated grocery list generation.

## Features

### Agents

- **meal-planner** (Sonnet): Generate balanced weekly meal plans
- **nutrition-analyzer** (Haiku): Calculate and track nutrition metrics
- **recipe-organizer**: Manage and tag recipe database
- **shopping-list-generator**: Auto-generate grocery lists from meal plans
- **dietary-filter**: Filter recipes by dietary restrictions

### Skills

- **meal-planning**: Meal planning strategies, weekly planning patterns, batch cooking
- **nutrition-analysis**: Macro/micro nutrient calculation, dietary goal tracking
- **recipe-management**: Recipe organization, tagging systems, scaling

## Quick Start

### Installation

```bash
/plugin install meal-planning-nutrition@puerto
```

### Basic Usage

**Generate a meal plan:**
```bash
@meal-planner create weekly-plan --dietary-restriction vegetarian --calories 2000
```

**Analyze nutrition:**
```bash
@nutrition-analyzer calculate --meal "Grilled Chicken Bowl" --ingredients "150g chicken, 200g rice, 100g broccoli"
```

**Generate shopping list:**
```bash
@shopping-list-generator from-meal-plan --week "2025-01-20"
```

## Meal Planning Strategies

### Weekly Planning Workflow

1. **Set dietary goals** (calories, macros, restrictions)
2. **Generate meal plan** (7 days, 3 meals + snacks)
3. **Review and adjust** (swap meals, adjust portions)
4. **Generate shopping list** (organized by store section)
5. **Prep ingredients** (batch cook, prep-ahead)
6. **Track adherence** (log meals, adjust as needed)

### Smart Planning Features

**Leftover Optimization**:
- Make extra dinner → use for next day's lunch
- Batch cook → freeze portions for later
- Repurpose ingredients → reduce waste

**Time Management**:
- Quick weeknight meals (< 30 min)
- Elaborate weekend cooking
- Sunday meal prep sessions

**Variety & Balance**:
- No repeat meals within 3 days
- Different proteins each day
- Seasonal ingredient rotation

## Nutrition Tracking

### Macronutrients

```
Protein: 20-35% of calories (4 cal/gram)
Carbs: 45-65% of calories (4 cal/gram)
Fat: 20-35% of calories (9 cal/gram)
Fiber: 25-30 grams per day
```

### Example Nutrition Analysis

```bash
@nutrition-analyzer analyze-day --date "2025-01-21"

# Output:
Daily Nutrition: January 21, 2025

Calories: 1,950 / 2,000 (98% of target) ✓
Protein: 125g (26%) ✓
Carbs: 245g (50%) ✓
Fat: 52g (24%) ✓
Fiber: 28g (93% of RDA) ✓

Status: On target for all macros
```

## Dietary Restrictions

### Supported Diets

- **Vegetarian**: No meat, fish, poultry
- **Vegan**: No animal products
- **Keto**: < 50g carbs/day, high fat
- **Paleo**: Whole foods, no grains/dairy
- **Mediterranean**: Plant-based, healthy fats
- **Gluten-free**: No wheat, barley, rye
- **Dairy-free**: No milk products
- **Low-FODMAP**: For IBS management

### Custom Restrictions

```json
{
  "allergies": ["peanuts", "shellfish"],
  "dislikes": ["mushrooms", "cilantro"],
  "preferences": ["low-sodium", "organic"],
  "medical": ["diabetic", "heart-healthy"]
}
```

## Use Cases

### Example 1: Vegetarian Meal Plan

```bash
@meal-planner create \
    --dietary-restriction vegetarian \
    --calories 2000 \
    --macro-targets "protein:25%,carbs:50%,fat:25%" \
    --duration 7days

# Output: 7-day vegetarian meal plan
Monday:
  Breakfast: Overnight Oats with Berries (350 cal, 12g protein)
  Lunch: Mediterranean Quinoa Bowl (450 cal, 18g protein)
  Dinner: Vegetarian Chili (500 cal, 22g protein) - make double!
  Snack: Greek Yogurt with Almonds (200 cal, 15g protein)

Tuesday:
  Breakfast: Smoothie Bowl (380 cal, 15g protein)
  Lunch: Leftover Vegetarian Chili
  Dinner: Stir-fry Tofu with Vegetables (480 cal, 24g protein)
  ...
```

### Example 2: Meal Prep Sunday

```bash
@meal-planner batch-cooking-plan --prep-day sunday --servings 4

# Output: Optimized prep plan
Sunday Prep (3 hours):
1. Batch cook brown rice (8 cups) - store in containers
2. Roast vegetables (4 pans) - use throughout week
3. Grill chicken breasts (8 pieces) - portion and freeze
4. Prep overnight oats (5 jars) - Mon-Fri breakfast
5. Chop vegetables for stir-fries - store in bags

Weekly Usage:
- Monday: Use rice + roasted veggies + chicken
- Tuesday: Use rice + stir-fry veggies
- Wednesday: Repeat Monday
...
```

### Example 3: Shopping List

```bash
@shopping-list-generator from-meal-plan --week "2025-01-20" --optimize true

# Output: Organized shopping list
Produce:
- Broccoli (2 lbs)
- Spinach (1 bag)
- Bell peppers (4, mixed colors)
- Bananas (6)
- Berries (2 containers)

Protein:
- Chicken breast (2 lbs)
- Extra firm tofu (2 blocks)
- Greek yogurt (32 oz)
- Eggs (1 dozen)

Grains:
- Brown rice (2 lbs)
- Quinoa (1 lb)
- Whole grain bread (1 loaf)

...

Estimated total: $85
Items: 32
```

## Recipe Database

### Recipe Structure

```json
{
  "name": "Mediterranean Quinoa Bowl",
  "servings": 2,
  "prep_time": 10,
  "cook_time": 15,
  "tags": ["quick", "healthy", "vegetarian", "meal-prep"],
  "ingredients": [
    {"item": "quinoa", "amount": "1 cup", "grams": 180},
    {"item": "chickpeas", "amount": "1 can", "grams": 240},
    {"item": "cucumber", "amount": "1 medium", "grams": 200}
  ],
  "nutrition_per_serving": {
    "calories": 450,
    "protein": 18,
    "carbs": 65,
    "fat": 12,
    "fiber": 12
  },
  "instructions": [
    "Cook quinoa according to package directions",
    "Drain and rinse chickpeas",
    "Dice cucumber and tomatoes",
    "Combine all ingredients and drizzle with dressing"
  ]
}
```

### Recipe Tags

Use tags for easy filtering:

- **Effort**: quick (< 30 min), medium (30-60 min), elaborate (> 60 min)
- **Budget**: budget-friendly, moderate, gourmet
- **Type**: breakfast, lunch, dinner, snack, dessert
- **Diet**: vegetarian, vegan, keto, paleo, gluten-free
- **Season**: spring, summer, fall, winter
- **Occasion**: meal-prep, weeknight, entertaining, holiday

## Nutrition Tips

### Macro Balance

**High Protein**: Builds muscle, satiety
- Target: 0.8-1.2g per lb body weight
- Sources: Chicken, fish, tofu, beans, eggs

**Complex Carbs**: Energy, fiber
- Target: 45-65% of calories
- Sources: Whole grains, vegetables, fruits, legumes

**Healthy Fats**: Hormones, absorption
- Target: 20-35% of calories
- Sources: Nuts, avocado, olive oil, fatty fish

### Micronutrients

Track these key vitamins/minerals:
- **Iron**: Red meat, spinach, lentils
- **Calcium**: Dairy, leafy greens, fortified foods
- **Vitamin D**: Fatty fish, fortified milk, sunlight
- **Vitamin B12**: Animal products, fortified foods
- **Magnesium**: Nuts, whole grains, leafy greens

## Integration

### With Wearables
```bash
# Import calorie burn from fitness tracker
@nutrition-analyzer adjust-targets --activity-calories 500

# Sync nutrition goals with Apple Health
@meal-planner sync --service "apple-health" --direction "bidirectional"
```

### With Recipe Apis
```bash
# Import recipe from URL
@recipe-organizer import --url "https://recipe-site.com/recipe/12345"

# Search recipes online
@recipe-organizer search --query "high protein vegetarian" --source "spoonacular"
```

## Best Practices

### Meal Planning Success

1. **Plan once, eat all week**: Dedicate 30 min Sunday to plan
2. **Batch cook strategically**: Make multiple servings
3. **Embrace leftovers**: Intentionally make extra
4. **Keep it simple**: Don't overcomplicate weeknights
5. **Build a recipe rotation**: 20-30 go-to recipes
6. **Seasonal eating**: Use in-season produce (cheaper, better)

### Nutrition Tracking

1. **Consistency over perfection**: Weekly averages matter more than daily
2. **Weigh food initially**: Develop intuition for portions
3. **Focus on whole foods**: Less tracking needed
4. **Adjust based on results**: Use scale and energy levels as guides
5. **Plan indulgences**: Budget for treats within weekly goals

## Troubleshooting

**Issue**: Meal plan feels repetitive

**Solution**: Expand recipe database and use variety filters
```bash
@meal-planner create --variety "high" --cuisine-rotation true
```

**Issue**: Nutrition goals not being met

**Solution**: Analyze gaps and adjust meal plan
```bash
@nutrition-analyzer identify-gaps --target "protein"
@meal-planner adjust --increase-protein true
```

**Issue**: Shopping list is too expensive

**Solution**: Optimize for budget
```bash
@shopping-list-generator optimize --budget 75 --prioritize-essentials
```

## Data Storage

```
data/
├── meal-plans/          # Weekly meal plans
├── recipes/             # Recipe database
├── shopping-lists/      # Generated lists
├── nutrition-logs/      # Daily nutrition tracking
└── preferences/         # Dietary preferences and goals
```

## License

MIT

## Support

For issues and questions:
- GitHub Issues: https://github.com/bandofai/puerto/issues

---

**Remember**: Meal planning should reduce stress, not create it. Start simple, find what works for you, and adjust over time.
