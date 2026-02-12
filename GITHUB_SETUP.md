# GitHub Setup Guide

Follow these steps to upload your A/B Testing project to GitHub.

## Step 1: Install Git (if not already installed)

**Windows:**
- Download from https://git-scm.com/download/win
- Run the installer with default settings

**Mac:**
```bash
brew install git
```

**Linux:**
```bash
sudo apt-get install git  # Ubuntu/Debian
sudo yum install git      # CentOS/RHEL
```

## Step 2: Configure Git (First Time Only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Step 3: Create GitHub Repository

1. Go to https://github.com
2. Click the "+" icon → "New repository"
3. Repository name: `ab-testing-decision-analysis`
4. Description: "Statistical A/B test analysis demonstrating hypothesis testing, confidence intervals, and data-driven decision making"
5. Choose "Public"
6. **DO NOT** initialize with README (we already have one)
7. Click "Create repository"

## Step 4: Upload Your Project

Open terminal/command prompt in your project folder and run:

```bash
# Navigate to your project directory
cd /path/to/ab-testing-decision-analysis

# Initialize git repository
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: A/B test analysis notebook with statistical testing"

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR-USERNAME/ab-testing-decision-analysis.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Replace `YOUR-USERNAME` with your actual GitHub username!**

## Step 5: Verify Upload

1. Go to `https://github.com/YOUR-USERNAME/ab-testing-decision-analysis`
2. You should see all your files
3. The README.md will display automatically

## Step 6: Make Your Repo Stand Out

### Add Topics/Tags
1. Click the gear icon next to "About" on your repo page
2. Add topics: `statistics`, `ab-testing`, `data-science`, `hypothesis-testing`, `python`, `jupyter-notebook`, `decision-science`

### Add a Description
Add this description:
"Statistical A/B test analysis with hypothesis testing, confidence intervals, effect size calculations, and business impact quantification. Perfect for data science portfolios."

### Enable GitHub Pages (Optional - for live notebook viewing)
1. Go to Settings → Pages
2. Source: Deploy from branch
3. Branch: main, /root
4. Save

## Common Git Commands for Future Updates

```bash
# Check status of changes
git status

# Add new/modified files
git add .

# Commit changes
git commit -m "Description of what you changed"

# Push to GitHub
git push

# Pull latest changes (if working from multiple computers)
git pull
```

## Troubleshooting

**Error: "fatal: remote origin already exists"**
```bash
git remote remove origin
git remote add origin https://github.com/YOUR-USERNAME/ab-testing-decision-analysis.git
```

**Error: Permission denied (publickey)**
- Use HTTPS instead of SSH for simpler setup
- Or set up SSH keys: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

**Error: "Updates were rejected because the remote contains work"**
```bash
git pull origin main --rebase
git push origin main
```

## Next Steps

1. ✅ Upload project to GitHub
2. 📝 Customize README with your contact info
3. 🎨 Run the notebook and add screenshots to README
4. 🔗 Share the link on LinkedIn
5. 💼 Add to your resume/portfolio

## Tips for LinkedIn Post

When sharing your project:

> 🎯 Just completed an A/B testing analysis project!
> 
> Built a comprehensive Jupyter notebook demonstrating:
> ✅ Hypothesis testing (z-tests, t-tests)
> ✅ Confidence intervals & effect size
> ✅ Statistical power analysis
> ✅ Business impact quantification
> 
> This project showcases how data science drives real business decisions - exactly the kind of work I want to do at [Company Name].
> 
> Check it out: [GitHub link]
> 
> #DataScience #ABTesting #Statistics #Python #Analytics

---

Need help? Create an issue on GitHub or reach out!
