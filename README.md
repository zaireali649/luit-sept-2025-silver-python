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

1. **Clone the Repository**  
   Open your terminal and run:
   ```bash
   git clone <your-repo-url>
   cd luit-sept-2025-silver-python
   ```

2. **Run the Hello World Program**  
   Make sure you have Python 3 installed. Then run:
   ```bash
   python hello_world.py
   ```

   You should see the following output:
   ```
   Hello, World!
   ```

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
