#!/usr/bin/env python3
"""
Hypothesis Testing Template

A comprehensive framework for statistical hypothesis testing with assumption
checking, effect size calculation, and proper interpretation.

Author: Data Scientist Plugin
Version: 1.0.0
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import shapiro, levene, ttest_ind, mannwhitneyu, chi2_contingency
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)


def check_normality(data, name="Data"):
    """
    Test if data follows normal distribution

    Args:
        data: Array-like data
        name: Name for reporting

    Returns:
        bool: True if data appears normally distributed
    """
    # Shapiro-Wilk test
    stat, p_value = shapiro(data)

    print(f"\n{name} - Normality Test (Shapiro-Wilk):")
    print(f"  Statistic: {stat:.4f}")
    print(f"  p-value: {p_value:.4f}")

    if p_value < 0.05:
        print(f"  Result: NOT normally distributed (p < 0.05)")
        return False
    else:
        print(f"  Result: Appears normally distributed (p >= 0.05)")
        return True


def check_equal_variance(group1, group2):
    """
    Test if two groups have equal variance

    Args:
        group1, group2: Array-like data

    Returns:
        bool: True if variances appear equal
    """
    # Levene's test
    stat, p_value = levene(group1, group2)

    print(f"\nEqual Variance Test (Levene's):")
    print(f"  Statistic: {stat:.4f}")
    print(f"  p-value: {p_value:.4f}")

    if p_value < 0.05:
        print(f"  Result: Variances NOT equal (p < 0.05)")
        return False
    else:
        print(f"  Result: Variances appear equal (p >= 0.05)")
        return True


def cohens_d(group1, group2):
    """
    Calculate Cohen's d effect size

    Args:
        group1, group2: Array-like data

    Returns:
        float: Cohen's d effect size

    Interpretation:
        0.2: small effect
        0.5: medium effect
        0.8: large effect
    """
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)

    # Pooled standard deviation
    pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))

    # Cohen's d
    d = (np.mean(group1) - np.mean(group2)) / pooled_std

    return d


def visualize_distributions(group1, group2, name1="Group 1", name2="Group 2"):
    """
    Visualize distributions of two groups

    Args:
        group1, group2: Array-like data
        name1, name2: Names for groups
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Histograms
    axes[0, 0].hist(group1, bins=20, alpha=0.7, label=name1, edgecolor='black')
    axes[0, 0].hist(group2, bins=20, alpha=0.7, label=name2, edgecolor='black')
    axes[0, 0].set_xlabel('Value')
    axes[0, 0].set_ylabel('Frequency')
    axes[0, 0].set_title('Distribution Comparison')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    # Box plots
    data_to_plot = [group1, group2]
    axes[0, 1].boxplot(data_to_plot, labels=[name1, name2])
    axes[0, 1].set_ylabel('Value')
    axes[0, 1].set_title('Box Plot Comparison')
    axes[0, 1].grid(True, alpha=0.3)

    # Q-Q plots
    stats.probplot(group1, dist="norm", plot=axes[1, 0])
    axes[1, 0].set_title(f'{name1} - Q-Q Plot')

    stats.probplot(group2, dist="norm", plot=axes[1, 1])
    axes[1, 1].set_title(f'{name2} - Q-Q Plot')

    plt.tight_layout()
    plt.savefig('distribution_comparison.png', dpi=300, bbox_inches='tight')
    print("\n✓ Visualization saved: distribution_comparison.png")
    plt.close()


def compare_two_groups(group1, group2, name1="Control", name2="Treatment",
                      alpha=0.05, alternative='two-sided'):
    """
    Compare two independent groups with appropriate statistical test

    Args:
        group1, group2: Array-like data
        name1, name2: Names for groups
        alpha: Significance level
        alternative: 'two-sided', 'less', or 'greater'

    Returns:
        dict: Test results
    """
    print("=" * 70)
    print("TWO-GROUP COMPARISON")
    print("=" * 70)

    # Sample sizes
    n1, n2 = len(group1), len(group2)
    print(f"\nSample Sizes:")
    print(f"  {name1}: n = {n1}")
    print(f"  {name2}: n = {n2}")

    # Descriptive statistics
    print(f"\nDescriptive Statistics:")
    print(f"  {name1}: Mean = {np.mean(group1):.4f}, SD = {np.std(group1, ddof=1):.4f}")
    print(f"  {name2}: Mean = {np.mean(group2):.4f}, SD = {np.std(group2, ddof=1):.4f}")

    # Check assumptions
    print("\n" + "=" * 70)
    print("ASSUMPTION CHECKS")
    print("=" * 70)

    normal1 = check_normality(group1, name1)
    normal2 = check_normality(group2, name2)
    equal_var = check_equal_variance(group1, group2)

    # Select appropriate test
    print("\n" + "=" * 70)
    print("STATISTICAL TEST")
    print("=" * 70)

    if normal1 and normal2:
        if equal_var:
            # Independent t-test
            stat, p_value = ttest_ind(group1, group2, alternative=alternative)
            test_name = "Independent t-test"
            print(f"\n✓ Using: {test_name}")
            print(f"  (Both groups normal, equal variances)")
        else:
            # Welch's t-test (unequal variances)
            stat, p_value = ttest_ind(group1, group2, equal_var=False, alternative=alternative)
            test_name = "Welch's t-test"
            print(f"\n✓ Using: {test_name}")
            print(f"  (Both groups normal, unequal variances)")
    else:
        # Mann-Whitney U test (non-parametric)
        stat, p_value = mannwhitneyu(group1, group2, alternative=alternative)
        test_name = "Mann-Whitney U test"
        print(f"\n✓ Using: {test_name}")
        print(f"  (At least one group not normal - non-parametric test)")

    # Calculate effect size
    d = cohens_d(group1, group2)

    # Confidence interval for mean difference (bootstrap)
    np.random.seed(42)
    n_bootstrap = 10000
    bootstrap_diffs = []

    for _ in range(n_bootstrap):
        sample1 = np.random.choice(group1, size=len(group1), replace=True)
        sample2 = np.random.choice(group2, size=len(group2), replace=True)
        bootstrap_diffs.append(np.mean(sample1) - np.mean(sample2))

    ci_low = np.percentile(bootstrap_diffs, 2.5)
    ci_high = np.percentile(bootstrap_diffs, 97.5)

    # Results
    print(f"\n" + "=" * 70)
    print("RESULTS")
    print("=" * 70)

    print(f"\nTest: {test_name}")
    print(f"Test Statistic: {stat:.4f}")
    print(f"p-value: {p_value:.4f}")

    print(f"\nEffect Size (Cohen's d): {d:.4f}")
    if abs(d) < 0.2:
        effect_interpretation = "negligible"
    elif abs(d) < 0.5:
        effect_interpretation = "small"
    elif abs(d) < 0.8:
        effect_interpretation = "medium"
    else:
        effect_interpretation = "large"
    print(f"  Interpretation: {effect_interpretation} effect")

    mean_diff = np.mean(group1) - np.mean(group2)
    print(f"\nMean Difference: {mean_diff:.4f}")
    print(f"95% CI: [{ci_low:.4f}, {ci_high:.4f}]")

    # Decision
    print(f"\n" + "=" * 70)
    print("DECISION")
    print("=" * 70)

    print(f"\nSignificance level: α = {alpha}")

    if p_value < alpha:
        print(f"\n✓ SIGNIFICANT: Reject null hypothesis (p = {p_value:.4f} < {alpha})")
        if mean_diff > 0:
            print(f"  {name1} has significantly higher values than {name2}")
        else:
            print(f"  {name2} has significantly higher values than {name1}")
        print(f"  Effect size: {effect_interpretation}")
    else:
        print(f"\n✗ NOT SIGNIFICANT: Fail to reject null hypothesis (p = {p_value:.4f} >= {alpha})")
        print(f"  No evidence of difference between {name1} and {name2}")

    # Create visualizations
    visualize_distributions(group1, group2, name1, name2)

    return {
        'test': test_name,
        'statistic': stat,
        'p_value': p_value,
        'effect_size': d,
        'mean_diff': mean_diff,
        'ci_low': ci_low,
        'ci_high': ci_high,
        'significant': p_value < alpha
    }


def compare_proportions(success1, n1, success2, n2, name1="Control", name2="Treatment",
                       alpha=0.05):
    """
    Compare two proportions (e.g., conversion rates)

    Args:
        success1, success2: Number of successes
        n1, n2: Sample sizes
        name1, name2: Group names
        alpha: Significance level

    Returns:
        dict: Test results
    """
    print("=" * 70)
    print("PROPORTION COMPARISON")
    print("=" * 70)

    # Calculate proportions
    p1 = success1 / n1
    p2 = success2 / n2

    print(f"\nSample Sizes:")
    print(f"  {name1}: {success1}/{n1} = {p1:.4%}")
    print(f"  {name2}: {success2}/{n2} = {p2:.4%}")

    # Create contingency table
    table = np.array([
        [success1, n1 - success1],
        [success2, n2 - success2]
    ])

    # Check expected frequencies
    expected = (table.sum(axis=0) * table.sum(axis=1)[:, None]) / table.sum()

    print("\n" + "=" * 70)
    print("STATISTICAL TEST")
    print("=" * 70)

    if (expected >= 5).all():
        # Chi-square test
        chi2, p_value, dof, expected = chi2_contingency(table)
        test_name = "Chi-square test"
        print(f"\n✓ Using: {test_name}")
        print(f"  (All expected frequencies >= 5)")
        print(f"\nChi-square statistic: {chi2:.4f}")
    else:
        # Fisher's exact test
        from scipy.stats import fisher_exact
        odds_ratio, p_value = fisher_exact(table)
        test_name = "Fisher's exact test"
        print(f"\n✓ Using: {test_name}")
        print(f"  (Some expected frequencies < 5)")
        print(f"\nOdds ratio: {odds_ratio:.4f}")

    print(f"p-value: {p_value:.4f}")

    # Effect size (relative risk and absolute difference)
    relative_risk = p2 / p1 if p1 > 0 else np.inf
    absolute_diff = p2 - p1

    print(f"\n" + "=" * 70)
    print("EFFECT SIZE")
    print("=" * 70)

    print(f"\nAbsolute difference: {absolute_diff:+.4%}")
    print(f"Relative risk: {relative_risk:.4f}")
    if p1 > 0:
        relative_lift = ((p2 - p1) / p1) * 100
        print(f"Relative lift: {relative_lift:+.2f}%")

    # Confidence interval for difference
    from statsmodels.stats.proportion import confint_proportions_2indep
    ci_low, ci_high = confint_proportions_2indep(success1, n1, success2, n2)

    print(f"95% CI for difference: [{ci_low:.4%}, {ci_high:.4%}]")

    # Decision
    print(f"\n" + "=" * 70)
    print("DECISION")
    print("=" * 70)

    if p_value < alpha:
        print(f"\n✓ SIGNIFICANT: Proportions differ (p = {p_value:.4f} < {alpha})")
        if absolute_diff > 0:
            print(f"  {name2} has higher proportion than {name1}")
        else:
            print(f"  {name1} has higher proportion than {name2}")
    else:
        print(f"\n✗ NOT SIGNIFICANT: No evidence of difference (p = {p_value:.4f} >= {alpha})")

    return {
        'test': test_name,
        'p_value': p_value,
        'prop1': p1,
        'prop2': p2,
        'absolute_diff': absolute_diff,
        'relative_risk': relative_risk,
        'ci_low': ci_low,
        'ci_high': ci_high,
        'significant': p_value < alpha
    }


# ==============================================================================
# EXAMPLE USAGE
# ==============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("HYPOTHESIS TESTING TEMPLATE - EXAMPLE")
    print("=" * 70)

    # Example 1: Compare two continuous variables
    print("\n\nEXAMPLE 1: Comparing Two Groups (Continuous Data)")
    print("-" * 70)

    # Generate sample data
    np.random.seed(42)
    control_group = np.random.normal(100, 15, 50)  # Control: mean=100, sd=15, n=50
    treatment_group = np.random.normal(110, 15, 50)  # Treatment: mean=110, sd=15, n=50

    results1 = compare_two_groups(
        control_group,
        treatment_group,
        name1="Control",
        name2="Treatment",
        alpha=0.05,
        alternative='two-sided'
    )

    # Example 2: Compare two proportions
    print("\n\n")
    print("=" * 70)
    print("EXAMPLE 2: Comparing Two Proportions")
    print("-" * 70)

    results2 = compare_proportions(
        success1=50,   # Control: 50/500 converted
        n1=500,
        success2=70,   # Treatment: 70/500 converted
        n2=500,
        name1="Control",
        name2="Treatment",
        alpha=0.05
    )

    print("\n\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)
    print("\nGenerated files:")
    print("  - distribution_comparison.png")
    print("\nNext steps:")
    print("  1. Review assumption checks")
    print("  2. Interpret effect sizes (not just p-values)")
    print("  3. Consider practical significance")
    print("  4. Document limitations and assumptions")
