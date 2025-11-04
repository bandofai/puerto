# Testing Practices

**Comprehensive testing strategies across the stack**

## Testing Pyramid

### Unit Tests (70%)
- Test individual functions/methods
- Fast execution
- No external dependencies
- High coverage of business logic

### Integration Tests (20%)
- Test component interactions
- Database queries
- API endpoints
- Service integrations

### E2E Tests (10%)
- Test user workflows
- Full stack testing
- Browser automation
- Critical paths only

## Frontend Testing

### Component Testing (React)
```tsx
import { render, screen, fireEvent } from '@testing-library/react'
import { Button } from './Button'

describe('Button', () => {
  it('calls onClick when clicked', () => {
    const onClick = jest.fn()
    render(<Button onClick={onClick}>Click me</Button>)

    fireEvent.click(screen.getByText('Click me'))

    expect(onClick).toHaveBeenCalledTimes(1)
  })
})
```

### State Management Testing
```tsx
import { renderHook, act } from '@testing-library/react-hooks'
import { useCounter } from './useCounter'

it('increments counter', () => {
  const { result } = renderHook(() => useCounter())

  act(() => {
    result.current.increment()
  })

  expect(result.current.count).toBe(1)
})
```

### E2E Testing (Playwright)
```typescript
import { test, expect } from '@playwright/test'

test('user can log in', async ({ page }) => {
  await page.goto('/login')
  await page.fill('[name=email]', 'user@example.com')
  await page.fill('[name=password]', 'password123')
  await page.click('button[type=submit]')

  await expect(page).toHaveURL('/dashboard')
  await expect(page.locator('h1')).toContainText('Welcome')
})
```

## Backend Testing

### API Testing
```typescript
import request from 'supertest'
import { app } from './app'

describe('POST /api/users', () => {
  it('creates a new user', async () => {
    const res = await request(app)
      .post('/api/users')
      .send({
        name: 'John Doe',
        email: 'john@example.com'
      })
      .expect(201)

    expect(res.body).toHaveProperty('id')
    expect(res.body.email).toBe('john@example.com')
  })
})
```

### Database Testing
```typescript
beforeEach(async () => {
  await db.migrate.rollback()
  await db.migrate.latest()
  await db.seed.run()
})

afterEach(async () => {
  await db.destroy()
})
```

## Test Best Practices

### AAA Pattern
```typescript
it('example test', () => {
  // Arrange
  const input = { ... }

  // Act
  const result = functionUnderTest(input)

  // Assert
  expect(result).toBe(expected)
})
```

### Test Isolation
- Each test should be independent
- No shared state between tests
- Clean up after each test
- Use beforeEach/afterEach appropriately

### Meaningful Test Names
```typescript
// ❌ BAD
it('works', () => { ... })

// ✅ GOOD
it('returns 404 when user not found', () => { ... })
```

### Mocking
```typescript
jest.mock('./api')

it('handles API errors', async () => {
  api.fetchUser.mockRejectedValue(new Error('Network error'))

  // Test error handling
})
```

## Performance Testing

### Load Testing
- Apache JMeter
- k6
- Artillery

### Stress Testing
- Identify breaking points
- Test recovery
- Monitor resource usage

## Test Coverage

### Coverage Metrics
- Line coverage: 80%+ target
- Branch coverage: 75%+ target
- Function coverage: 90%+ target

### Coverage Tools
- Jest (--coverage)
- Istanbul/nyc
- Codecov/Coveralls

## CI/CD Integration

### GitHub Actions
```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: npm install
      - run: npm test
      - run: npm run test:e2e
```

### Test Stages
1. Lint and type check
2. Unit tests
3. Integration tests
4. Build verification
5. E2E tests (on staging)

## Debugging Tests

- Use `test.only` to isolate
- Add console.logs strategically
- Use debugger statements
- Check test environment setup
- Verify mock implementations

