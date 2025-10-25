#!/usr/bin/env python3
"""
A/B Test Designer and Analyzer

A comprehensive framework for designing, implementing, and analyzing A/B tests
with power analysis, randomization, and statistical rigor.

Author: Data Scientist Plugin
Version: 1.0.0
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportions_ztest, proportion_effectsize, confint_proportions_2indep
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)


class ABTestDesigner:
    """
    A/B Test Designer and Analyzer

    Workflow:
    1. Design experiment (power analysis, sample size)
    2. Implement randomization
    3. Analyze results
    4. Make decision
    """

    def __init__(self, name, description=""):
        """
        Initialize A/B test

        Args:
            name: Experiment name
            description: Experiment description
        """
        self.name = name
        self.description = description
        self.design = {}
        self.results = {}
        self.created_at = datetime.now()

    def design_experiment(self, baseline_rate, mde, alpha=0.05, power=0.80, ratio=1):
        """
        Design A/B test with power analysis

        Args:
            baseline_rate: Current conversion rate (e.g., 0.10 for 10%)
            mde: Minimum detectable effect (absolute, e.g., 0.02 for 2 percentage points)
            alpha: Significance level (default 0.05)
            power: Statistical power (default 0.80)
            ratio: Ratio of treatment to control (default 1 for equal allocation)

        Returns:
            dict: Design specifications
        """
        print("=" * 70)
        print(f"A/B TEST DESIGN: {self.name}")
        print("=" * 70)

        # Target rate
        target_rate = baseline_rate + mde

        # Effect size (Cohen's h for proportions)
        effect_size = proportion_effectsize(baseline_rate, target_rate)

        # Power analysis
        power_analyzer = NormalIndPower()
        sample_size_per_group = power_analyzer.solve_power(
            effect_size=effect_size,
            alpha=alpha,
            power=power,
            ratio=ratio,
            alternative='two-sided'
        )

        # Round up
        sample_size_per_group = int(np.ceil(sample_size_per_group))
        total_sample_size = int(sample_size_per_group * (1 + ratio))

        # Store design
        self.design = {
            'baseline_rate': baseline_rate,
            'target_rate': target_rate,
            'mde_absolute': mde,
            'mde_relative': (mde / baseline_rate) * 100 if baseline_rate > 0 else 0,
            'alpha': alpha,
            'power': power,
            'effect_size': effect_size,
            'sample_size_per_group': sample_size_per_group,
            'total_sample_size': total_sample_size,
            'ratio': ratio
        }

        # Print design
        print(f"\nExperiment: {self.name}")
        if self.description:
            print(f"Description: {self.description}")

        print(f"\n" + "-" * 70)
        print("HYPOTHESIS")
        print("-" * 70)
        print(f"H0 (null): Control rate = Treatment rate")
        print(f"H1 (alternative): Control rate ≠ Treatment rate")
        print(f"Significance level: α = {alpha}")

        print(f"\n" + "-" * 70)
        print("BASELINE ASSUMPTIONS")
        print("-" * 70)
        print(f"Current conversion rate: {baseline_rate:.4%}")
        print(f"Target conversion rate: {target_rate:.4%}")
        print(f"Minimum detectable effect:")
        print(f"  Absolute: {mde:+.4%}")
        print(f"  Relative: {self.design['mde_relative']:+.2f}%")

        print(f"\n" + "-" * 70)
        print("STATISTICAL PARAMETERS")
        print("-" * 70)
        print(f"Significance level (α): {alpha}")
        print(f"Statistical power (1-β): {power}")
        print(f"Effect size (Cohen's h): {effect_size:.4f}")

        print(f"\n" + "-" * 70)
        print("REQUIRED SAMPLE SIZE")
        print("-" * 70)
        print(f"Per group: {sample_size_per_group:,}")
        print(f"Total: {total_sample_size:,}")
        print(f"Allocation ratio (Treatment:Control): {ratio}:1")

        # Generate power curve
        self._plot_power_curve()

        return self.design

    def _plot_power_curve(self):
        """Generate and save power curve visualization"""
        if not self.design:
            print("Error: Must run design_experiment first")
            return

        baseline = self.design['baseline_rate']
        sample_size = self.design['sample_size_per_group']
        alpha = self.design['alpha']

        # Range of effect sizes
        mde_range = np.linspace(0.005, 0.10, 100)  # 0.5% to 10%
        powers = []

        power_analyzer = NormalIndPower()

        for mde in mde_range:
            target = baseline + mde
            effect_size = proportion_effectsize(baseline, target)

            power = power_analyzer.solve_power(
                effect_size=effect_size,
                alpha=alpha,
                nobs1=sample_size,
                ratio=1,
                alternative='two-sided'
            )
            powers.append(power)

        # Plot
        plt.figure(figsize=(10, 6))
        plt.plot(mde_range * 100, powers, linewidth=2)
        plt.axhline(y=0.80, color='r', linestyle='--', linewidth=1, label='80% power')
        plt.axhline(y=0.90, color='orange', linestyle='--', linewidth=1, label='90% power')
        plt.axvline(x=self.design['mde_absolute'] * 100, color='green',
                   linestyle='--', linewidth=1, label='Target MDE')
        plt.xlabel('Absolute Lift (percentage points)', fontsize=12)
        plt.ylabel('Statistical Power', fontsize=12)
        plt.title(f'Power Curve (n={sample_size:,} per group, baseline={baseline:.1%})',
                 fontsize=14)
        plt.grid(True, alpha=0.3)
        plt.legend(fontsize=10)
        plt.tight_layout()
        plt.savefig('ab_test_power_curve.png', dpi=300, bbox_inches='tight')
        print("\n✓ Power curve saved: ab_test_power_curve.png")
        plt.close()

    def randomize(self, user_ids, seed=42):
        """
        Randomly assign users to control or treatment

        Args:
            user_ids: List or array of user IDs
            seed: Random seed for reproducibility

        Returns:
            DataFrame with user assignments
        """
        if not self.design:
            print("Error: Must run design_experiment first")
            return None

        np.random.seed(seed)

        # Simple randomization (50/50)
        n_users = len(user_ids)
        assignments = np.random.binomial(1, 0.5, n_users)

        # Create DataFrame
        df = pd.DataFrame({
            'user_id': user_ids,
            'treatment': assignments
        })

        # Summary
        control_count = (assignments == 0).sum()
        treatment_count = (assignments == 1).sum()

        print("\n" + "=" * 70)
        print("RANDOMIZATION")
        print("=" * 70)
        print(f"\nTotal users: {n_users:,}")
        print(f"Control: {control_count:,} ({control_count/n_users:.1%})")
        print(f"Treatment: {treatment_count:,} ({treatment_count/n_users:.1%})")
        print(f"Random seed: {seed}")

        return df

    def analyze(self, df, treatment_col='treatment', outcome_col='converted'):
        """
        Analyze A/B test results

        Args:
            df: DataFrame with experiment data
            treatment_col: Column name for treatment assignment (0=control, 1=treatment)
            outcome_col: Column name for outcome (0=no, 1=yes)

        Returns:
            dict: Analysis results
        """
        print("\n" + "=" * 70)
        print(f"A/B TEST ANALYSIS: {self.name}")
        print("=" * 70)

        # Summary statistics by group
        summary = df.groupby(treatment_col)[outcome_col].agg(['sum', 'count', 'mean'])
        summary.columns = ['conversions', 'total', 'rate']
        summary.index = ['Control', 'Treatment']

        # Extract values
        conversions = summary['conversions'].values
        totals = summary['total'].values
        rates = summary['rate'].values

        print(f"\n" + "-" * 70)
        print("SAMPLE SIZES")
        print("-" * 70)
        print(summary[['total', 'conversions']])

        print(f"\n" + "-" * 70)
        print("CONVERSION RATES")
        print("-" * 70)
        print(f"Control:   {rates[0]:.4%} ({conversions[0]}/{totals[0]})")
        print(f"Treatment: {rates[1]:.4%} ({conversions[1]}/{totals[1]})")

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

        # Store results
        self.results = {
            'control_rate': rates[0],
            'treatment_rate': rates[1],
            'absolute_lift': absolute_lift,
            'relative_lift': relative_lift,
            'z_statistic': z_stat,
            'p_value': p_value,
            'ci_low': ci_low,
            'ci_high': ci_high,
            'control_n': totals[0],
            'treatment_n': totals[1],
            'significant': p_value < self.design['alpha']
        }

        print(f"\n" + "-" * 70)
        print("EFFECT SIZE")
        print("-" * 70)
        print(f"Absolute lift: {absolute_lift:+.4%}")
        print(f"Relative lift: {relative_lift:+.2f}%")
        print(f"95% CI for difference: [{ci_low:.4%}, {ci_high:.4%}]")

        print(f"\n" + "-" * 70)
        print("STATISTICAL TEST")
        print("-" * 70)
        print(f"Test: Two-proportion z-test")
        print(f"z-statistic: {z_stat:.4f}")
        print(f"p-value: {p_value:.4f}")

        # Decision
        alpha = self.design['alpha']

        print(f"\n" + "=" * 70)
        print("DECISION")
        print("=" * 70)
        print(f"\nSignificance level: α = {alpha}")

        if p_value < alpha:
            direction = "increases" if absolute_lift > 0 else "decreases"
            print(f"\n✓ SIGNIFICANT: Treatment {direction} conversion rate")
            print(f"  Relative change: {abs(relative_lift):.1f}% {direction}")
            print(f"  Statistical evidence: p = {p_value:.4f} < {alpha}")

            # Practical significance
            if abs(absolute_lift) >= self.design['mde_absolute']:
                print(f"  ✓ Effect meets minimum detectable effect threshold")
            else:
                print(f"  ⚠ Effect is smaller than target MDE ({self.design['mde_absolute']:.4%})")

        else:
            print(f"\n✗ NOT SIGNIFICANT: No evidence of treatment effect")
            print(f"  p = {p_value:.4f} ≥ {alpha}")
            print(f"  Cannot conclude treatment has an effect")

        # Visualizations
        self._plot_results(summary)

        return self.results

    def _plot_results(self, summary):
        """Generate result visualizations"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        # Bar plot of conversion rates
        rates = summary['rate'].values
        groups = ['Control', 'Treatment']
        colors = ['#3498db', '#e74c3c']

        axes[0].bar(groups, rates, color=colors, alpha=0.7, edgecolor='black')
        axes[0].set_ylabel('Conversion Rate', fontsize=12)
        axes[0].set_title('Conversion Rate by Group', fontsize=14)
        axes[0].set_ylim(0, max(rates) * 1.2)

        # Add value labels
        for i, (group, rate) in enumerate(zip(groups, rates)):
            axes[0].text(i, rate + max(rates)*0.02, f'{rate:.2%}',
                        ha='center', fontsize=11, fontweight='bold')

        # Add error bars (95% CI)
        for i, row in summary.iterrows():
            n = row['total']
            p = row['rate']
            se = np.sqrt(p * (1-p) / n)
            ci = 1.96 * se
            group_idx = 0 if i == 'Control' else 1
            axes[0].errorbar(group_idx, p, yerr=ci, fmt='none',
                           color='black', capsize=5, capthick=2)

        axes[0].grid(True, alpha=0.3, axis='y')

        # Lift visualization
        absolute_lift = self.results['absolute_lift']
        ci_low = self.results['ci_low']
        ci_high = self.results['ci_high']

        axes[1].barh(['Observed Lift'], [absolute_lift],
                    color='green' if absolute_lift > 0 else 'red', alpha=0.7)
        axes[1].errorbar(absolute_lift, 0, xerr=[[absolute_lift - ci_low], [ci_high - absolute_lift]],
                        fmt='none', color='black', capsize=5, capthick=2)
        axes[1].axvline(x=0, color='black', linestyle='--', linewidth=1)
        axes[1].set_xlabel('Absolute Lift (percentage points)', fontsize=12)
        axes[1].set_title('Treatment Effect with 95% CI', fontsize=14)
        axes[1].grid(True, alpha=0.3, axis='x')

        # Add value labels
        axes[1].text(absolute_lift, 0, f'{absolute_lift:+.2%}',
                    ha='left' if absolute_lift > 0 else 'right',
                    va='center', fontsize=11, fontweight='bold')

        plt.tight_layout()
        plt.savefig('ab_test_results.png', dpi=300, bbox_inches='tight')
        print("\n✓ Results visualization saved: ab_test_results.png")
        plt.close()

    def generate_report(self, output_file='ab_test_report.md'):
        """
        Generate comprehensive markdown report

        Args:
            output_file: Output filename
        """
        if not self.design or not self.results:
            print("Error: Must run design_experiment and analyze first")
            return

        report = f"""# A/B Test Report: {self.name}

**Date**: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}

{f'**Description**: {self.description}' if self.description else ''}

---

## Executive Summary

{self._generate_executive_summary()}

---

## Experiment Design

### Hypotheses
- **H0 (null)**: Control rate = Treatment rate
- **H1 (alternative)**: Control rate ≠ Treatment rate
- **Significance level**: α = {self.design['alpha']}

### Target Metrics
- **Baseline conversion rate**: {self.design['baseline_rate']:.4%}
- **Target conversion rate**: {self.design['target_rate']:.4%}
- **Minimum detectable effect**:
  - Absolute: {self.design['mde_absolute']:+.4%}
  - Relative: {self.design['mde_relative']:+.2f}%

### Sample Size Calculation
- **Statistical power**: {self.design['power']:.0%}
- **Sample size per group**: {self.design['sample_size_per_group']:,}
- **Total sample size**: {self.design['total_sample_size']:,}

---

## Results

### Sample Sizes (Actual)
- **Control**: {self.results['control_n']:,}
- **Treatment**: {self.results['treatment_n']:,}
- **Total**: {self.results['control_n'] + self.results['treatment_n']:,}

### Conversion Rates
- **Control**: {self.results['control_rate']:.4%}
- **Treatment**: {self.results['treatment_rate']:.4%}

### Effect Size
- **Absolute lift**: {self.results['absolute_lift']:+.4%}
- **Relative lift**: {self.results['relative_lift']:+.2f}%
- **95% Confidence Interval**: [{self.results['ci_low']:.4%}, {self.results['ci_high']:.4%}]

### Statistical Test
- **Test**: Two-proportion z-test
- **z-statistic**: {self.results['z_statistic']:.4f}
- **p-value**: {self.results['p_value']:.4f}

---

## Decision

**Result**: {'SIGNIFICANT ✓' if self.results['significant'] else 'NOT SIGNIFICANT ✗'}

{self._generate_recommendation()}

---

## Visualizations

![Power Curve](ab_test_power_curve.png)

![Test Results](ab_test_results.png)

---

## Limitations

1. **Generalizability**: Results may not generalize to different populations or time periods
2. **External validity**: Experiment conducted in specific context
3. **Assumptions**: Assumes independence between users, no network effects

---

## Next Steps

{self._generate_next_steps()}

---

*Report generated automatically by A/B Test Designer*
"""

        # Write report
        with open(output_file, 'w') as f:
            f.write(report)

        print(f"\n✓ Report saved: {output_file}")

    def _generate_executive_summary(self):
        """Generate executive summary for report"""
        if self.results['significant']:
            direction = "increased" if self.results['absolute_lift'] > 0 else "decreased"
            return f"""The treatment {direction} conversion rate by {abs(self.results['relative_lift']):.1f}% \
(from {self.results['control_rate']:.2%} to {self.results['treatment_rate']:.2%}). \
This result is statistically significant (p = {self.results['p_value']:.4f} < {self.design['alpha']}) \
with a {'large' if abs(self.results['absolute_lift']) >= self.design['mde_absolute'] else 'small'} effect size."""
        else:
            return f"""No significant difference was detected between control and treatment \
(p = {self.results['p_value']:.4f} ≥ {self.design['alpha']}). \
The observed lift was {self.results['relative_lift']:+.1f}%, but this could be due to random chance."""

    def _generate_recommendation(self):
        """Generate recommendation based on results"""
        if self.results['significant']:
            if self.results['absolute_lift'] > 0:
                if abs(self.results['absolute_lift']) >= self.design['mde_absolute']:
                    return "**Recommendation**: SHIP - Treatment shows significant improvement meeting target effect size."
                else:
                    return "**Recommendation**: CONSIDER - Treatment is significant but effect is smaller than target. Evaluate business value."
            else:
                return "**Recommendation**: DO NOT SHIP - Treatment significantly decreases conversion rate."
        else:
            return "**Recommendation**: DO NOT SHIP - No evidence of treatment effect. Consider redesigning treatment or running longer experiment."

    def _generate_next_steps(self):
        """Generate next steps"""
        if self.results['significant']:
            return """1. Validate results with additional monitoring
2. Implement treatment for all users
3. Monitor for long-term effects
4. Document learnings"""
        else:
            return """1. Investigate why treatment didn't work
2. Consider alternative treatments
3. Review power analysis and sample size
4. Plan follow-up experiments"""


# ==============================================================================
# EXAMPLE USAGE
# ==============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("A/B TEST DESIGNER - EXAMPLE")
    print("=" * 70)

    # Initialize A/B test
    ab_test = ABTestDesigner(
        name="Checkout Button Color Test",
        description="Testing whether green checkout button increases conversion vs. blue"
    )

    # Design experiment
    design = ab_test.design_experiment(
        baseline_rate=0.10,  # Current 10% conversion rate
        mde=0.02,            # Want to detect 2 percentage point lift (20% relative)
        alpha=0.05,
        power=0.80
    )

    # Simulate randomization
    print("\n")
    user_ids = [f"user_{i}" for i in range(10000)]
    assignments = ab_test.randomize(user_ids, seed=42)

    # Simulate experiment results
    # (In real scenario, this would be actual experimental data)
    np.random.seed(42)
    control_rate = 0.10
    treatment_rate = 0.12  # 20% relative lift

    conversions = []
    for _, row in assignments.iterrows():
        if row['treatment'] == 0:
            converted = np.random.random() < control_rate
        else:
            converted = np.random.random() < treatment_rate
        conversions.append(converted)

    assignments['converted'] = conversions

    # Analyze results
    results = ab_test.analyze(assignments, treatment_col='treatment', outcome_col='converted')

    # Generate report
    ab_test.generate_report('ab_test_report.md')

    print("\n\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)
    print("\nGenerated files:")
    print("  - ab_test_power_curve.png")
    print("  - ab_test_results.png")
    print("  - ab_test_report.md")
