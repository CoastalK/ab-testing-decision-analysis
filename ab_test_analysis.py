#!/usr/bin/env python3
"""
A/B Test Analysis - Standalone Script
======================================

This script performs the same analysis as the Jupyter notebook but as
a standalone Python script. Useful for automation or command-line execution.

Usage:
    python ab_test_analysis.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.power import zt_ind_solve_power
from statsmodels.stats.proportion import proportion_effectsize
import warnings

warnings.filterwarnings('ignore')


class ABTestAnalyzer:
    """A/B Test Statistical Analysis Framework"""
    
    def __init__(self, control_rate=0.12, treatment_rate=0.145, 
                 n_per_group=5000, alpha=0.05):
        """
        Initialize the A/B test analyzer.
        
        Parameters:
        -----------
        control_rate : float
            Baseline conversion rate for control group
        treatment_rate : float
            Conversion rate for treatment group
        n_per_group : int
            Sample size per group
        alpha : float
            Significance level (default 0.05)
        """
        self.control_rate = control_rate
        self.treatment_rate = treatment_rate
        self.n_per_group = n_per_group
        self.alpha = alpha
        
        # Set random seed for reproducibility
        np.random.seed(42)
        
        # Generate data
        self.df = self._generate_data()
        
        # Results storage
        self.results = {}
        
    def _generate_data(self):
        """Generate simulated A/B test data"""
        control_conversions = np.random.binomial(1, self.control_rate, 
                                                  self.n_per_group)
        treatment_conversions = np.random.binomial(1, self.treatment_rate, 
                                                    self.n_per_group)
        
        df = pd.DataFrame({
            'user_id': range(1, 2 * self.n_per_group + 1),
            'group': ['Control'] * self.n_per_group + ['Treatment'] * self.n_per_group,
            'converted': np.concatenate([control_conversions, treatment_conversions])
        })
        
        return df
    
    def calculate_basic_metrics(self):
        """Calculate conversion rates and lift"""
        summary = self.df.groupby('group')['converted'].agg(['sum', 'count', 'mean'])
        
        control_rate = summary.loc['Control', 'mean']
        treatment_rate = summary.loc['Treatment', 'mean']
        
        absolute_lift = treatment_rate - control_rate
        relative_lift = (treatment_rate / control_rate - 1) * 100
        
        self.results['control_rate'] = control_rate
        self.results['treatment_rate'] = treatment_rate
        self.results['absolute_lift'] = absolute_lift
        self.results['relative_lift'] = relative_lift
        
        return summary
    
    def run_hypothesis_test(self):
        """Perform two-proportion z-test"""
        control_data = self.df[self.df['group'] == 'Control']['converted']
        treatment_data = self.df[self.df['group'] == 'Treatment']['converted']
        
        control_conv = control_data.sum()
        control_n = len(control_data)
        treatment_conv = treatment_data.sum()
        treatment_n = len(treatment_data)
        
        # Pooled proportion
        pooled_prob = (control_conv + treatment_conv) / (control_n + treatment_n)
        pooled_se = np.sqrt(pooled_prob * (1 - pooled_prob) * 
                           (1/control_n + 1/treatment_n))
        
        # Z-statistic
        z_stat = (self.results['treatment_rate'] - self.results['control_rate']) / pooled_se
        
        # P-value (two-tailed)
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
        
        # T-test for verification
        t_stat, t_pvalue = stats.ttest_ind(treatment_data, control_data)
        
        self.results['z_stat'] = z_stat
        self.results['p_value'] = p_value
        self.results['t_stat'] = t_stat
        self.results['t_pvalue'] = t_pvalue
        
        return z_stat, p_value
    
    def calculate_confidence_intervals(self):
        """Calculate 95% confidence intervals"""
        def ci(successes, n, confidence=0.95):
            prop = successes / n
            z_critical = stats.norm.ppf(1 - (1 - confidence) / 2)
            se = np.sqrt(prop * (1 - prop) / n)
            margin = z_critical * se
            return (prop - margin, prop + margin)
        
        control_data = self.df[self.df['group'] == 'Control']['converted']
        treatment_data = self.df[self.df['group'] == 'Treatment']['converted']
        
        control_ci = ci(control_data.sum(), len(control_data))
        treatment_ci = ci(treatment_data.sum(), len(treatment_data))
        
        # CI for difference
        diff = self.results['treatment_rate'] - self.results['control_rate']
        se_diff = np.sqrt(
            (self.results['control_rate'] * (1 - self.results['control_rate']) / self.n_per_group) +
            (self.results['treatment_rate'] * (1 - self.results['treatment_rate']) / self.n_per_group)
        )
        z_critical = 1.96
        diff_ci = (diff - z_critical * se_diff, diff + z_critical * se_diff)
        
        self.results['control_ci'] = control_ci
        self.results['treatment_ci'] = treatment_ci
        self.results['diff_ci'] = diff_ci
        
        return control_ci, treatment_ci, diff_ci
    
    def calculate_effect_size(self):
        """Calculate Cohen's h effect size"""
        h = 2 * (np.arcsin(np.sqrt(self.results['treatment_rate'])) - 
                 np.arcsin(np.sqrt(self.results['control_rate'])))
        
        if abs(h) < 0.2:
            category = "Small"
        elif abs(h) < 0.5:
            category = "Medium"
        else:
            category = "Large"
        
        self.results['cohens_h'] = h
        self.results['effect_category'] = category
        
        return h, category
    
    def calculate_power(self):
        """Calculate statistical power"""
        effect_size = proportion_effectsize(self.results['control_rate'], 
                                           self.results['treatment_rate'])
        
        achieved_power = zt_ind_solve_power(
            effect_size=effect_size,
            nobs1=self.n_per_group,
            alpha=self.alpha,
            ratio=1.0,
            alternative='two-sided'
        )
        
        required_n = zt_ind_solve_power(
            effect_size=effect_size,
            power=0.8,
            alpha=self.alpha,
            ratio=1.0,
            alternative='two-sided'
        )
        
        self.results['achieved_power'] = achieved_power
        self.results['required_n'] = required_n
        
        return achieved_power, required_n
    
    def calculate_business_impact(self, monthly_visitors=100000, avg_order_value=75):
        """Calculate projected business impact"""
        current_conversions = monthly_visitors * self.results['control_rate']
        projected_conversions = monthly_visitors * self.results['treatment_rate']
        
        current_revenue = current_conversions * avg_order_value
        projected_revenue = projected_conversions * avg_order_value
        
        additional_conversions = projected_conversions - current_conversions
        additional_revenue = projected_revenue - current_revenue
        
        self.results['monthly_visitors'] = monthly_visitors
        self.results['avg_order_value'] = avg_order_value
        self.results['additional_conversions'] = additional_conversions
        self.results['additional_revenue'] = additional_revenue
        
        return additional_revenue
    
    def run_full_analysis(self):
        """Run complete A/B test analysis pipeline"""
        print("=" * 70)
        print(" " * 20 + "A/B TEST ANALYSIS")
        print("=" * 70)
        
        # Basic metrics
        print("\n1. BASIC METRICS")
        print("-" * 70)
        self.calculate_basic_metrics()
        print(f"Control Rate: {self.results['control_rate']:.2%}")
        print(f"Treatment Rate: {self.results['treatment_rate']:.2%}")
        print(f"Absolute Lift: {self.results['absolute_lift']:.2%}")
        print(f"Relative Lift: {self.results['relative_lift']:.2f}%")
        
        # Hypothesis test
        print("\n2. HYPOTHESIS TEST")
        print("-" * 70)
        self.run_hypothesis_test()
        print(f"Z-statistic: {self.results['z_stat']:.4f}")
        print(f"P-value: {self.results['p_value']:.4f}")
        print(f"Significance level: {self.alpha}")
        
        is_significant = self.results['p_value'] < self.alpha
        print(f"\nResult: {'✅ STATISTICALLY SIGNIFICANT' if is_significant else '❌ NOT SIGNIFICANT'}")
        
        # Confidence intervals
        print("\n3. CONFIDENCE INTERVALS")
        print("-" * 70)
        self.calculate_confidence_intervals()
        print(f"Control 95% CI: [{self.results['control_ci'][0]:.2%}, {self.results['control_ci'][1]:.2%}]")
        print(f"Treatment 95% CI: [{self.results['treatment_ci'][0]:.2%}, {self.results['treatment_ci'][1]:.2%}]")
        print(f"Difference 95% CI: [{self.results['diff_ci'][0]:.2%}, {self.results['diff_ci'][1]:.2%}]")
        
        # Effect size
        print("\n4. EFFECT SIZE")
        print("-" * 70)
        self.calculate_effect_size()
        print(f"Cohen's h: {self.results['cohens_h']:.4f}")
        print(f"Effect category: {self.results['effect_category']}")
        
        # Power analysis
        print("\n5. POWER ANALYSIS")
        print("-" * 70)
        self.calculate_power()
        print(f"Achieved power: {self.results['achieved_power']:.2%}")
        print(f"Required sample size for 80% power: {self.results['required_n']:,.0f} per group")
        
        # Business impact
        print("\n6. BUSINESS IMPACT")
        print("-" * 70)
        self.calculate_business_impact()
        print(f"Additional monthly conversions: {self.results['additional_conversions']:,.0f}")
        print(f"Additional monthly revenue: ${self.results['additional_revenue']:,.2f}")
        print(f"Additional annual revenue: ${self.results['additional_revenue'] * 12:,.2f}")
        
        # Final recommendation
        print("\n7. RECOMMENDATION")
        print("=" * 70)
        if is_significant and self.results['diff_ci'][0] > 0:
            print("\n✅ PROCEED WITH ROLLOUT")
            print("\nThe new button design shows statistically significant improvement.")
            print(f"Expected annual revenue impact: ${self.results['additional_revenue'] * 12:,.2f}")
        else:
            print("\n⚠️  INSUFFICIENT EVIDENCE - DO NOT PROCEED")
            print("\nThe difference is not statistically significant.")
            print("Consider extending the test or trying a different design.")
        
        print("\n" + "=" * 70)
        
        return self.results
    
    def create_visualizations(self, save_dir='outputs'):
        """Generate and save visualizations"""
        import os
        os.makedirs(save_dir, exist_ok=True)
        
        sns.set_style('whitegrid')
        
        # Conversion rate comparison
        fig, ax = plt.subplots(figsize=(10, 6))
        rates = [self.results['control_rate'] * 100, 
                 self.results['treatment_rate'] * 100]
        groups = ['Control', 'Treatment']
        colors = ['#3498db', '#e74c3c']
        
        bars = ax.bar(groups, rates, color=colors, alpha=0.7, edgecolor='black')
        ax.set_ylabel('Conversion Rate (%)', fontsize=12, fontweight='bold')
        ax.set_title('A/B Test: Conversion Rate Comparison', 
                    fontsize=14, fontweight='bold')
        
        for bar, rate in zip(bars, rates):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{rate:.2f}%', ha='center', va='bottom', 
                   fontsize=12, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(f'{save_dir}/conversion_comparison.png', dpi=300, bbox_inches='tight')
        print(f"\n✅ Saved visualization to {save_dir}/conversion_comparison.png")
        plt.close()


def main():
    """Main execution function"""
    print("\n🚀 Starting A/B Test Analysis...\n")
    
    # Initialize analyzer
    analyzer = ABTestAnalyzer(
        control_rate=0.12,
        treatment_rate=0.145,
        n_per_group=5000,
        alpha=0.05
    )
    
    # Run analysis
    results = analyzer.run_full_analysis()
    
    # Create visualizations
    try:
        analyzer.create_visualizations()
    except Exception as e:
        print(f"\n⚠️  Could not create visualizations: {e}")
    
    # Save results
    results_df = pd.DataFrame([results])
    results_df.to_csv('outputs/ab_test_results.csv', index=False)
    print(f"\n✅ Saved results to outputs/ab_test_results.csv")
    
    print("\n🎉 Analysis complete!")
    
    return analyzer, results


if __name__ == "__main__":
    analyzer, results = main()
