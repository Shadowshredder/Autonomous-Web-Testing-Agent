import json
import os

from browser.playwright_runner import execute_test_plan


test_plans = [

    {
        "test_name": "Successful SauceDemo Login Test",

        "steps": [

            {
                "action": "navigate",
                "url": "https://www.saucedemo.com"
            },

            {
                "action": "type",
                "selector": "#user-name",
                "text": "standard_user"
            },

            {
                "action": "type",
                "selector": "#password",
                "text": "secret_sauce"
            },

            {
                "action": "click_text",
                "text": "Login"
            },

            {
                "action": "verify_text",
                "expected": "Products"
            }
        ]
    },

    {
        "test_name": "Intentional Failure Test",

        "steps": [

            {
                "action": "navigate",
                "url": "https://example.com"
            },

            {
                "action": "verify_text",
                "expected": "This Text Does Not Exist"
            }
        ]
    },

    {
        "test_name": "Test After Failure",

        "steps": [

            {
                "action": "navigate",
                "url": "https://example.com"
            },

            {
                "action": "verify_title",
                "expected": "Example Domain"
            }
        ]
    }
]


def main():

    print("\n🤖 FAILURE RECOVERY TEST")
    print("=" * 50)

    all_test_results = []

    for number, test_plan in enumerate(
        test_plans,
        start=1
    ):

        print("\n" + "=" * 50)

        print(
            f"🚀 RUNNING TEST {number}: "
            f"{test_plan['test_name']}"
        )

        print("=" * 50)

        try:

            results = execute_test_plan(
                test_plan
            )

            passed = sum(
                1
                for result in results
                if result.get("status") == "PASS"
            )

            failed = sum(
                1
                for result in results
                if result.get("status") == "FAIL"
            )

            status = (
                "PASS"
                if failed == 0
                else "FAIL"
            )

            test_summary = {
                "test_number": number,
                "test_name": test_plan["test_name"],
                "status": status,
                "passed_steps": passed,
                "failed_steps": failed
            }

            all_test_results.append({
                "test_plan": test_plan,
                "results": results,
                "summary": test_summary
            })

            print("\n📊 TEST SUMMARY")
            print(f"Status: {status}")
            print(f"Passed steps: {passed}")
            print(f"Failed steps: {failed}")

        except Exception as e:

            print(
                f"\n⚠️ Test {number} crashed: {e}"
            )

            all_test_results.append({

                "test_plan": test_plan,

                "results": [],

                "summary": {
                    "test_number": number,
                    "test_name": test_plan["test_name"],
                    "status": "FAIL",
                    "passed_steps": 0,
                    "failed_steps": 1
                },

                "error": str(e)
            })

            print(
                "➡️ Continuing to the next test..."
            )

    # ---------------------------------
    # OVERALL SUMMARY
    # ---------------------------------

    total_tests = len(
        all_test_results
    )

    passed_tests = sum(
        1
        for test in all_test_results
        if test["summary"]["status"] == "PASS"
    )

    failed_tests = (
        total_tests - passed_tests
    )

    overall_status = (
        "PASS"
        if failed_tests == 0
        else "FAIL"
    )

    final_report = {

        "agent": "Autonomous Web Testing Agent",

        "total_tests": total_tests,

        "passed_tests": passed_tests,

        "failed_tests": failed_tests,

        "overall_status": overall_status,

        "tests": all_test_results
    }

    # ---------------------------------
    # SAVE REPORT
    # ---------------------------------

    os.makedirs(
        "reports",
        exist_ok=True
    )

    report_path = (
        "reports/failure_recovery_report.json"
    )

    with open(
        report_path,
        "w"
    ) as file:

        json.dump(
            final_report,
            file,
            indent=4
        )

    # ---------------------------------
    # FINAL RESULT
    # ---------------------------------

    print("\n" + "=" * 50)

    print("🏁 FAILURE RECOVERY TEST COMPLETED")

    print("=" * 50)

    print(
        f"Total tests: {total_tests}"
    )

    print(
        f"Passed tests: {passed_tests}"
    )

    print(
        f"Failed tests: {failed_tests}"
    )

    print(
        f"Overall status: {overall_status}"
    )

    print(
        f"\n📄 Report saved: {report_path}"
    )


if __name__ == "__main__":
    main()