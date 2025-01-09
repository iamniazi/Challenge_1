# Challenge 1: Python Testing with Playwright and Allure

## Prerequisites
Ensure the following dependencies are installed on your system:
- **Python 3.13.1**
- **Pip** (Python package manager)
- **Node.js**
- **Allure** (for generating test reports)

## Installation Instructions

1. **Install Python Dependencies:**
   ```bash
   pip install pytest pytest-playwright allure-pytest
   ```

2. **Install Playwright Browsers:**
   ```bash
   playwright install
   ```

## Running Tests

To execute the tests and generate Allure results:

1. **Run Tests:**
   ```bash
   pytest --alluredir=allure-results
   ```
   This will execute all tests in the project and save the results in the `allure-results` directory.

2. **Generate and Serve Allure Report:**
   ```bash
   allure serve allure-results
   ```
   This will generate the Allure report and open it in your default web browser.

## Notes
- Make sure the `allure-results` directory is accessible and contains valid test results before generating the report.
- For additional configurations or advanced options, refer to the official documentation for [Pytest](https://docs.pytest.org/) and [Allure](https://docs.qameta.io/allure/).
