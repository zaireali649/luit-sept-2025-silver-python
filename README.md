# luit-sept-2025-silver-python

This repository is for students learning basic Python for the first time.  

## Repository Structure

```
.
├── .github/
│   └── workflows/           # GitHub Actions CI/CD workflows
│       ├── on_pull_request.yaml  # Beta/testing workflow
│       └── on_merge.yaml         # Production deployment workflow
├── prompts/                 # AI prompts for code documentation and PR reviews
│   ├── document_code.txt    # Prompt for adding comments, type hints, and docstrings
│   └── pr_review.txt        # Prompt for generating detailed PR summaries
├── creating_instances.py    # AWS EC2 instance creation with multiple AMI types
├── defining_functions.py    # Python function examples with type hints and docstrings
├── hello_world.py          # Basic "Hello, World!" Python script
├── helpers.py              # AWS utility functions for EC2 and S3 operations
├── list_buckets_lambda.py  # AWS Lambda function to list S3 buckets
├── list_buckets.py         # Simple S3 bucket listing script
├── list_vpc_ids.py         # VPC listing script (used in GitHub Actions)
├── listing_resources.py    # Combined AWS resource listing (EC2 instances + S3 buckets)
├── using_imports.py        # Python imports and library examples
├── requirements.txt        # Python dependencies (boto3)
└── README.md              # Project documentation
```

## Getting Started

### GitHub Setup Options

Choose the method that works best for your computer setup:

#### Option 1: GitHub Desktop (Recommended for Beginners)
1. **Download GitHub Desktop** from [desktop.github.com](https://desktop.github.com)
2. **Sign in** with your GitHub account
3. **Clone this repository**:
   - Click "Clone a repository from the Internet"
   - Enter the repository URL
   - Choose a local folder to save the project
   - Click "Clone"

#### Option 2: VS Code with GitHub Extension
1. **Install VS Code** from [code.visualstudio.com](https://code.visualstudio.com)
2. **Install the GitHub Extension**:
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "GitHub Pull Requests and Issues"
   - Install the extension
3. **Clone the repository**:
   - Press Ctrl+Shift+P
   - Type "Git: Clone"
   - Enter the repository URL
   - Choose a local folder

#### Option 3: GitHub.com (Web-based)
1. **Fork the repository**:
   - Go to the repository on GitHub.com
   - Click the "Fork" button in the top-right corner
   - This creates your own copy of the repository
2. **Edit files directly** in the GitHub web interface
3. **Create pull requests** to contribute changes back

### Running the Code

1. **Install Python 3** from [python.org](https://python.org) if not already installed
2. **Navigate to the project folder** (if using GitHub Desktop or VS Code)
3. **Run the Hello World Program**:
   ```bash
   python hello_world.py
   ```

   You should see the following output:
   ```
   Hello, World!
   ```

### Complete GitHub Workflow Tutorial

Follow these step-by-step instructions to contribute to the project:

#### Step 1: Clone the Repository

**Using GitHub Desktop:**
1. Open GitHub Desktop
2. Click "Clone a repository from the Internet"
3. Go to the "URL" tab
4. Paste the repository URL: `https://github.com/[username]/luit-sept-2025-silver-python`
5. Choose where to save it on your computer
6. Click "Clone"

**Using VS Code:**
1. Open VS Code
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
3. Type "Git: Clone" and select it
4. Paste the repository URL
5. Choose a folder to save it
6. Click "Select Repository Location"

**Using GitHub.com:**
1. Go to the repository on GitHub.com
2. Click the green "Code" button
3. Click "Open with GitHub Desktop" or "Open with Visual Studio Code"

#### Step 2: Create a New Branch

**Using GitHub Desktop:**
1. Click "Current branch" dropdown at the top
2. Click "New branch"
3. Name your branch (e.g., "my-feature" or "add-new-script")
4. Click "Create branch"

**Using VS Code:**
1. Click the branch name in the bottom-left corner
2. Click "Create new branch"
3. Type your branch name
4. Press Enter

**Using GitHub.com:**
1. Click the branch dropdown (usually says "main")
2. Type a new branch name
3. Click "Create branch: [name] from main"

#### Step 3: Make Your Changes

1. **Edit files** using your preferred method:
   - GitHub Desktop: Right-click files → "Open with external editor"
   - VS Code: Files open automatically
   - GitHub.com: Click the pencil icon to edit

2. **Add new files** if needed
3. **Test your changes** by running the Python scripts

#### Step 4: Commit Your Changes

**Using GitHub Desktop:**
1. You'll see your changes in the left panel
2. Check the boxes next to files you want to commit
3. Write a commit message (e.g., "Add new Python script for data processing")
4. Click "Commit to [branch-name]"

**Using VS Code:**
1. Go to the Source Control panel (Ctrl+Shift+G)
2. Click the "+" next to files you want to stage
3. Type a commit message in the text box
4. Press Ctrl+Enter to commit

**Using GitHub.com:**
1. Scroll to the bottom of the file you edited
2. Write a commit message
3. Click "Commit changes"

#### Step 5: Push Your Changes

**Using GitHub Desktop:**
1. Click "Push origin" button at the top
2. Your changes are now on GitHub

**Using VS Code:**
1. Click the "..." menu in Source Control
2. Select "Push"
3. Choose your branch if prompted

**Using GitHub.com:**
1. Changes are automatically saved when you commit
2. No additional push needed

#### Step 6: Create a Pull Request

1. **Go to the repository on GitHub.com**
2. **You'll see a yellow banner** saying "Compare & pull request"
3. **Click "Compare & pull request"**
4. **Fill out the form:**
   - Title: Brief description of your changes
   - Description: Explain what you changed and why
5. **Click "Create pull request"**

#### Step 7: Review and Merge

1. **Wait for review** from project maintainers
2. **Address any feedback** by making more commits
3. **Once approved**, the maintainer will merge your changes
4. **Your changes are now part of the main project!**

### Quick Reference Commands

- **Clone**: Get a copy of the repository
- **Branch**: Create a separate workspace for your changes
- **Commit**: Save your changes with a message
- **Push**: Upload your changes to GitHub
- **Pull Request**: Ask to merge your changes into the main project

## GitHub Actions Workflows

This repository includes automated workflows that run Python scripts with AWS integration. The workflows are designed with a **beta/prod split** strategy for safe deployment practices.

### Workflow Structure

#### 1. Pull Request Workflow (`.github/workflows/on_pull_request.yaml`)
- **Trigger**: Runs on every pull request
- **Purpose**: **Beta/Testing environment** - validates code changes before merging
- **AWS Integration**: Uses AWS credentials to run Python scripts against test resources
- **Permissions**: Limited scope for testing and validation

#### 2. Merge Workflow (`.github/workflows/on_merge.yaml`)
- **Trigger**: Runs when code is pushed to the `main` branch
- **Purpose**: **Production environment** - deploys validated code to production
- **AWS Integration**: Uses AWS credentials to run Python scripts against production resources
- **Permissions**: Full production access for deployment

### AWS Permissions & Security

Both workflows require the following GitHub Secrets to be configured in your repository settings:

- `AWS_ACCESS_KEY_ID`: AWS access key for authentication
- `AWS_SECRET_ACCESS_KEY`: AWS secret key for authentication  
- `AWS_REGION`: AWS region where resources are located

**Security Best Practices:**
- Use IAM roles with minimal required permissions
- Rotate access keys regularly
- Never commit AWS credentials to the repository
- Use different AWS accounts/regions for beta vs prod environments

### Workflow Features

- **Python 3.12**: Latest stable Python version
- **Dependency Management**: Automatically installs packages from `requirements.txt`
- **AWS CLI Integration**: Configured to work with AWS services
- **Ubuntu Runner**: Uses GitHub's latest Ubuntu environment

### Running Workflows

1. **For Testing**: Create a pull request to trigger the beta workflow
2. **For Production**: Merge to main branch to trigger the production workflow
3. **Manual Trigger**: Workflows can also be triggered manually from the Actions tab

## Python Scripts Overview

This repository contains a comprehensive collection of Python scripts designed to teach various programming concepts and AWS integration:

### Basic Python Concepts
- **`hello_world.py`** - Traditional "Hello, World!" introduction to Python
- **`defining_functions.py`** - Function definition, type hints, docstrings, and random number generation
- **`using_imports.py`** - Comprehensive examples of Python imports including:
  - Standard library modules (random, math, os, datetime, string, unicodedata, uuid)
  - Third-party libraries (matplotlib for data visualization)
  - Unicode and emoji handling

### AWS Integration Scripts
- **`helpers.py`** - Core AWS utility functions for EC2 and S3 operations
- **`creating_instances.py`** - EC2 instance creation with support for multiple AMI types (Ubuntu, Amazon Linux 2023, Amazon Linux 2)
- **`list_buckets.py`** - Simple S3 bucket listing
- **`list_buckets_lambda.py`** - AWS Lambda function for S3 bucket listing
- **`list_vpc_ids.py`** - VPC listing script (used in GitHub Actions workflows)
- **`listing_resources.py`** - Combined AWS resource listing (EC2 instances + S3 buckets)

### Development Tools
- **`prompts/`** - AI prompts for code documentation and PR review generation
- **`requirements.txt`** - Python dependencies (boto3 for AWS integration)

## Purpose

This repository serves as a comprehensive learning resource for Python programming with AWS integration. It progresses from basic Python concepts to advanced AWS operations, making it perfect for students learning Python for the first time while also introducing cloud computing concepts.
