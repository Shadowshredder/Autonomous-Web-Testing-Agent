# Autonomous Web Testing Agent

An AI-powered web testing agent that converts natural-language testing requirements into structured test plans and executes them automatically using Playwright.

The agent uses Google Gemini to generate test plans, handles failed actions with automatic retries, captures failure screenshots, and analyzes failures to provide possible recovery suggestions.

## Overview

Traditional test automation requires testers to manually write test scripts and define test steps. This project explores a more AI-driven approach where a user can provide a testing requirement in natural language.

The system then:

1. Converts the requirement into a structured test plan using Gemini.
2. Executes the generated steps using Playwright.
3. Retries failed actions automatically.
4. Captures a screenshot if an action continues to fail.
5. Uses Gemini to analyze the failure.
6. Generates a JSON report containing the test results.

## Features

* Converts natural-language testing requirements into structured test plans.
* Executes browser tests using Playwright and Chromium.
* Supports common browser actions such as navigation, clicking, typing, form submission, and verification.
* Automatically retries failed actions.
* Captures screenshots for failed test steps.
* Uses Gemini AI to analyze failures and suggest possible recovery actions.
* Generates JSON test reports.
* Supports single and multiple test execution.
* Includes MCP tools that expose the testing capabilities of the project.
* Uses environment variables to securely manage API keys.

## Architecture

```text
Natural Language Requirement
            |
            v
     Gemini AI Planner
            |
            v
   Structured Test Plan
            |
            v
   Playwright Test Runner
            |
            v
      Browser Actions
            |
      ----------------
      |              |
     PASS           FAIL
      |              |
      v              v
    Report      Retry Action
                     |
              ----------------
              |              |
           Success       Final Failure
                              |
                              v
                     Failure Screenshot
                              |
                              v
                     Gemini Failure Analysis
                              |
                              v
                         JSON Report
```

## Tech Stack

* Python
* Google Gemini API
* Google GenAI SDK
* Playwright
* Chromium
* Model Context Protocol (MCP)
* python-dotenv
* JSON
* Git and GitHub

## Project Structure

```text
ai-autonomous-web-testing-agent/
|
|-- agent/
|   |-- planner.py
|
|-- browser/
|   |-- playwright_runner.py
|
|-- reports/
|   |-- test_report.json
|   |-- failure_recovery_report.json
|
|-- screenshots/
|   |-- test_failure.png
|
|-- .gitignore
|-- main.py
|-- local_test.py
|-- mcp_server.py
|-- requirements.txt
|-- README.md
```

> Note: The `.env` file is intentionally not included in the repository because it contains the Gemini API key.

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd ai-autonomous-web-testing-agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Chromium

```bash
playwright install chromium
```

### 5. Configure the Gemini API

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Do not upload or commit the `.env` file to GitHub.

## Running the Agent

Start the application:

```bash
python main.py
```

You can choose between:

```text
1. Single test
2. Multiple tests
```

Enter a testing requirement in natural language, and the agent will generate and execute the corresponding test plan.

## Example

Example requirement:

```text
Open https://www.saucedemo.com, log in using username
standard_user and password secret_sauce, and verify that
the Products page is displayed.
```

The AI generates a structured plan similar to:

```text
1. Navigate to the website
2. Enter the username
3. Enter the password
4. Click the Login button
5. Verify that the Products page is displayed
```

The Playwright runner then executes these steps automatically.

## Example Successful Test

```text
Navigating to: https://www.saucedemo.com
Navigate action passed

Typing 'standard_user' into: #user-name
Type action passed

Typing 'secret_sauce' into: #password
Type action passed

Clicking selector: #login-button
Click action passed

Checking visible text...
Expected: Products
Text verification passed

Status: PASS
Passed steps: 5
Failed steps: 0
```

## Failure Handling

When a browser action fails, the agent automatically retries the action.

```text
Action Failed
     |
     v
Retry Attempt 1
     |
     v
Retry Attempt 2
     |
     v
Retry Attempt 3
     |
     v
Failure Screenshot
     |
     v
Gemini Failure Analysis
     |
     v
Recovery Suggestion
```

Example failure analysis:

```text
Action failed after 3 attempts

Screenshot saved: screenshots/test_failure.png

Failure Reason:
The expected text is not present on the page.

Suggested Action:
Update the assertion to match the actual page content.
```

## Test Reports

Test results are saved as JSON files in the `reports/` directory.

Example:

```json
{
    "agent": "Autonomous Web Testing Agent",
    "total_tests": 1,
    "passed_tests": 1,
    "failed_tests": 0,
    "overall_status": "PASS"
}
```

The project also includes a separate failure recovery report generated by `local_test.py`.

## MCP Integration

The project includes an MCP server that exposes testing-related tools.

### get_testing_capabilities

Returns the browser testing actions supported by the agent.

### create_test_requirement_template

Creates a structured testing requirement using a website and task description.

Supported actions include:

* `navigate`
* `click`
* `click_text`
* `type`
* `submit`
* `verify_title`
* `verify_url`
* `verify_text`
* `screenshot`

## What This Project Demonstrates

This project demonstrates practical experience with:

* Python development
* Generative AI
* LLM-based task planning
* AI agents
* Browser automation
* Playwright
* Test automation
* Retry and failure handling
* AI-assisted failure analysis
* Model Context Protocol (MCP)
* API integration
* JSON reporting

## Future Improvements

Possible future enhancements include:

* Automatic selector recovery
* Self-healing test steps
* Support for additional browser actions
* Parallel test execution
* Test history and analytics
* CI/CD integration
* Firefox and WebKit support
* Persistent test memory
* Advanced MCP integrations

## Author

**Gayathri U**

B.Tech Information Technology

GitHub: [Shadowshredder](https://github.com/Shadowshredder)
