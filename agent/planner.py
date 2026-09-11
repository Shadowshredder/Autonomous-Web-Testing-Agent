import os
import json

from dotenv import load_dotenv
from google import genai


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def create_test_plan(requirement):
    """
    Uses Gemini to convert a natural language
    testing requirement into a structured test plan.
    """

    prompt = f"""
You are an expert software testing planner.

Convert the following testing requirement into a structured JSON test plan.

Testing requirement:
{requirement}

Available actions:

1. navigate
   - Opens a website.
   - Required field: "url"

2. click
   - Clicks an element using a CSS selector.
   - Required field: "selector"

3. click_text
   - Clicks an element using its visible text.
   - Required field: "text"

4. verify_title
   - Verifies the current page title.
   - Required field: "expected"

5. type
   - Enters text into an input field.
   - Required fields: "selector" and "text"

6. verify_url
   - Verifies the current page URL.
   - Required field: "expected"

7. verify_text
   - Verifies that specific visible text exists on the current page.
   - Required field: "expected"

8. screenshot
   - Takes a screenshot of the current page.
   - Required field: "path"

9. submit
   - Submits a form.
   - Required field: "selector"

Rules:
- Use "click_text" when the requirement refers to a button or link by visible text.
- Use "click" when a CSS selector is appropriate.
- Use "type" for input fields.
- Use "submit" when the requirement explicitly asks to submit a form.
- Use "verify_text" when checking visible text.
- Use "verify_title" when checking the page title.
- Use "verify_url" when checking the current URL.
- Use "screenshot" when a screenshot is requested.
- Only include actions that are actually needed.
- Keep the steps in the correct execution order.
- Return ONLY valid JSON.
- Do not add explanations.
- Do not use markdown.

Return the result in this format:

{{
    "test_name": "short descriptive test name",
    "steps": [
        {{
            "action": "navigate",
            "url": "website URL"
        }},
        {{
            "action": "submit",
            "selector": "form selector"
        }}
    ]
}}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return json.loads(response.text)


def analyze_failure(requirement, test_plan, error):
    """
    Uses Gemini to analyze a failed test execution
    and suggest a possible recovery.
    """

    prompt = f"""
You are an expert software testing failure analyst.

A test failed during execution.

Testing requirement:
{requirement}

Test plan:
{json.dumps(test_plan, indent=2)}

Error:
{error}

Analyze the failure and return ONLY valid JSON.

Return:

{{
    "failure_reason": "short explanation",
    "suggested_action": "short recovery suggestion"
}}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return json.loads(response.text)