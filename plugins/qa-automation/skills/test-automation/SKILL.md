# Test Automation Skill

**Test execution, coverage analysis, and CI/CD integration**

## Test Execution Strategies

### Fast Feedback
```bash
# Run only changed tests
pytest --testmon

# Parallel execution
pytest -n auto  # Use all CPU cores
npm test -- --maxWorkers=50%
```

### Coverage Enforcement
```bash
# Fail if coverage below threshold
pytest --cov=src --cov-fail-under=80

# Coverage with missing lines
pytest --cov=src --cov-report=term-missing
```

## Flaky Test Detection

### Run Multiple Times
```bash
# pytest-repeat
pytest --count=10 tests/test_checkout.py

# jest
npm test -- --testNamePattern="checkout" --runInBand --verbose --maxWorkers=1
```

### Common Causes
1. **Timing issues**: Add explicit waits
2. **Test order dependency**: Isolate tests
3. **External services**: Mock properly
4. **Random data**: Use fixed seeds
5. **Async operations**: Await properly

## Performance Testing

### Load Testing (Locust)
```python
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def view_homepage(self):
        self.client.get("/")

    @task(3)
    def view_product(self):
        self.client.get("/products/1")
```

### Benchmark Testing (pytest-benchmark)
```python
def test_calculate_performance(benchmark):
    result = benchmark(calculate_total, large_dataset)
    assert result > 0
```

## CI/CD Integration

### GitHub Actions
```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements-test.txt
      - run: pytest --cov=src --cov-report=xml
      - uses: codecov/codecov-action@v3
```

## Test Reporting

### HTML Reports
```bash
# pytest-html
pytest --html=report.html --self-contained-html

# Playwright
playwright test --reporter=html
```

### JUnit XML (for CI)
```bash
pytest --junitxml=results.xml
```

## Best Practices

✅ **Fast Tests**: Unit tests <5s total
✅ **Isolation**: No shared state
✅ **Deterministic**: Same input → same output
✅ **Clear Failures**: Descriptive assertions
✅ **Maintainable**: Easy to update

---

**Version**: 1.0.0
