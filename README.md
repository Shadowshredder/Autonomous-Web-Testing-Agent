# Autonomous-Web-Testing-Agent
AI-powered autonomous web testing agent that converts natural language requirements into Playwright test plans using Gemini AI, with retries, failure analysis, screenshots, JSON reporting, and MCP integration.
\# 🤖 Autonomous Web Testing Agent



An AI-powered autonomous web testing agent that converts natural-language testing requirements into executable browser test plans, runs them using Playwright, automatically retries failed actions, captures failure screenshots, and uses Gemini AI to analyze test failures.



\## 🚀 Features



\* 🧠 \*\*AI Test Planning\*\* — Converts natural-language requirements into structured test plans using Google Gemini.

\* 🌐 \*\*Browser Automation\*\* — Executes generated test steps using Playwright and Chromium.

\* 🔄 \*\*Automatic Retries\*\* — Retries failed browser actions up to three attempts.

\* 📸 \*\*Failure Screenshots\*\* — Captures screenshots when a test action fails.

\* 🤖 \*\*AI Failure Analysis\*\* — Uses Gemini to identify failure causes and suggest recovery actions.

\* 📊 \*\*JSON Test Reports\*\* — Generates detailed execution reports.

\* 🔌 \*\*MCP Integration\*\* — Provides testing capabilities through Model Context Protocol tools.

\* 🧪 \*\*Multiple Testing Modes\*\* — Supports single and multiple test execution.

\* 🛡️ \*\*Environment Configuration\*\* — API credentials are loaded securely through environment variables.



\## 🏗️ Architecture



```text

&#x20;                   Natural Language Requirement

&#x20;                              │

&#x20;                              ▼

&#x20;                    ┌──────────────────┐

&#x20;                    │   Gemini AI      │

&#x20;                    │   Test Planner   │

&#x20;                    └────────┬─────────┘

&#x20;                             │

&#x20;                             ▼

&#x20;                    Structured Test Plan

&#x20;                             │

&#x20;                             ▼

&#x20;                    ┌──────────────────┐

&#x20;                    │    Playwright   │

&#x20;                    │ Browser Runner   │

&#x20;                    └────────┬─────────┘

&#x20;                             │

&#x20;                             ▼

&#x20;                      Browser Actions

&#x20;                             │

&#x20;                   ┌─────────┴─────────┐

&#x20;                   │                   │

&#x20;                 PASS                FAIL

&#x20;                   │                   │

&#x20;                   ▼                   ▼

&#x20;                Report            Retry Action

&#x20;                                       │

&#x20;                                 ┌─────┴─────┐

&#x20;                                 │           │

&#x20;                              Success     Final Failure

&#x20;                                             │

&#x20;                                             ▼

&#x20;                                     Failure Screenshot

&#x20;                                             │

&#x20;                                             ▼

&#x20;                                       Gemini AI

&#x20;                                    Failure Analysis

&#x20;                                             │

&#x20;                                             ▼

&#x20;                                      JSON Report

```



\## 🛠️ Tech Stack



\* \*\*Python\*\*

\* \*\*Google Gemini API\*\*

\* \*\*Google GenAI SDK\*\*

\* \*\*Playwright\*\*

\* \*\*Chromium\*\*

\* \*\*Model Context Protocol (MCP)\*\*

\* \*\*python-dotenv\*\*

\* \*\*JSON\*\*

\* \*\*Git/GitHub\*\*



\## 📁 Project Structure



```text

ai-autonomous-web-testing-agent/

│

├── agent/

│   └── planner.py

│

├── browser/

│   └── playwright\_runner.py

│

├── reports/

│   ├── test\_report.json

│   └── failure\_recovery\_report.json

│

├── screenshots/

│   └── test\_failure.png

│

├── .env

├── .gitignore

├── main.py

├── local\_test.py

├── mcp\_server.py

├── requirements.txt

└── README.md

```



\## ⚙️ Installation



\### 1. Clone the repository



```bash

git clone <your-github-repository-url>

cd ai-autonomous-web-testing-agent

```



\### 2. Create a virtual environment



```bash

python -m venv venv

```



Activate it on Windows:



```bash

venv\\Scripts\\activate

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\### 4. Install Playwright Chromium



```bash

playwright install chromium

```



\### 5. Configure the Gemini API



Create a `.env` file in the project root:



```env

GEMINI\_API\_KEY=your\_api\_key\_here

```



Do not commit the `.env` file to GitHub.



\## ▶️ Running the Agent



Start the autonomous testing agent:



```bash

python main.py

```



Choose:



```text

1\. Single test

2\. Multiple tests

```



\### Example



Testing requirement:



```text

Open https://www.saucedemo.com, log in using username

standard\_user and password secret\_sauce, and verify that

the Products page is displayed.

```



Gemini generates a plan similar to:



```text

1\. navigate

2\. type username

3\. type password

4\. click Login

5\. verify Products

```



Playwright then executes the generated steps automatically.



\## 🧪 Example Successful Test



```text

🌐 Navigating to: https://www.saucedemo.com

✅ Navigate action passed



⌨️ Typing 'standard\_user' into: #user-name

✅ Type action passed



⌨️ Typing 'secret\_sauce' into: #password

✅ Type action passed



🖱️ Clicking selector: #login-button

✅ Click action passed



🔍 Checking visible text...

Expected: Products

✅ Text verification passed



Status: PASS

Passed steps: 5

Failed steps: 0

```



\## 🔄 Failure Handling



When an action fails, the agent automatically retries it.



```text

Action failed

&#x20;    ↓

Retry attempt 1

&#x20;    ↓

Retry attempt 2

&#x20;    ↓

Retry attempt 3

&#x20;    ↓

Failure screenshot

&#x20;    ↓

Gemini failure analysis

&#x20;    ↓

Recovery suggestion

```



Example:



```text

❌ Action failed after 3 attempts

📸 Screenshot saved: screenshots/test\_failure.png



🧠 AI FAILURE ANALYSIS



Reason:

The expected text is not present on the page.



Suggested action:

Update the assertion to match the actual page content.

```



\## 📊 Test Reports



The agent generates JSON reports inside the `reports/` directory.



Example:



```json

{

&#x20;   "agent": "Autonomous Web Testing Agent",

&#x20;   "total\_tests": 1,

&#x20;   "passed\_tests": 0,

&#x20;   "failed\_tests": 1,

&#x20;   "overall\_status": "FAIL"

}

```



\## 🔌 MCP Tools



The project includes an MCP server exposing testing-related tools.



\### `get\_testing\_capabilities`



Returns the browser testing actions supported by the agent.



\### `create\_test\_requirement\_template`



Creates a structured testing requirement from a website and task description.



Supported browser actions include:



\* `navigate`

\* `click`

\* `click\_text`

\* `type`

\* `submit`

\* `verify\_title`

\* `verify\_url`

\* `verify\_text`

\* `screenshot`



\## 🎯 Project Highlights



This project demonstrates practical experience with:



\* Generative AI

\* LLM-based task planning

\* AI agents

\* Browser automation

\* Playwright

\* Test automation

\* Failure detection

\* Retry mechanisms

\* AI-powered failure analysis

\* MCP

\* API integration

\* JSON-based reporting

\* Python development



\## 🔮 Future Improvements



\* Automatic selector recovery

\* Self-healing test steps

\* More browser actions

\* Parallel test execution

\* Test history and analytics

\* CI/CD integration

\* Browser support for Firefox and WebKit

\* Persistent test memory

\* Advanced MCP integrations



\## 👩‍💻 Author



\*\*Gayathri U\*\*



B.Tech Information Technology



GitHub: \[Shadowshredder](https://github.com/Shadowshredder)



