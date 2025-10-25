# Test Generation Skill

**Comprehensive test creation patterns and best practices**

## Test Pyramid

```
        /\
       /  \     E2E Tests (5-10%)
      /____\    Slow, brittle, expensive
     /      \
    /Integration\ (15-20%)
   /________________\
  /                  \
 /   Unit Tests (70-80%) \ Fast, reliable, cheap
/________________________\
```

## Arrange-Act-Assert (AAA) Pattern

```python
def test_user_registration():
    # Arrange: Set up test data
    user_data = {"email": "test@example.com", "password": "SecurePass123"}

    # Act: Execute the function
    result = register_user(user_data)

    # Assert: Verify the outcome
    assert result.status == "success"
    assert result.user_id is not None
```

## Test Coverage Targets

- **Critical code**: 95%+ (payment, auth, data)
- **Business logic**: 80%+
- **UI components**: 60%+
- **Utilities**: 90%+

## Unit Test Patterns

### Happy Path
```python
def test_calculate_discount_standard():
    """Test standard discount calculation"""
    assert calculate_discount(100, 10) == 90
```

### Edge Cases
```python
def test_calculate_discount_zero():
    """Test zero discount"""
    assert calculate_discount(100, 0) == 100

def test_calculate_discount_full():
    """Test 100% discount"""
    assert calculate_discount(100, 100) == 0
```

### Error Cases
```python
def test_calculate_discount_negative():
    """Test negative discount raises error"""
    with pytest.raises(ValueError, match="Discount must be positive"):
        calculate_discount(100, -10)

def test_calculate_discount_over_100():
    """Test discount over 100% raises error"""
    with pytest.raises(ValueError, match="Discount cannot exceed 100%"):
        calculate_discount(100, 150)
```

## Mocking External Dependencies

### Python (pytest)
```python
from unittest.mock import Mock, patch

@patch('myapp.payment.stripe.charge')
def test_process_payment(mock_charge):
    """Test payment processing with mocked Stripe"""
    mock_charge.return_value = {"id": "ch_123", "status": "succeeded"}

    result = process_payment(amount=100, card="tok_visa")

    assert result["status"] == "succeeded"
    mock_charge.assert_called_once_with(amount=100, card="tok_visa")
```

### JavaScript (jest)
```javascript
import { processPayment } from './payment';
import * as stripe from './stripe';

jest.mock('./stripe');

test('processes payment successfully', async () => {
  stripe.charge.mockResolvedValue({ id: 'ch_123', status: 'succeeded' });

  const result = await processPayment({ amount: 100, card: 'tok_visa' });

  expect(result.status).toBe('succeeded');
  expect(stripe.charge).toHaveBeenCalledWith({ amount: 100, card: 'tok_visa' });
});
```

## Test Data Generation

### Fixtures (pytest)
```python
import pytest

@pytest.fixture
def sample_user():
    """Create sample user for testing"""
    return {
        "id": 1,
        "email": "test@example.com",
        "name": "Test User"
    }

@pytest.fixture
def authenticated_client(sample_user):
    """Create authenticated API client"""
    client = TestClient(app)
    client.headers["Authorization"] = f"Bearer {generate_token(sample_user)}"
    return client
```

### Factory Pattern
```python
from factory import Factory, Faker

class UserFactory(Factory):
    class Meta:
        model = User

    email = Faker('email')
    name = Faker('name')
    age = Faker('random_int', min=18, max=100)

# Usage
user = UserFactory.create()
users = UserFactory.create_batch(10)
```

## Integration Test Patterns

```python
def test_user_registration_integration(db_session):
    """Test user registration with real database"""
    # Arrange
    user_data = {"email": "test@example.com", "password": "SecurePass123"}

    # Act
    response = client.post("/api/register", json=user_data)

    # Assert
    assert response.status_code == 201
    assert response.json()["email"] == user_data["email"]

    # Verify database
    user = db_session.query(User).filter_by(email=user_data["email"]).first()
    assert user is not None
    assert user.email == user_data["email"]
```

## E2E Test Patterns (Playwright)

```javascript
import { test, expect } from '@playwright/test';

test('user can complete checkout', async ({ page }) => {
  // Navigate to site
  await page.goto('https://example.com');

  // Add item to cart
  await page.click('[data-testid="add-to-cart"]');
  await expect(page.locator('.cart-count')).toHaveText('1');

  // Go to checkout
  await page.click('[data-testid="checkout-button"]');
  await expect(page).toHaveURL(/.*checkout/);

  // Fill form
  await page.fill('[name="email"]', 'test@example.com');
  await page.fill('[name="card"]', '4242424242424242');

  // Submit
  await page.click('[data-testid="submit-payment"]');

  // Verify success
  await expect(page.locator('.success-message')).toBeVisible();
});
```

## Test Quality Checklist

✅ **DO**:
- Test behavior, not implementation
- Use descriptive test names
- Keep tests independent
- Mock external dependencies
- Test error cases
- Use fixtures for setup
- Aim for fast tests (<1s)

❌ **DON'T**:
- Test private methods
- Depend on test order
- Use real external APIs
- Hardcode values
- Skip edge cases
- Write flaky tests
- Ignore slow tests

---

**Version**: 1.0.0
**Patterns**: Industry-standard testing
