# QA Automation Plugin

**Comprehensive test generation, automation, and quality assurance**

This plugin provides specialized agents for automated testing, code coverage analysis, and bug reporting.

## Agents

### 1. **test-generator** (Sonnet)
Generates comprehensive test cases and test automation scripts.

**Use when:**
- Creating tests for new features
- Improving test coverage
- Generating E2E test scenarios
- Creating test data

**Capabilities:**
- Unit test generation (pytest, jest, junit)
- Integration test creation
- E2E test scenarios (Playwright, Cypress, Selenium)
- Test data generation
- Mock and fixture creation
- Coverage gap analysis

### 2. **test-runner** (Haiku)
Executes tests and analyzes coverage reports.

**Use when:**
- Running test suites
- Analyzing code coverage
- Identifying flaky tests
- Generating coverage reports
- Performance testing

**Capabilities:**
- Test execution across frameworks
- Coverage analysis (80%+ target)
- Flaky test detection
- Performance profiling
- Parallel test execution
- Test result reporting

### 3. **bug-reporter** (Sonnet)
Creates detailed bug reports with reproduction steps.

**Use when:**
- Documenting test failures
- Creating GitHub issues
- Regression analysis
- Root cause investigation

**Capabilities:**
- Structured bug reports
- Reproduction steps generation
- Screenshot/log attachment
- Severity assessment
- Regression tracking
- GitHub issue creation

## Skills

### 1. **test-generation**
Best practices for creating comprehensive tests:
- Test pyramid (unit, integration, E2E)
- Arrange-Act-Assert pattern
- Test data strategies
- Mock and stub patterns
- Coverage targets

### 2. **test-automation**
Test automation frameworks and patterns:
- pytest (Python)
- jest (JavaScript/TypeScript)
- Playwright/Cypress (E2E)
- Continuous testing in CI/CD
- Flaky test prevention

## Templates

- **pytest template**: Python unit test structure
- **jest template**: JavaScript/TypeScript test setup
- **playwright template**: E2E test framework
- **bug report template**: Standardized issue format

## Quick Start

### Generate Tests
```
User: Generate pytest tests for my FastAPI endpoints

Agent: test-generator
1. Analyzes API code
2. Creates comprehensive test suite
3. Includes happy path and edge cases
4. Generates test data and fixtures
5. Achieves 80%+ coverage
```

### Run Tests
```
User: Run tests and check coverage

Agent: test-runner
1. Executes test suite
2. Analyzes coverage report
3. Identifies uncovered code
4. Reports flaky tests
5. Provides actionable recommendations
```

### Report Bugs
```
User: Create a bug report for the failing login test

Agent: bug-reporter
1. Analyzes test failure
2. Extracts error logs
3. Creates reproduction steps
4. Assesses severity
5. Generates GitHub issue
```

## Best Practices

✓ **Test Pyramid**: 70% unit, 20% integration, 10% E2E
✓ **Coverage Target**: ≥80% for critical code
✓ **Fast Feedback**: Unit tests <5s total
✓ **Isolated Tests**: No dependencies between tests
✓ **Clear Assertions**: Descriptive failure messages

Closes #19

---

**Version**: 1.0.0
**Patterns**: Industry-standard testing practices
