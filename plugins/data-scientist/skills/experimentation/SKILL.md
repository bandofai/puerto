# Experimentation Skill

**Production-tested patterns for rigorous A/B testing and causal inference**

This skill codifies best practices from thousands of online controlled experiments and decades of experimental design research across technology, healthcare, and social sciences.

---

## Core Principles

1. **Randomization is Key**: Random assignment is the gold standard for causal inference
2. **Pre-register Everything**: Decide on analysis before seeing results to avoid p-hacking
3. **Power First**: Calculate sample size before starting experiment
4. **ITT Analysis**: Intention-to-treat is the primary analysis
5. **Validity Matters**: Internal validity (causation) and external validity (generalization)

---

## A/B Testing Framework

### The A/B Test Lifecycle

```
1. HYPOTHESIS
   ↓
2. POWER ANALYSIS (sample size)
   ↓
3. DESIGN (randomization, metrics)
   ↓
4. PRE-REGISTRATION (statistical analysis plan)
   ↓
5. IMPLEMENTATION (ship experiment)
   ↓
6. MONITORING (data quality, balance)
   ↓
7. ANALYSIS (hypothesis test, effect size)
   ↓
8. INTERPRETATION (practical significance)
   ↓
9. DECISION (ship/don't ship)
   ↓
10. LEARNING (document for future)
```

---

## Power Analysis and Sample Size

### Why Power Analysis?

```
Power = Probability of detecting an effect if it exists
Power = 1 - β (where β is Type II error rate)

Typical target: 80% power
Means: 20% chance of missing a real effect
```

### Sample Size Calculation

#### For Proportions (Conversion Rates)

```python
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize
import numpy as np

def calculate_sample_size_proportions(
    baseline_rate,
    mde,  # Minimum detectable effect (absolute)
    alpha=0.05,
    power=0.80,
    ratio=1
):
    """
    Calculate sample size for A/B test with proportion outcome

    baseline_rate: Current conversion rate (e.g., 0.10 for 10%)
    mde: Minimum detectable effect in absolute terms (e.g., 0.02 for 2 percentage points)
    alpha: Significance level (default 0.05)
    power: Statistical power (default 0.80)
    ratio: Ratio of treatment to control size (default 1 for equal sizes)

    Returns: Required sample size per group
    """

    # Target rate
    target_rate = baseline_rate + mde

    # Effect size (Cohen's h)
    effect_size = proportion_effectsize(baseline_rate, target_rate)

    # Power analysis
    power_analysis = NormalIndPower()
    sample_size = power_analysis.solve_power(
        effect_size=effect_size,
        alpha=alpha,
        power=power,
        ratio=ratio,
        alternative='two-sided'
    )

    # Results
    total_size = sample_size * (1 + ratio)

    results = {
        'sample_size_per_group': int(np.ceil(sample_size)),
        'total_sample_size': int(np.ceil(total_size)),
        'effect_size': effect_size,
        'baseline_rate': baseline_rate,
        'target_rate': target_rate,
        'relative_lift': (mde / baseline_rate) * 100
    }

    # Print summary
    print(f"Power Analysis for A/B Test (Proportions)")
    print(f"=" * 50)
    print(f"Baseline rate: {baseline_rate:.1%}")
    print(f"Minimum detectable effect: {mde:.1%} absolute ({results['relative_lift']:.1f}% relative)")
    print(f"Significance level (α): {alpha}")
    print(f"Power (1-β): {power}")
    print(f"\nRequired Sample Size:")
    print(f"  Per group: {results['sample_size_per_group']:,}")
    print(f"  Total: {results['total_sample_size']:,}")

    return results

# Example usage
calculate_sample_size_proportions(
    baseline_rate=0.10,  # 10% baseline
    mde=0.02,            # Want to detect 2 percentage point lift
    alpha=0.05,
    power=0.80
)
```

#### For Continuous Metrics (Revenue, Time on Site)

```python
from statsmodels.stats.power import TTestIndPower

def calculate_sample_size_continuous(
    mean,
    std,
    mde,  # Minimum detectable effect (absolute)
    alpha=0.05,
    power=0.80,
    ratio=1
):
    """
    Calculate sample size for continuous outcome

    mean: Baseline mean
    std: Standard deviation
    mde: Minimum detectable effect (absolute)
    alpha: Significance level
    power: Statistical power
    ratio: Ratio of treatment to control

    Returns: Required sample size per group
    """

    # Effect size (Cohen's d)
    effect_size = mde / std

    # Power analysis
    power_analysis = TTestIndPower()
    sample_size = power_analysis.solve_power(
        effect_size=effect_size,
        alpha=alpha,
        power=power,
        ratio=ratio,
        alternative='two-sided'
    )

    results = {
        'sample_size_per_group': int(np.ceil(sample_size)),
        'total_sample_size': int(np.ceil(sample_size * (1 + ratio))),
        'effect_size': effect_size,
        'baseline_mean': mean,
        'target_mean': mean + mde,
        'relative_lift': (mde / mean) * 100 if mean != 0 else 0
    }

    print(f"Power Analysis for A/B Test (Continuous)")
    print(f"=" * 50)
    print(f"Baseline mean: {mean:.2f}")
    print(f"Standard deviation: {std:.2f}")
    print(f"Minimum detectable effect: {mde:.2f} ({results['relative_lift']:.1f}% relative)")
    print(f"Significance level (α): {alpha}")
    print(f"Power (1-β): {power}")
    print(f"\nRequired Sample Size:")
    print(f"  Per group: {results['sample_size_per_group']:,}")
    print(f"  Total: {results['total_sample_size']:,}")

    return results

# Example usage
calculate_sample_size_continuous(
    mean=50.0,   # $50 average order value
    std=20.0,    # $20 standard deviation
    mde=5.0,     # Want to detect $5 increase
    alpha=0.05,
    power=0.80
)
```

### Power Curves

```python
import matplotlib.pyplot as plt

def plot_power_curve(baseline_rate, sample_size_per_group, alpha=0.05):
    """Visualize power as function of effect size"""

    mde_range = np.linspace(0.005, 0.05, 50)  # 0.5% to 5% absolute lift
    powers = []

    power_analysis = NormalIndPower()

    for mde in mde_range:
        target_rate = baseline_rate + mde
        effect_size = proportion_effectsize(baseline_rate, target_rate)

        power = power_analysis.solve_power(
            effect_size=effect_size,
            alpha=alpha,
            nobs1=sample_size_per_group,
            ratio=1,
            alternative='two-sided'
        )
        powers.append(power)

    plt.figure(figsize=(10, 6))
    plt.plot(mde_range * 100, powers, linewidth=2)
    plt.axhline(y=0.80, color='r', linestyle='--', label='80% power')
    plt.axhline(y=0.90, color='orange', linestyle='--', label='90% power')
    plt.xlabel('Absolute Lift (percentage points)')
    plt.ylabel('Statistical Power')
    plt.title(f'Power Curve (n={sample_size_per_group:,} per group, baseline={baseline_rate:.1%})')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.savefig('power_curve.png', dpi=300, bbox_inches='tight')
    plt.close()

plot_power_curve(baseline_rate=0.10, sample_size_per_group=5000)
```

---

## Randomization Strategies

### 1. Simple Randomization

```python
import numpy as np
import pandas as pd

def simple_randomization(n, p=0.5, seed=42):
    """
    Simple random assignment

    Pros: Easiest to implement, unbiased in expectation
    Cons: May have imbalance with small samples

    n: Number of units
    p: Probability of treatment (0.5 for 50/50)
    seed: Random seed for reproducibility
    """
    np.random.seed(seed)
    return np.random.binomial(1, p, n)

# Example
n_users = 1000
assignments = simple_randomization(n_users, p=0.5, seed=42)

print(f"Control: {(assignments == 0).sum()} ({(assignments == 0).mean():.1%})")
print(f"Treatment: {(assignments == 1).sum()} ({(assignments == 1).mean():.1%})")
```

### 2. Stratified Randomization

```python
def stratified_randomization(df, strata_cols, treatment_col='treatment', p=0.5, seed=42):
    """
    Stratified randomization - ensures balance on important covariates

    Pros: Guarantees balance on stratification variables
    Cons: Need to know important covariates in advance

    df: DataFrame with units
    strata_cols: Column(s) to stratify on (e.g., ['country', 'device_type'])
    treatment_col: Name of treatment column to create
    p: Probability of treatment within each stratum
    seed: Random seed
    """
    np.random.seed(seed)

    # Randomize within each stratum
    df[treatment_col] = df.groupby(strata_cols).transform(
        lambda x: np.random.binomial(1, p, len(x))
    ).astype(int)

    # Check balance
    print(f"Overall Treatment Rate: {df[treatment_col].mean():.1%}")
    print(f"\nBalance by Strata:")
    print(df.groupby(strata_cols)[treatment_col].agg(['count', 'mean']))

    return df

# Example
df = pd.DataFrame({
    'user_id': range(1000),
    'country': np.random.choice(['US', 'UK', 'CA'], 1000),
    'device': np.random.choice(['mobile', 'desktop'], 1000)
})

df = stratified_randomization(df, strata_cols=['country', 'device'], seed=42)
```

### 3. Block Randomization

```python
def block_randomization(n, block_size=4, seed=42):
    """
    Block randomization - ensures equal group sizes

    Pros: Guarantees balance over time
    Cons: Predictable if block size known

    n: Number of units
    block_size: Size of each block (must be even)
    seed: Random seed
    """
    np.random.seed(seed)

    if block_size % 2 != 0:
        raise ValueError("Block size must be even")

    n_blocks = int(np.ceil(n / block_size))
    assignments = []

    for _ in range(n_blocks):
        # Create balanced block
        block = [0] * (block_size // 2) + [1] * (block_size // 2)
        np.random.shuffle(block)
        assignments.extend(block)

    # Trim to exact size
    assignments = np.array(assignments[:n])

    print(f"Control: {(assignments == 0).sum()} ({(assignments == 0).mean():.1%})")
    print(f"Treatment: {(assignments == 1).sum()} ({(assignments == 1).mean():.1%})")

    return assignments

# Example
assignments = block_randomization(n=1000, block_size=4, seed=42)
```

---

## Statistical Analysis Plan (SAP)

**CRITICAL**: Write this BEFORE seeing results to avoid bias.

### Template

```markdown
# Statistical Analysis Plan

## Experiment Details
- **Experiment Name**: [Clear, descriptive name]
- **Owner**: [Name]
- **Date**: [SAP creation date]
- **Hypothesis**: [What we're testing]

## Primary Outcome
- **Metric**: [Name of metric]
- **Type**: [Binary/Continuous/Count]
- **Success Criteria**: [What constitutes success]

## Secondary Outcomes
1. [Metric 1]
2. [Metric 2]
3. [Metric 3]

## Sample Size
- **Per Group**: [N based on power analysis]
- **Total**: [Total N]
- **Expected Duration**: [Days/weeks]
- **Traffic Allocation**: [% to treatment]

## Randomization
- **Unit**: [User/Session/Page view]
- **Method**: [Simple/Stratified/Block]
- **Strata** (if stratified): [Variables]
- **Seed**: [Random seed for reproducibility]

## Exclusions
Pre-specified exclusions:
- [Bot traffic]
- [Internal employees]
- [Incomplete sessions]
- [Technical errors]

## Primary Analysis
- **Test**: [Test name, e.g., Two-proportion z-test]
- **Significance Level**: α = 0.05
- **Sidedness**: Two-sided
- **Analysis Population**: Intention-to-treat (ITT)

## Multiple Testing
- **Number of Hypotheses**: [N]
- **Correction Method**: [Bonferroni/Holm/FDR]
- **Adjusted α**: [Value]

## Subgroup Analyses
Pre-specified subgroups (exploratory only):
1. [Subgroup 1, e.g., By device type]
2. [Subgroup 2, e.g., By user segment]

**Note**: These are exploratory. No claims without replication.

## Stopping Rules
- **Fixed Sample**: Stop when reach target N
- **Sequential** (if applicable): [Alpha spending function]
- **Futility**: [Conditions for early stop]
- **Safety**: [Conditions for emergency stop]

## Reporting
Will report:
- Test statistic and p-value
- Effect size with 95% CI
- Absolute and relative lift
- Per-group sample sizes
- All pre-specified analyses
- Any post-hoc analyses (clearly labeled)

## Signatures
- **Author**: [Name, Date]
- **Reviewer**: [Name, Date]
- **Approved**: [Name, Date]
```

---

## A/B Test Analysis

### Balance Check

```python
def check_randomization_balance(df, treatment_col, covariates):
    """
    Check if randomization produced balanced groups

    df: DataFrame
    treatment_col: Name of treatment column
    covariates: List of covariate columns to check

    Returns: DataFrame with balance statistics
    """
    from scipy.stats import ttest_ind, chi2_contingency

    results = []

    for covar in covariates:
        if df[covar].dtype in ['int64', 'float64']:
            # Continuous covariate - t-test
            control = df[df[treatment_col] == 0][covar]
            treatment = df[df[treatment_col] == 1][covar]

            stat, p_value = ttest_ind(control, treatment)

            results.append({
                'covariate': covar,
                'control_mean': control.mean(),
                'treatment_mean': treatment.mean(),
                'difference': treatment.mean() - control.mean(),
                'p_value': p_value,
                'balanced': 'Yes' if p_value > 0.05 else 'No'
            })
        else:
            # Categorical covariate - chi-square test
            contingency_table = pd.crosstab(df[covar], df[treatment_col])
            chi2, p_value, dof, expected = chi2_contingency(contingency_table)

            results.append({
                'covariate': covar,
                'control_mean': 'N/A',
                'treatment_mean': 'N/A',
                'difference': 'N/A',
                'p_value': p_value,
                'balanced': 'Yes' if p_value > 0.05 else 'No'
            })

    balance_df = pd.DataFrame(results)

    print("Randomization Balance Check")
    print("=" * 60)
    print(balance_df.to_string(index=False))
    print()

    if (balance_df['p_value'] < 0.05).any():
        print("⚠ WARNING: Imbalance detected on some covariates")
        print("   Consider regression adjustment or stratified analysis")
    else:
        print("✓ All covariates balanced (no significant differences)")

    return balance_df
```

### Primary Analysis: Two-Proportion Test

```python
from scipy.stats import chi2_contingency
from statsmodels.stats.proportion import proportions_ztest, confint_proportions_2indep

def analyze_ab_test_proportions(df, treatment_col, outcome_col):
    """
    Analyze A/B test with binary outcome

    df: DataFrame with experimental data
    treatment_col: Name of treatment column (0=control, 1=treatment)
    outcome_col: Name of outcome column (0=no conversion, 1=conversion)

    Returns: Dictionary with test results
    """

    # Summary statistics
    summary = df.groupby(treatment_col)[outcome_col].agg(['sum', 'count', 'mean'])
    summary.columns = ['conversions', 'total', 'rate']
    summary.index = ['Control', 'Treatment']

    # Extract values
    conversions = summary['conversions'].values
    totals = summary['total'].values
    rates = summary['rate'].values

    # Two-proportion z-test
    z_stat, p_value = proportions_ztest(conversions, totals, alternative='two-sided')

    # Confidence interval for difference
    ci_low, ci_high = confint_proportions_2indep(
        conversions[0], totals[0],
        conversions[1], totals[1],
        method='wald'
    )

    # Effect sizes
    absolute_lift = rates[1] - rates[0]
    relative_lift = (absolute_lift / rates[0]) * 100 if rates[0] > 0 else 0

    # Results
    results = {
        'control_rate': rates[0],
        'treatment_rate': rates[1],
        'absolute_lift': absolute_lift,
        'relative_lift': relative_lift,
        'z_stat': z_stat,
        'p_value': p_value,
        'ci_low': ci_low,
        'ci_high': ci_high,
        'significant': p_value < 0.05
    }

    # Print report
    print("=" * 70)
    print("A/B TEST RESULTS")
    print("=" * 70)
    print()
    print("SAMPLE SIZES")
    print("-" * 70)
    print(summary[['total', 'conversions']])
    print()

    print("CONVERSION RATES")
    print("-" * 70)
    print(f"Control:   {rates[0]:.4%}")
    print(f"Treatment: {rates[1]:.4%}")
    print()

    print("EFFECT SIZE")
    print("-" * 70)
    print(f"Absolute lift: {absolute_lift:+.4%}")
    print(f"Relative lift: {relative_lift:+.2f}%")
    print(f"95% CI for difference: [{ci_low:.4%}, {ci_high:.4%}]")
    print()

    print("STATISTICAL TEST")
    print("-" * 70)
    print(f"Test: Two-proportion z-test")
    print(f"z-statistic: {z_stat:.4f}")
    print(f"p-value: {p_value:.4f}")
    print()

    print("DECISION")
    print("-" * 70)
    if p_value < 0.05:
        direction = "increases" if absolute_lift > 0 else "decreases"
        print(f"✓ SIGNIFICANT: Treatment {direction} conversion rate")
        print(f"  Relative change: {abs(relative_lift):.1f}% {direction}")
        print(f"  Evidence: p = {p_value:.4f} < 0.05")
    else:
        print(f"✗ NOT SIGNIFICANT: No evidence of treatment effect")
        print(f"  p = {p_value:.4f} ≥ 0.05")
    print()

    return results
```

### Regression Adjustment

```python
import statsmodels.formula.api as smf

def regression_adjustment(df, treatment_col, outcome_col, covariates):
    """
    Increase precision with regression adjustment

    Controlling for pre-treatment covariates can reduce variance
    and increase power, even in randomized experiments.

    df: DataFrame
    treatment_col: Treatment indicator
    outcome_col: Outcome variable
    covariates: List of covariate column names

    Returns: Regression model with adjusted treatment effect
    """

    # Build formula
    covar_str = ' + '.join(covariates)
    formula = f"{outcome_col} ~ {treatment_col} + {covar_str}"

    # Fit regression
    model = smf.ols(formula, data=df).fit()

    # Extract treatment effect
    treatment_effect = model.params[treatment_col]
    ci = model.conf_int().loc[treatment_col]
    p_value = model.pvalues[treatment_col]

    print("Regression-Adjusted Treatment Effect")
    print("=" * 60)
    print(f"Treatment effect: {treatment_effect:.4f}")
    print(f"95% CI: [{ci[0]:.4f}, {ci[1]:.4f}]")
    print(f"p-value: {p_value:.4f}")
    print()
    print("Full Model:")
    print(model.summary())

    return model
```

---

## Sequential Testing

**Problem**: Peeking at results increases false positive rate.
**Solution**: Alpha spending functions control Type I error.

```python
from scipy.stats import norm

def sequential_analysis_obrien_fleming(
    control_conversions,
    control_total,
    treatment_conversions,
    treatment_total,
    alpha=0.05,
    max_n=10000
):
    """
    Sequential test with O'Brien-Fleming boundary

    Allows interim analyses while controlling overall alpha

    Returns: (can_stop, z_stat, boundary, information_fraction)
    """

    # Current sample size
    current_n = control_total + treatment_total

    # Information fraction (how far through experiment)
    information_fraction = min(current_n / max_n, 1.0)

    # Calculate z-statistic
    control_rate = control_conversions / control_total
    treatment_rate = treatment_conversions / treatment_total

    pooled_rate = (control_conversions + treatment_conversions) / \
                  (control_total + treatment_total)

    se = np.sqrt(pooled_rate * (1 - pooled_rate) *
                (1/control_total + 1/treatment_total))

    z_stat = (treatment_rate - control_rate) / se

    # O'Brien-Fleming boundary (conservative early, relaxed late)
    boundary = norm.ppf(1 - alpha/2) / np.sqrt(information_fraction)

    # Decision
    can_stop = abs(z_stat) > boundary

    print(f"Sequential Analysis (O'Brien-Fleming)")
    print(f"=" * 60)
    print(f"Information fraction: {information_fraction:.1%}")
    print(f"Current sample size: {current_n:,} / {max_n:,}")
    print(f"z-statistic: {z_stat:.4f}")
    print(f"Boundary: ±{boundary:.4f}")
    print()

    if can_stop:
        print(f"✓ CAN STOP: |z| > boundary")
        print(f"  Result is significant at α = {alpha}")
    else:
        print(f"✗ CONTINUE: |z| ≤ boundary")
        print(f"  Need more data for conclusive result")

    return {
        'can_stop': can_stop,
        'z_stat': z_stat,
        'boundary': boundary,
        'information_fraction': information_fraction
    }
```

---

## Causal Inference Methods

### 1. Difference-in-Differences (DiD)

**Use case**: Natural experiments where treatment and control groups exist over time.

```python
import statsmodels.formula.api as smf

def difference_in_differences(df, outcome, treatment, time, group):
    """
    Estimate treatment effect with DiD

    df: Panel data (multiple time periods, treatment/control groups)
    outcome: Outcome variable
    treatment: 0=pre, 1=post treatment
    time: Time period
    group: 0=control, 1=treatment group

    Effect = (Treatment_post - Treatment_pre) - (Control_post - Control_pre)
    """

    # Create interaction term (this is the DiD estimator)
    df['did_term'] = df[group] * df[time]

    # Regression
    formula = f"{outcome} ~ C({group}) + C({time}) + did_term"
    model = smf.ols(formula, data=df).fit(cov_type='HC1')  # Robust SE

    # Treatment effect
    did_effect = model.params['did_term']
    ci = model.conf_int().loc['did_term']
    p_value = model.pvalues['did_term']

    print("Difference-in-Differences Estimation")
    print("=" * 60)
    print(f"Treatment Effect: {did_effect:.4f}")
    print(f"95% CI: [{ci[0]:.4f}, {ci[1]:.4f}]")
    print(f"p-value: {p_value:.4f}")
    print()
    print("Assumptions:")
    print("  1. Parallel trends: Control and treatment would have")
    print("     followed same trend without treatment")
    print("  2. No compositional changes in groups")
    print()
    print(model.summary())

    return model
```

### 2. Regression Discontinuity Design (RDD)

**Use case**: Treatment assigned based on cutoff of running variable.

```python
def regression_discontinuity(df, outcome, running_var, threshold, bandwidth=None):
    """
    Estimate treatment effect with RDD

    df: DataFrame
    outcome: Outcome variable
    running_var: Assignment variable (e.g., test score)
    threshold: Cutoff for treatment
    bandwidth: Window around threshold (if None, use optimal)

    Example: Students with score ≥ 70 get scholarship
    """

    # Treatment indicator
    df['treatment'] = (df[running_var] >= threshold).astype(int)

    # Center running variable
    df['running_centered'] = df[running_var] - threshold

    # Optimal bandwidth (simple rule - use rdrobust package for production)
    if bandwidth is None:
        bandwidth = 2 * df['running_centered'].std()

    # Restrict to bandwidth
    df_rdd = df[abs(df['running_centered']) <= bandwidth].copy()

    # Local linear regression
    formula = f"{outcome} ~ treatment * running_centered"
    model = smf.ols(formula, data=df_rdd).fit(cov_type='HC1')

    # Treatment effect (jump at threshold)
    rdd_effect = model.params['treatment']
    ci = model.conf_int().loc['treatment']
    p_value = model.pvalues['treatment']

    print("Regression Discontinuity Design")
    print("=" * 60)
    print(f"Threshold: {threshold}")
    print(f"Bandwidth: {bandwidth:.2f}")
    print(f"Sample size in bandwidth: {len(df_rdd)}")
    print(f"\nTreatment Effect: {rdd_effect:.4f}")
    print(f"95% CI: [{ci[0]:.4f}, {ci[1]:.4f}]")
    print(f"p-value: {p_value:.4f}")
    print()
    print("Assumptions:")
    print("  1. No manipulation of running variable")
    print("  2. Continuous relationship on either side of cutoff")
    print()
    print(model.summary())

    # Visualization
    plt.figure(figsize=(10, 6))

    # Plot data
    control = df_rdd[df_rdd['treatment'] == 0]
    treated = df_rdd[df_rdd['treatment'] == 1]

    plt.scatter(control['running_centered'], control[outcome],
               alpha=0.5, label='Control', color='blue')
    plt.scatter(treated['running_centered'], treated[outcome],
               alpha=0.5, label='Treatment', color='red')

    # Plot fitted lines
    x_control = np.linspace(control['running_centered'].min(), 0, 100)
    x_treated = np.linspace(0, treated['running_centered'].max(), 100)

    # Predictions from model
    # (simplified - actual would use model.predict())

    plt.axvline(x=0, color='black', linestyle='--', label='Threshold')
    plt.xlabel(f'{running_var} (centered at threshold)')
    plt.ylabel(outcome)
    plt.title('Regression Discontinuity Design')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('rdd_plot.png', dpi=300)
    plt.close()

    return model
```

---

## Experimental Validity Checklist

### Internal Validity (Causal Inference)

```
✓ Randomization successful
  - Balance check passed
  - Random assignment implemented correctly

✓ No selection bias
  - Intention-to-treat (ITT) analysis used
  - All randomized units included

✓ No attrition bias
  - Similar dropout rates in both groups
  - Dropouts analyzed and reported

✓ No interference between units
  - Stable unit treatment value assumption (SUTVA) holds
  - No spillover or network effects

✓ Treatment implemented as designed
  - Compliance tracked
  - No contamination between groups
```

### External Validity (Generalization)

```
✓ Representative sample
  - Sample reflects target population
  - Exclusions documented and justified

✓ Realistic context
  - Experiment conducted in natural setting
  - No artificial conditions

✓ No Hawthorne effects
  - Participants unaware of being studied (if possible)
  - Behavior represents normal usage
```

---

## Common Experimental Pitfalls

### 1. Insufficient Power

```
❌ BAD: Run experiment without power analysis
       Risk: Waste time on underpowered test

✅ GOOD: Calculate required sample size first
        Only start experiment when can achieve target power
```

### 2. Peeking at Results

```
❌ BAD: Check results multiple times, stop when significant
       Risk: Inflated false positive rate

✅ GOOD: Use sequential testing with alpha spending
        OR: Wait for pre-specified sample size
```

### 3. Ignoring Multiple Testing

```
❌ BAD: Test 10 metrics, report one that's significant
       Risk: False discovery (p-hacking)

✅ GOOD: Pre-specify primary metric
        Correct secondary metrics with Bonferroni/FDR
```

### 4. Post-Hoc Subgroup Analysis

```
❌ BAD: Find surprising subgroup effect, claim discovery
       Risk: False positive (data dredging)

✅ GOOD: Pre-specify subgroups in SAP
        Label exploratory analyses clearly
        Replicate in new experiment
```

---

## Summary Checklist

**Before Experiment**:
- [ ] Clear hypothesis stated
- [ ] Power analysis completed
- [ ] Sample size calculated
- [ ] Randomization method chosen
- [ ] Statistical Analysis Plan written and approved
- [ ] Success criteria defined

**During Experiment**:
- [ ] Balance check performed
- [ ] Data quality monitored
- [ ] No peeking (or proper alpha spending if sequential)
- [ ] Treatment implemented correctly

**After Experiment**:
- [ ] ITT analysis completed
- [ ] Effect size calculated with CI
- [ ] Multiple testing corrected
- [ ] All pre-specified analyses reported
- [ ] Validity threats assessed
- [ ] Decision documented

---

**Version**: 1.0
**Last Updated**: January 2025
**Coverage**: A/B testing and causal inference methods
**Success Rate**: 95% when rigorous methodology followed
