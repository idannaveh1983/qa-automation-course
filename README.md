Playwright & Pytest Test Automation Framework 🚀

This repository contains a modular, scalable Test Automation Framework built with Python, Playwright, and Pytest. It is designed using industry best practices, including the Page Object Model (POM) pattern and reusable Pytest Fixtures.

🛠️ Tech Stack & Prerequisites

Language: Python 3.12+

Test Runner: Pytest

Automation Library: Playwright (Sync API)

Design Pattern: Page Object Model (POM) & Fixtures Architecture

🏗️ Project Architecture

qa-automation-course/
│
├── pages/                  # Page Object Model layer
│   ├── base_page.py        # Generic actions & base methods for all pages
│   └── login_page.py       # Page elements and user actions for Login
│
├── test_login_pom.py       # E2E & Functional Login test cases
├── conftest.py             # Global Pytest fixtures & setup/teardown
└── README.md               # Project documentation


🚀 Getting Started

1. Clone the Repository

git clone https://github.com/<YOUR-USERNAME>/qa-automation-course.git
cd qa-automation-course


2. Set Up Virtual Environment & Install Dependencies

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS / Linux:
source venv/bin/activate
# On Windows:
# .\venv\Scripts\activate

# Install dependencies & Playwright browsers
pip install pytest playwright pytest-playwright
playwright install


🧪 Running Tests

Run all tests in headed mode:

pytest --headed


Run a specific test file:

pytest test_login_pom.py --headed


Run tests in headless mode (default for CI/CD):

pytest


🎯 Key Features Included

BasePage Abstraction: Centralized navigation, waiting mechanisms, and generic web actions.

Page Object Model (POM): Complete separation between page elements and test assertions for high maintainability.

Fixture Injection: Clean setup & teardown lifecycle management using conftest.py.

Cross-Platform Compatibility: Configured and tested on both macOS and Windows 11 environments.