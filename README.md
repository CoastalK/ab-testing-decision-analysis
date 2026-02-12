# A/B Test Decision Analysis 📊

A comprehensive Jupyter notebook demonstrating A/B testing methodology, statistical hypothesis testing, and data-driven decision making. This project showcases the complete workflow from data generation to business recommendations.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🎯 Project Overview

This project analyzes a simulated A/B test comparing two checkout button designs for an e-commerce website:
- **Control (A):** Current green "Checkout" button
- **Treatment (B):** New orange "Complete Purchase" button

**Key Question:** Should we roll out the new button design based on the test results?

## 📚 What You'll Learn

### Statistical Concepts
- **Hypothesis Testing:** Null vs. alternative hypotheses, p-values, significance levels
- **Two-Proportion Z-Test:** Comparing conversion rates between groups
- **T-Tests:** Alternative approach for binary outcomes
- **Confidence Intervals:** Understanding uncertainty in our estimates
- **Effect Size:** Cohen's h for measuring practical significance
- **Statistical Power:** Ensuring adequate sample size

### Business Skills
- Converting statistical findings into business recommendations
- Calculating revenue impact from conversion rate changes
- Balancing statistical significance with practical significance
- Communicating technical results to non-technical stakeholders

### Data Science Workflow
1. Data generation and exploration
2. Descriptive statistics and visualization
3. Statistical testing and inference
4. Interpretation and decision making
5. Business impact quantification

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.8 or higher
python --version

# Recommended: Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ab-testing-decision-analysis.git
cd ab-testing-decision-analysis

# Install required packages
pip install -r requirements.txt

# Launch Jupyter Notebook
jupyter notebook ab_test_analysis.ipynb
```

## 📦 Dependencies

- **numpy** (≥1.21.0): Numerical computing and array operations
- **pandas** (≥1.3.0): Data manipulation and analysis
- **matplotlib** (≥3.4.0): Data visualization
- **seaborn** (≥0.11.0): Statistical data visualization
- **scipy** (≥1.7.0): Scientific computing and statistical tests
- **statsmodels** (≥0.13.0): Statistical modeling and power analysis
- **jupyter** (≥1.0.0): Interactive notebook environment

## 📊 Project Structure

```
ab-testing-decision-analysis/
│
├── ab_test_analysis.ipynb    # Main analysis notebook
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── LICENSE                    # MIT License
└── data/                      # (Generated during runtime)
    └── sample_data.csv        # Simulated A/B test data
```

## 🔍 Notebook Sections

### 1. **Setup & Data Generation**
- Import libraries
- Create realistic simulated test data (10,000 users)
- Define test parameters

### 2. **Exploratory Data Analysis**
- Calculate conversion rates by group
- Compute absolute and relative lift
- Visualize results with bar charts

### 3. **Hypothesis Testing**
- Set up null and alternative hypotheses
- Perform two-proportion z-test
- Validate with two-sample t-test
- Interpret p-values

### 4. **Confidence Intervals**
- Calculate 95% CIs for each group
- Determine CI for the difference
- Visualize uncertainty ranges

### 5. **Statistical Significance**
- Interpret p-values in plain English
- Make statistical decisions
- Understand Type I and Type II errors

### 6. **Effect Size & Business Impact**
- Calculate Cohen's h
- Project revenue impact
- Assess practical significance

### 7. **Power Analysis**
- Evaluate achieved statistical power
- Calculate required sample sizes
- Validate test design

### 8. **Conclusion & Recommendations**
- Synthesize findings
- Provide actionable business recommendations
- Suggest next steps

### 9. **Key Learnings**
- Statistical vs. practical significance
- Sample size importance
- Business context integration

## 💡 Key Insights from the Analysis

Based on our simulated data:

- **Conversion Rate Improvement:** ~2.5 percentage points (20% relative lift)
- **Statistical Significance:** p < 0.05 (statistically significant)
- **95% Confidence Interval:** Improvement between 1.2% - 3.8%
- **Effect Size:** Medium effect (Cohen's h ≈ 0.3)
- **Business Impact:** $225,000+ additional annual revenue (hypothetical)

**Recommendation:** ✅ Proceed with rollout of the new button design

## 🎓 Skills Demonstrated

### Statistics & Mathematics
- ✅ Hypothesis testing (z-tests, t-tests)
- ✅ Confidence interval calculation
- ✅ Effect size analysis
- ✅ Power analysis and sample size determination
- ✅ Understanding of p-values and significance levels

### Programming & Data Science
- ✅ Python programming
- ✅ NumPy and Pandas for data manipulation
- ✅ Matplotlib and Seaborn for visualization
- ✅ SciPy and Statsmodels for statistical analysis
- ✅ Jupyter notebooks for reproducible research

### Business Acumen
- ✅ Translating technical results to business language
- ✅ Revenue impact quantification
- ✅ Decision-making under uncertainty
- ✅ Stakeholder communication

### Teaching & Communication
- ✅ Clear explanations of complex concepts
- ✅ Visual storytelling with data
- ✅ Step-by-step documentation
- ✅ Plain English interpretations

## 🔄 Customization

### Modify Test Parameters

Edit the notebook's data generation section:

```python
# Adjust these parameters to explore different scenarios
n_control = 5000                    # Sample size for control group
n_treatment = 5000                  # Sample size for treatment group
control_conversion_rate = 0.12      # Baseline conversion rate
treatment_conversion_rate = 0.145   # New conversion rate
```

### Change Business Assumptions

Update the business impact section:

```python
monthly_visitors = 100000  # Your website traffic
avg_order_value = 75       # Your average transaction value
```

## 📈 Use Cases

This notebook is perfect for:

- **Data science portfolios:** Demonstrates end-to-end analysis skills
- **Interview preparation:** Common analytics case study
- **Learning A/B testing:** Comprehensive educational resource
- **Teaching statistics:** Ready-to-use classroom material
- **Business stakeholders:** Template for experiment analysis

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

- 🐛 Report bugs or issues
- 💡 Suggest new features or analyses
- 📝 Improve documentation
- 🎨 Enhance visualizations
- 🧪 Add new statistical tests

Please open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Statistical methods based on standard industry practices
- Inspired by real-world A/B testing at companies like Google, Netflix, and Amazon
- Designed for decision science and analytics professionals

## 📬 Contact

**Questions or feedback?** Feel free to reach out:

- GitHub: [@CoastalK](https://github.com/yourusername)
- LinkedIn: [Kylie Harris]([https://linkedin.com/in/yourprofile](https://www.linkedin.com/in/kylie-harris-168722230 ))

---

## 🎯 Why This Project Matters

> "In God we trust, all others must bring data." - W. Edwards Deming

A/B testing is the foundation of data-driven decision making in modern business. This project demonstrates:

1. **Rigor:** Proper statistical methodology, not just "eyeballing" results
2. **Clarity:** Complex statistics explained in accessible language
3. **Impact:** Connecting analysis to real business outcomes
4. **Reproducibility:** Fully documented, runnable code

Whether you're interviewing for a data science role, learning statistics, or making business decisions, this notebook provides a solid foundation in experimental analysis.

---

⭐ **If you found this helpful, please consider giving it a star!** ⭐

