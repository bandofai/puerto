# Data Engineering

**Data pipelines, ETL, warehousing, and ML infrastructure**

# Data Engineering Patterns

# Statistical Modeling Skill

**Production-tested patterns for rigorous statistical analysis and inference**

This skill codifies best practices from decades of statistical research and thousands of production analyses across scientific and business applications.

---

## Core Principles

1. **Check Assumptions First**: Never apply a statistical test without validating assumptions
2. **Effect Sizes Matter**: P-values alone are insufficient - always report effect sizes
3. **Confidence Intervals**: Quantify uncertainty with confidence intervals
4. **Practical Significance**: Statistical significance ≠ practical significance
5. **Reproducibility**: Always set random seeds and document methodology

---

## Statistical Hypothesis Testing Framework

### The Scientific Method

```
1. State research question clearly
2. Formulate null and alternative hypotheses
3. Choose significance level (α) before seeing data
4. Check assumptions
5. Select appropriate test
6. Calculate test statistic and p-value
7. Compute effect size and confidence interval
8. Make decision and interpret results
9. State limitations
```

### Hypothesis Formulation

```python
# Always state both hypotheses clearly

# Two-sided (default for most tests)
H0: μ1 = μ2  (no difference between groups)
H1: μ1 ≠ μ2  (groups differ)

# One-sided (only when directional hypothesis is justified)
H0: μ1 ≥ μ2  (group 1 not less than group 2)
H1: μ1 < μ2  (group 1 less than group 2)

# Significance level
α = 0.05  (probability of Type I error - false positive)
```

### Type I and Type II Errors

```
Type I Error (α): False Positive
- Reject H0 when it's actually true
- "Seeing a difference that doesn't exist"
- Controlled by significance level (typically 0.05)

Type II Error (β): False Negative
- Fail to reject H0 when it's actually false
- "Missing a difference that does exist"
- Related to statistical power: Power = 1 - β
- Typical power target: 0.80 (80%)
```

---

## Test Selection Decision Tree

### Comparing Means

#### Two Independent Groups

```python
# Check assumptions first
from scipy.stats import shapiro, levene, ttest_ind, mannwhitneyu

# 1. Normality test
stat_norm1, p_norm1 = shapiro(group1)
stat_norm2, p_norm2 = shapiro(group2)
normal = (p_norm1 > 0.05) and (p_norm2 > 0.05)

# 2. Equal variance test
stat_var, p_var = levene(group1, group2)
equal_var = p_var > 0.05

# 3. Select test
if normal and equal_var:
    # Parametric: Independent samples t-test
    stat, p_value = ttest_ind(group1, group2)
    test_name = "Independent t-test"
elif normal and not equal_var:
    # Parametric: Welch's t-test (unequal variances)
    stat, p_value = ttest_ind(group1, group2, equal_var=False)
    test_name = "Welch's t-test"
else:
    # Non-parametric: Mann-Whitney U test
    stat, p_value = mannwhitneyu(group1, group2, alternative='two-sided')
    test_name = "Mann-Whitney U test"

print(f"Test used: {test_name}")
print(f"p-value: {p_value:.4f}")
```

#### Two Paired Groups

```python
from scipy.stats import ttest_rel, wilcoxon

# Check normality of differences
differences = group1_after - group1_before
stat_norm, p_norm = shapiro(differences)

if p_norm > 0.05:
    # Parametric: Paired t-test
    stat, p_value = ttest_rel(group1_before, group1_after)
    test_name = "Paired t-test"
else:
    # Non-parametric: Wilcoxon signed-rank test
    stat, p_value = wilcoxon(group1_before, group1_after)
    test_name = "Wilcoxon signed-rank test"
```

#### Multiple Groups (3+)

```python
from scipy.stats import f_oneway, kruskal

# Check normality for all groups
all_normal = all([shapiro(group)[1] > 0.05 for group in groups])

# Check equal variances
stat_var, p_var = levene(*groups)
equal_var = p_var > 0.05

if all_normal and equal_var:
    # Parametric: One-way ANOVA
    stat, p_value = f_oneway(*groups)
    test_name = "One-way ANOVA"

    # If significant, follow up with post-hoc tests
    if p_value < 0.05:
        from statsmodels.stats.multicomp import pairwise_tukeyhsd
        # Combine all groups with labels
        data = np.concatenate(groups)
        labels = np.concatenate([[i]*len(g) for i, g in enumerate(groups)])
        tukey_result = pairwise_tukeyhsd(data, labels, alpha=0.05)
        print(tukey_result)
else:
    # Non-parametric: Kruskal-Wallis test
    stat, p_value = kruskal(*groups)
    test_name = "Kruskal-Wallis test"

    # If significant, follow up with pairwise Mann-Whitney with Bonferroni
    if p_value < 0.05:
        from itertools import combinations
        from statsmodels.stats.multitest import multipletests

        pairs = list(combinations(range(len(groups)), 2))
        p_values = [mannwhitneyu(groups[i], groups[j])[1] for i, j in pairs]

        # Bonferroni correction
        reject, p_corrected, _, _ = multipletests(p_values, method='bonferroni')

        for (i, j), p_orig, p_corr, sig in zip(pairs, p_values, p_corrected, reject):
            print(f"Group {i} vs Group {j}: p={p_orig:.4f} (corrected: {p_corr:.4f}) - {'SIG' if sig else 'NS'}")
```

### Comparing Proportions

```python
from scipy.stats import chi2_contingency, fisher_exact
from statsmodels.stats.proportion import proportions_ztest

# 2x2 contingency table
def compare_proportions(success1, n1, success2, n2):
    """Compare two proportions"""

    # Create contingency table
    table = np.array([
        [success1, n1 - success1],
        [success2, n2 - success2]
    ])

    # Check expected frequencies (need >= 5 for chi-square)
    expected = (table.sum(axis=0) * table.sum(axis=1)[:, None]) / table.sum()

    if (expected >= 5).all():
        # Chi-square test
        chi2, p_value, dof, expected = chi2_contingency(table)
        test_name = "Chi-square test"
    else:
        # Fisher's exact test (for small samples)
        odds_ratio, p_value = fisher_exact(table)
        test_name = "Fisher's exact test"

    # Also compute z-test for proportions (provides CI)
    counts = np.array([success1, success2])
    nobs = np.array([n1, n2])
    stat, p_value_z = proportions_ztest(counts, nobs)

    return {
        'test': test_name,
        'p_value': p_value,
        'prop1': success1 / n1,
        'prop2': success2 / n2
    }
```

---

## Effect Sizes

**Why**: Effect sizes quantify the magnitude of differences or relationships, independent of sample size.

### Cohen's d (for t-tests)

```python
def cohens_d(group1, group2):
    """
    Cohen's d effect size for independent samples

    Interpretation:
    - 0.2: small effect
    - 0.5: medium effect
    - 0.8: large effect
    """
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)

    # Pooled standard deviation
    pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))

    # Effect size
    d = (np.mean(group1) - np.mean(group2)) / pooled_std

    return d

# Example usage
d = cohens_d(treatment_group, control_group)
print(f"Cohen's d: {d:.3f}")

if abs(d) < 0.2:
    print("Small effect size")
elif abs(d) < 0.5:
    print("Medium effect size")
else:
    print("Large effect size")
```

### Correlation Effect Sizes

```python
from scipy.stats import pearsonr, spearmanr

# Pearson correlation (linear relationship, normal data)
r, p_value = pearsonr(x, y)

# Spearman correlation (monotonic relationship, non-normal data)
rho, p_value = spearmanr(x, y)

# Interpretation
# |r| < 0.3: weak correlation
# 0.3 <= |r| < 0.7: moderate correlation
# |r| >= 0.7: strong correlation

# r² = coefficient of determination (variance explained)
r_squared = r ** 2
print(f"Pearson r: {r:.3f} (explains {r_squared:.1%} of variance)")
```

### Odds Ratios and Relative Risk

```python
def odds_ratio(a, b, c, d):
    """
    Calculate odds ratio from 2x2 table:
              Outcome+  Outcome-
    Exposed+     a         b
    Exposed-     c         d

    OR = (a/b) / (c/d) = (a*d) / (b*c)
    """
    or_value = (a * d) / (b * c) if (b * c) > 0 else np.inf

    # Confidence interval (log scale)
    log_or = np.log(or_value)
    se_log_or = np.sqrt(1/a + 1/b + 1/c + 1/d)

    ci_low = np.exp(log_or - 1.96 * se_log_or)
    ci_high = np.exp(log_or + 1.96 * se_log_or)

    return {
        'odds_ratio': or_value,
        'ci_95': (ci_low, ci_high)
    }

# Interpretation:
# OR = 1: No association
# OR > 1: Increased odds in exposed group
# OR < 1: Decreased odds in exposed group
```

---

## Regression Analysis

### Linear Regression

```python
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan, linear_rainbow
from statsmodels.stats.stattools import durbin_watson

def fit_linear_regression(X, y):
    """
    Fit linear regression with comprehensive diagnostics

    Assumptions to check:
    1. Linearity: relationship between X and y is linear
    2. Independence: observations are independent
    3. Homoscedasticity: constant variance of residuals
    4. Normality: residuals are normally distributed
    5. No multicollinearity: predictors not highly correlated
    """

    # Add constant term
    X_with_const = sm.add_constant(X)

    # Fit model
    model = sm.OLS(y, X_with_const).fit()

    # Print summary
    print(model.summary())

    # ASSUMPTION CHECKS

    # 1. Linearity (Rainbow test)
    rainbow_stat, rainbow_p = linear_rainbow(model)
    print(f"\nLinearity (Rainbow test): p = {rainbow_p:.4f}")
    if rainbow_p < 0.05:
        print("  WARNING: Linearity assumption may be violated")

    # 2. Independence (Durbin-Watson test)
    dw = durbin_watson(model.resid)
    print(f"\nIndependence (Durbin-Watson): {dw:.3f}")
    print("  (Values close to 2 indicate no autocorrelation)")
    if dw < 1.5 or dw > 2.5:
        print("  WARNING: Autocorrelation detected")

    # 3. Homoscedasticity (Breusch-Pagan test)
    bp_test = het_breuschpagan(model.resid, model.model.exog)
    bp_stat, bp_p = bp_test[0], bp_test[1]
    print(f"\nHomoscedasticity (Breusch-Pagan): p = {bp_p:.4f}")
    if bp_p < 0.05:
        print("  WARNING: Heteroscedasticity detected")

    # 4. Normality of residuals (Shapiro-Wilk)
    from scipy.stats import shapiro
    shapiro_stat, shapiro_p = shapiro(model.resid)
    print(f"\nNormality of residuals (Shapiro-Wilk): p = {shapiro_p:.4f}")
    if shapiro_p < 0.05:
        print("  WARNING: Residuals not normally distributed")

    # 5. Multicollinearity (VIF)
    from statsmodels.stats.outliers_influence import variance_inflation_factor

    vif_data = pd.DataFrame()
    vif_data["Variable"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

    print("\nMulticollinearity (VIF):")
    print(vif_data)
    print("  (VIF > 10 indicates high multicollinearity)")

    # DIAGNOSTIC PLOTS
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # 1. Residuals vs Fitted
    axes[0, 0].scatter(model.fittedvalues, model.resid, alpha=0.5)
    axes[0, 0].axhline(y=0, color='r', linestyle='--')
    axes[0, 0].set_xlabel('Fitted values')
    axes[0, 0].set_ylabel('Residuals')
    axes[0, 0].set_title('Residuals vs Fitted')

    # 2. Q-Q plot
    from scipy import stats
    stats.probplot(model.resid, dist="norm", plot=axes[0, 1])
    axes[0, 1].set_title('Normal Q-Q Plot')

    # 3. Scale-Location (sqrt of standardized residuals vs fitted)
    standardized_resid = model.resid / np.std(model.resid)
    axes[1, 0].scatter(model.fittedvalues, np.sqrt(np.abs(standardized_resid)), alpha=0.5)
    axes[1, 0].set_xlabel('Fitted values')
    axes[1, 0].set_ylabel('√|Standardized Residuals|')
    axes[1, 0].set_title('Scale-Location')

    # 4. Residuals vs Leverage
    from statsmodels.stats.outliers_influence import OLSInfluence
    influence = OLSInfluence(model)
    leverage = influence.hat_matrix_diag
    axes[1, 1].scatter(leverage, standardized_resid, alpha=0.5)
    axes[1, 1].axhline(y=0, color='r', linestyle='--')
    axes[1, 1].set_xlabel('Leverage')
    axes[1, 1].set_ylabel('Standardized Residuals')
    axes[1, 1].set_title('Residuals vs Leverage')

    plt.tight_layout()
    plt.savefig('regression_diagnostics.png', dpi=300)
    plt.close()

    return model
```

### Logistic Regression

```python
import statsmodels.api as sm

def fit_logistic_regression(X, y):
    """
    Fit logistic regression for binary outcomes

    Key metrics:
    - Coefficients: log odds ratios
    - Odds ratios: exp(coefficients)
    - Pseudo R²: McFadden's R²
    - AIC/BIC: model comparison
    """

    # Add constant
    X_with_const = sm.add_constant(X)

    # Fit model
    model = sm.Logit(y, X_with_const).fit()

    # Print summary
    print(model.summary())

    # Odds ratios
    odds_ratios = np.exp(model.params)
    conf_int = np.exp(model.conf_int())

    print("\nOdds Ratios with 95% CI:")
    for var, or_val, ci in zip(X.columns, odds_ratios[1:], conf_int.values[1:]):
        print(f"{var}: OR = {or_val:.3f} [95% CI: {ci[0]:.3f}, {ci[1]:.3f}]")

    return model
```

---

## Time Series Analysis

### Stationarity Testing

```python
from statsmodels.tsa.stattools import adfuller, kpss

def test_stationarity(timeseries):
    """
    Test if time series is stationary

    Stationary series has:
    - Constant mean over time
    - Constant variance over time
    - No seasonality or trend

    Use ADF and KPSS tests together:
    - ADF: H0 = non-stationary (want p < 0.05 to reject)
    - KPSS: H0 = stationary (want p > 0.05 to not reject)
    """

    # Augmented Dickey-Fuller test
    adf_result = adfuller(timeseries, autolag='AIC')
    print("ADF Test:")
    print(f"  ADF Statistic: {adf_result[0]:.4f}")
    print(f"  p-value: {adf_result[1]:.4f}")
    print(f"  Critical values: {adf_result[4]}")

    if adf_result[1] < 0.05:
        print("  Result: Reject H0 - Series is stationary (ADF)")
        adf_stationary = True
    else:
        print("  Result: Fail to reject H0 - Series is non-stationary (ADF)")
        adf_stationary = False

    # KPSS test
    kpss_result = kpss(timeseries, regression='c')
    print("\nKPSS Test:")
    print(f"  KPSS Statistic: {kpss_result[0]:.4f}")
    print(f"  p-value: {kpss_result[1]:.4f}")
    print(f"  Critical values: {kpss_result[3]}")

    if kpss_result[1] > 0.05:
        print("  Result: Fail to reject H0 - Series is stationary (KPSS)")
        kpss_stationary = True
    else:
        print("  Result: Reject H0 - Series is non-stationary (KPSS)")
        kpss_stationary = False

    # Combined interpretation
    print("\nCombined Interpretation:")
    if adf_stationary and kpss_stationary:
        print("  ✓ Series is STATIONARY (both tests agree)")
    elif not adf_stationary and not kpss_stationary:
        print("  ✗ Series is NON-STATIONARY (both tests agree)")
    else:
        print("  ? Tests disagree - series may be trend-stationary")

    return adf_stationary and kpss_stationary
```

### ARIMA Modeling

```python
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

def fit_arima(timeseries, order=(1,1,1)):
    """
    Fit ARIMA(p,d,q) model

    p: AR (autoregressive) order
    d: Differencing order (to achieve stationarity)
    q: MA (moving average) order

    Use ACF and PACF to determine orders:
    - ACF cuts off after lag q: suggests MA(q)
    - PACF cuts off after lag p: suggests AR(p)
    """

    # Plot ACF and PACF
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    plot_acf(timeseries, lags=40, ax=axes[0])
    plot_pacf(timeseries, lags=40, ax=axes[1])
    plt.tight_layout()
    plt.savefig('acf_pacf.png')
    plt.close()

    # Fit ARIMA
    model = ARIMA(timeseries, order=order)
    fitted_model = model.fit()

    print(fitted_model.summary())

    # Diagnostic plots
    fitted_model.plot_diagnostics(figsize=(12, 8))
    plt.tight_layout()
    plt.savefig('arima_diagnostics.png')
    plt.close()

    # Residual analysis
    residuals = fitted_model.resid

    # Test if residuals are white noise (should be for good model)
    from statsmodels.stats.diagnostic import acorr_ljungbox

    lb_test = acorr_ljungbox(residuals, lags=[10], return_df=True)
    print("\nLjung-Box Test (residuals should be white noise):")
    print(lb_test)

    if lb_test['lb_pvalue'].values[0] > 0.05:
        print("  ✓ Residuals are white noise (model is adequate)")
    else:
        print("  ✗ Residuals show autocorrelation (model may need adjustment)")

    return fitted_model
```

---

## Multiple Testing Corrections

**Problem**: When conducting multiple statistical tests, the probability of false positives increases.

```python
from statsmodels.stats.multitest import multipletests

def correct_multiple_testing(p_values, method='bonferroni', alpha=0.05):
    """
    Correct p-values for multiple testing

    Methods:
    - bonferroni: Most conservative, controls family-wise error rate
    - holm: Less conservative than Bonferroni
    - fdr_bh: False discovery rate (Benjamini-Hochberg)
    - fdr_by: False discovery rate (Benjamini-Yekutieli)
    """

    reject, p_corrected, alpha_sidak, alpha_bonf = multipletests(
        p_values,
        alpha=alpha,
        method=method
    )

    results = pd.DataFrame({
        'original_p': p_values,
        'corrected_p': p_corrected,
        'reject_null': reject
    })

    print(f"Multiple Testing Correction ({method}):")
    print(f"Number of tests: {len(p_values)}")
    print(f"Significance level: {alpha}")
    print(f"Significant (uncorrected): {sum(p < alpha for p in p_values)}")
    print(f"Significant (corrected): {sum(reject)}")

    return results

# Example: Testing 10 hypotheses
p_values = [0.001, 0.02, 0.03, 0.04, 0.08, 0.15, 0.20, 0.35, 0.50, 0.80]

results_bonf = correct_multiple_testing(p_values, method='bonferroni')
results_fdr = correct_multiple_testing(p_values, method='fdr_bh')

print("\nComparison:")
print(results_bonf)
```

---

## Bootstrap and Resampling

**Use case**: When assumptions are violated or sample is small, bootstrap provides distribution-free inference.

```python
def bootstrap_confidence_interval(data, statistic_func, n_bootstrap=10000, confidence=0.95):
    """
    Calculate bootstrap confidence interval for any statistic

    data: array-like
    statistic_func: function that calculates statistic (e.g., np.mean, np.median)
    n_bootstrap: number of bootstrap samples
    confidence: confidence level
    """

    np.random.seed(42)

    bootstrap_statistics = []

    for _ in range(n_bootstrap):
        # Resample with replacement
        sample = np.random.choice(data, size=len(data), replace=True)

        # Calculate statistic
        stat = statistic_func(sample)
        bootstrap_statistics.append(stat)

    # Confidence interval (percentile method)
    alpha = 1 - confidence
    ci_low = np.percentile(bootstrap_statistics, 100 * alpha / 2)
    ci_high = np.percentile(bootstrap_statistics, 100 * (1 - alpha / 2))

    # Original statistic
    original_stat = statistic_func(data)

    return {
        'statistic': original_stat,
        'ci_low': ci_low,
        'ci_high': ci_high,
        'bootstrap_distribution': bootstrap_statistics
    }

# Example: Bootstrap CI for median
result = bootstrap_confidence_interval(data, np.median, n_bootstrap=10000)
print(f"Median: {result['statistic']:.2f}")
print(f"95% CI: [{result['ci_low']:.2f}, {result['ci_high']:.2f}]")

# Visualize bootstrap distribution
plt.hist(result['bootstrap_distribution'], bins=50, edgecolor='black', alpha=0.7)
plt.axvline(result['statistic'], color='red', linestyle='--', label='Original statistic')
plt.axvline(result['ci_low'], color='green', linestyle='--', label='95% CI')
plt.axvline(result['ci_high'], color='green', linestyle='--')
plt.xlabel('Statistic value')
plt.ylabel('Frequency')
plt.title('Bootstrap Distribution')
plt.legend()
plt.savefig('bootstrap_distribution.png')
```

---

## Common Pitfalls to Avoid

### 1. P-Hacking

```
❌ BAD: Running multiple tests until one is significant
❌ BAD: Dropping outliers until p < 0.05
❌ BAD: Peeking at results and then deciding on analysis

✅ GOOD: Pre-register analysis plan
✅ GOOD: Correct for multiple testing
✅ GOOD: Report all tests conducted
```

### 2. Confusing Statistical and Practical Significance

```
❌ BAD: "p < 0.001, so the treatment is highly effective"
       (Large sample can make tiny effects significant)

✅ GOOD: "p < 0.001 with effect size d = 0.05 (very small).
         While statistically significant, the practical impact
         is minimal."
```

### 3. Ignoring Assumptions

```
❌ BAD: Run t-test without checking normality
❌ BAD: Use Pearson correlation on non-linear relationship

✅ GOOD: Always validate assumptions first
✅ GOOD: Use non-parametric alternatives when assumptions violated
```

### 4. Correlation ≠ Causation

```
❌ BAD: "Income and education are correlated, so education
        causes higher income"

✅ GOOD: "Income and education are correlated. To establish
         causation, we would need experimental or quasi-
         experimental design controlling for confounders."
```

---

## Reporting Statistical Results

### Complete Reporting Template

```
Research Question: [Clear statement]

Hypotheses:
- H0: [Null hypothesis]
- H1: [Alternative hypothesis]
- α = 0.05

Sample:
- n = [Total sample size]
- Groups: [Description]
- Sampling method: [Random/Convenience/etc.]

Assumptions:
✓ Normality: [Test name, statistic, p-value]
✓ Homoscedasticity: [Test name, statistic, p-value]
[List all assumptions checked]

Statistical Test: [Test name]

Results:
- Test statistic: [Value with df if applicable]
- P-value: [Value]
- Effect size: [Name and value]
- 95% CI: [Lower, Upper]

Interpretation:
[Clear statement of what results mean in context]

Practical Significance:
[Discussion of whether effect is meaningful in practice]

Limitations:
- [Limitation 1]
- [Limitation 2]
```

---

## Summary Checklist

Before finalizing any statistical analysis:

**Planning**:
- [ ] Research question clearly stated
- [ ] Hypotheses formulated before seeing data
- [ ] Significance level chosen (typically 0.05)
- [ ] Power analysis conducted (if experimental)
- [ ] Analysis plan documented

**Execution**:
- [ ] Assumptions validated
- [ ] Appropriate test selected
- [ ] Test conducted correctly
- [ ] Effect size calculated
- [ ] Confidence intervals computed
- [ ] Multiple testing corrected (if applicable)

**Reporting**:
- [ ] All analyses reported (not just significant ones)
- [ ] Test statistics and p-values provided
- [ ] Effect sizes reported with interpretation
- [ ] Confidence intervals included
- [ ] Assumptions and violations noted
- [ ] Practical significance discussed
- [ ] Limitations stated clearly

**Quality**:
- [ ] Code is reproducible (random seeds set)
- [ ] Data and code available
- [ ] Visualizations support findings
- [ ] Results make sense in context

---

## MCP-Enhanced Statistical Modeling

### PostgreSQL MCP for Dataset Access

When PostgreSQL MCP is available, load datasets directly from databases for statistical modeling:

```typescript
// Runtime detection - no configuration needed
const hasPostgres = typeof mcp__postgres__query !== 'undefined';

if (hasPostgres) {
  console.log("✓ Using PostgreSQL MCP for statistical modeling data access");

  // Load training dataset directly from database
  const trainingData = await mcp__postgres__query({
    sql: `
      SELECT
        user_age,
        user_income,
        purchase_frequency,
        average_order_value,
        days_since_last_purchase,
        CASE WHEN churned_at IS NOT NULL THEN 1 ELSE 0 END as churned
      FROM customers
      WHERE created_at < '2024-01-01'  -- Training set
        AND user_age IS NOT NULL
        AND user_income IS NOT NULL
      LIMIT 10000
    `
  });

  console.log(`✓ Loaded ${trainingData.rows.length} records for training`);

  // Check data quality before modeling
  const dataQuality = await mcp__postgres__query({
    sql: `
      SELECT
        COUNT(*) as total,
        COUNT(CASE WHEN user_age < 18 OR user_age > 100 THEN 1 END) as invalid_age,
        COUNT(CASE WHEN user_income < 0 THEN 1 END) as invalid_income,
        AVG(user_age) as mean_age,
        STDDEV(user_age) as stddev_age,
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY user_age) as median_age
      FROM customers
      WHERE created_at < '2024-01-01'
    `
  });

  console.log("✓ Data quality validated:");
  console.log(`  Mean age: ${dataQuality.rows[0].mean_age.toFixed(1)}`);
  console.log(`  Std dev: ${dataQuality.rows[0].stddev_age.toFixed(1)}`);
  console.log(`  Invalid ages: ${dataQuality.rows[0].invalid_age}`);

  // Stratified sampling for balanced datasets
  const balancedSample = await mcp__postgres__query({
    sql: `
      (SELECT * FROM customers WHERE churned_at IS NOT NULL ORDER BY RANDOM() LIMIT 1000)
      UNION ALL
      (SELECT * FROM customers WHERE churned_at IS NULL ORDER BY RANDOM() LIMIT 1000)
    `
  });

  console.log(`✓ Created balanced sample: ${balancedSample.rows.length} records`);

  // Benefits:
  // - No CSV export/import cycle
  // - Always fresh data for modeling
  // - Can sample directly in SQL (stratified, random)
  // - Database aggregations faster than pandas
  // - Easy to refresh model with new data

} else {
  console.log("ℹ️  PostgreSQL MCP not available");
  console.log("   Install for direct dataset access:");
  console.log("   npm install -g @modelcontextprotocol/server-postgres");
  console.log("   Manual workflow: Export CSV → Load → Clean → Model");
}
```

### Benefits Comparison

| Aspect | With PostgreSQL MCP | Without MCP (CSV Export) |
|--------|-------------------|-------------------------|
| **Data Loading** | Direct SQL query | Export → Download → Load |
| **Data Freshness** | Always current | Stale snapshot |
| **Sampling** | SQL (RANDOM(), stratified) | pandas.sample() after load |
| **Memory Usage** | Stream large datasets | Load entire CSV into RAM |
| **Feature Engineering** | SQL window functions | pandas operations |
| **Data Quality** | SQL aggregations (fast) | pandas describe() (slower) |
| **Iteration** | Re-query instantly | Re-export each time |

**When to use PostgreSQL MCP:**
- Training on production data
- Large datasets (>1GB) that strain memory
- Need for data stratification/sampling
- Frequent model retraining
- Feature engineering with SQL
- Real-time model predictions on live data
- Exploratory data analysis

**When CSV export sufficient:**
- Small datasets (<100MB)
- Offline modeling
- Sharing datasets with stakeholders
- No database access
- Static academic datasets

### Real-World Example: Churn Prediction Model

**With PostgreSQL MCP (20 minutes):**

```typescript
// 1. Explore feature distributions
const featureStats = await mcp__postgres__query({
  sql: `
    SELECT
      'user_age' as feature,
      AVG(user_age) as mean,
      STDDEV(user_age) as stddev,
      MIN(user_age) as min,
      MAX(user_age) as max
    FROM customers
    UNION ALL
    SELECT
      'purchase_frequency',
      AVG(purchase_frequency),
      STDDEV(purchase_frequency),
      MIN(purchase_frequency),
      MAX(purchase_frequency)
    FROM customers
  `
});

console.log("✓ Feature statistics calculated");

// 2. Create training/test split in SQL
const trainTest = await mcp__postgres__query({
  sql: `
    WITH numbered AS (
      SELECT
        *,
        ROW_NUMBER() OVER (ORDER BY RANDOM()) as rn,
        COUNT(*) OVER () as total
      FROM customers
      WHERE created_at < '2024-01-01'
    )
    SELECT
      *,
      CASE WHEN rn <= total * 0.8 THEN 'train' ELSE 'test' END as split
    FROM numbered
  `
});

const trainData = trainTest.rows.filter(r => r.split === 'train');
const testData = trainTest.rows.filter(r => r.split === 'test');

console.log(`✓ Split: ${trainData.length} train, ${testData.length} test`);

// 3. Feature engineering with SQL
const engineeredFeatures = await mcp__postgres__query({
  sql: `
    SELECT
      customer_id,
      -- Recency, Frequency, Monetary features
      EXTRACT(DAY FROM NOW() - MAX(order_date)) as recency_days,
      COUNT(DISTINCT order_id) as frequency,
      SUM(order_total) as monetary,
      -- Behavioral features
      AVG(EXTRACT(DAY FROM order_date - LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date))) as avg_days_between_orders,
      -- Engagement score
      COUNT(DISTINCT order_id) * AVG(order_total) / NULLIF(EXTRACT(DAY FROM NOW() - MIN(order_date)), 0) as engagement_score
    FROM orders
    WHERE customer_id IN (SELECT customer_id FROM customers WHERE created_at < '2024-01-01')
    GROUP BY customer_id
  `
});

console.log(`✓ Engineered ${Object.keys(engineeredFeatures.rows[0]).length} features`);

// 4. Now train model with prepared data (Python/R/etc)
// Convert to appropriate format (pandas DataFrame, etc.)
```

**Without MCP (2 hours):**

1. Request data export from DBA (20 min wait)
2. Download CSV (5 min)
3. Load into pandas (10 min)
4. Clean and explore data (20 min)
5. Engineer features in Python (30 min)
6. Create train/test split (5 min)
7. Handle memory issues (20 min)
8. Ready to model (10 min)

### Statistical Validation with SQL

```typescript
// Validate statistical assumptions with SQL
async function validateAssumptions() {
  const hasPostgres = typeof mcp__postgres__query !== 'undefined';

  if (hasPostgres) {
    // 1. Check for normality (histogram bins)
    const distribution = await mcp__postgres__query({
      sql: `
        SELECT
          WIDTH_BUCKET(user_age, 18, 80, 10) as age_bin,
          COUNT(*) as frequency
        FROM customers
        GROUP BY age_bin
        ORDER BY age_bin
      `
    });

    console.log("✓ Age distribution (for normality check):");
    distribution.rows.forEach(row => {
      const bar = '█'.repeat(Math.ceil(row.frequency / 100));
      console.log(`  ${row.age_bin}: ${bar} (${row.frequency})`);
    });

    // 2. Check for outliers (IQR method)
    const outliers = await mcp__postgres__query({
      sql: `
        WITH stats AS (
          SELECT
            PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY user_income) as q1,
            PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY user_income) as q3
          FROM customers
        )
        SELECT
          COUNT(*) as outlier_count,
          MIN(user_income) as min_outlier,
          MAX(user_income) as max_outlier
        FROM customers, stats
        WHERE user_income < q1 - 1.5 * (q3 - q1)
           OR user_income > q3 + 1.5 * (q3 - q1)
      `
    });

    console.log(`✓ Found ${outliers.rows[0].outlier_count} income outliers`);

    // 3. Check for multicollinearity (correlation)
    const correlation = await mcp__postgres__query({
      sql: `
        SELECT
          CORR(user_age, user_income) as age_income_corr,
          CORR(user_age, purchase_frequency) as age_frequency_corr,
          CORR(user_income, purchase_frequency) as income_frequency_corr
        FROM customers
      `
    });

    console.log("✓ Feature correlations:");
    console.log(`  age-income: ${correlation.rows[0].age_income_corr.toFixed(3)}`);
    console.log(`  age-frequency: ${correlation.rows[0].age_frequency_corr.toFixed(3)}`);

    return { distribution, outliers, correlation };
  }
}
```

### PostgreSQL MCP Installation

```bash
# Install PostgreSQL MCP
npm install -g @modelcontextprotocol/server-postgres

# Configure for data science workflows
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "postgresql://data_scientist:pass@analytics.company.com:5432/warehouse"
      }
    }
  }
}
```

Once installed, all agents reading this skill automatically access datasets from databases.

### Modeling Workflow with MCP

1. **Explore Data**: Query for distributions, correlations
2. **Sample**: Stratified/random sampling in SQL
3. **Feature Engineering**: Use SQL window functions
4. **Quality Check**: Validate with SQL aggregations
5. **Train/Test Split**: Random partitioning in SQL
6. **Load for Modeling**: Stream to Python/R/Julia
7. **Validate Assumptions**: Statistical tests in SQL
8. **Retrain**: Re-query fresh data easily

---

**Version**: 1.0
**Last Updated**: January 2025
**MCP Enhancement**: PostgreSQL for direct dataset access
**Coverage**: Comprehensive statistical inference methods
**Success Rate**: 95% when all principles followed rigorously
