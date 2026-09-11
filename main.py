import json
import os

from agent.planner import (
    create_test_plan,
    analyze_failure
)

from browser.playwright_runner import (
    execute_test_plan
)


def run_single_test(requirement, test_number):

    print("\n" + "=" * 60)
    print(f"🤖 AUTONOMOUS TEST CASE {test_number}")
    print("=" * 60)

    print(f"\nRequirement:")
    print(requirement)

    # --------------------------------
    # AI PLANNING
    # --------------------------------

    print("\n🧠 AI PLANNING TEST...")

    test_plan = create_test_plan(
        requirement
    )

    print("\n🤖 GENERATED TEST PLAN")

    print(
        "Test Name:",
        test_plan["test_name"]
    )

    for number, step in enumerate(
        test_plan["steps"],
        start=1
    ):
        print(
            f"{number}. {step}"
        )

    # --------------------------------
    # EXECUTION
    # --------------------------------

    print("\n🚀 EXECUTING TEST...")

    results = execute_test_plan(
        test_plan
    )

    # --------------------------------
    # RESULT ANALYSIS
    # --------------------------------

    failed = any(
        result.get("status") == "FAIL"
        for result in results
    )

    ai_analysis = None

    if failed:

        print(
            "\n🤖 TEST FAILED — ANALYZING..."
        )

        errors = [
            result.get(
                "error",
                "Unknown error"
            )
            for result in results
            if result.get("status") == "FAIL"
        ]

        try:

            ai_analysis = analyze_failure(
                requirement,
                test_plan,
                "\n".join(errors)
            )

            print(
                "\n🧠 AI FAILURE ANALYSIS"
            )

            print(
                "Reason:",
                ai_analysis.get(
                    "failure_reason"
                )
            )

            print(
                "Suggested action:",
                ai_analysis.get(
                    "suggested_action"
                )
            )

        except Exception as e:

            print(
                f"⚠️ AI analysis error: {e}"
            )

    # --------------------------------
    # SUMMARY
    # --------------------------------

    passed = sum(
        1
        for result in results
        if result.get("status") == "PASS"
    )

    failed_count = sum(
        1
        for result in results
        if result.get("status") == "FAIL"
    )

    if failed_count == 0:

        status = "PASS"

    else:

        status = "FAIL"

    summary = {
        "test_number": test_number,
        "test_name": test_plan["test_name"],
        "status": status,
        "passed_steps": passed,
        "failed_steps": failed_count
    }

    print("\n📊 TEST SUMMARY")
    print("-" * 40)

    print(
        f"Status: {status}"
    )

    print(
        f"Passed steps: {passed}"
    )

    print(
        f"Failed steps: {failed_count}"
    )

    return {
        "requirement": requirement,
        "test_plan": test_plan,
        "results": results,
        "summary": summary,
        "ai_failure_analysis": ai_analysis
    }


def main():

    print("\n" + "=" * 60)
    print("🤖 AUTONOMOUS WEB TESTING AGENT")
    print("=" * 60)

    print(
        "\nChoose testing mode:"
    )

    print(
        "1. Single test"
    )

    print(
        "2. Multiple tests"
    )

    choice = input(
        "\nEnter choice (1 or 2): "
    )

    test_requirements = []

    # --------------------------------
    # SINGLE TEST
    # --------------------------------

    if choice == "1":

        requirement = input(
            "\nEnter your testing requirement: "
        )

        test_requirements.append(
            requirement
        )

    # --------------------------------
    # MULTIPLE TESTS
    # --------------------------------

    elif choice == "2":

        count = int(
            input(
                "\nHow many test cases? "
            )
        )

        for number in range(1, count + 1):

            requirement = input(
                f"\nEnter requirement "
                f"for test {number}: "
            )

            test_requirements.append(
                requirement
            )

    else:

        print(
            "\n❌ Invalid choice."
        )

        return

    # --------------------------------
    # AUTONOMOUS TEST LOOP
    # --------------------------------

    all_results = []

    for number, requirement in enumerate(
        test_requirements,
        start=1
    ):

        result = run_single_test(
            requirement,
            number
        )

        all_results.append(
            result
        )

    # --------------------------------
    # OVERALL REPORT
    # --------------------------------

    total_tests = len(
        all_results
    )

    passed_tests = sum(
        1
        for result in all_results
        if result["summary"]["status"] == "PASS"
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

        "tests": all_results
    }

    os.makedirs(
        "reports",
        exist_ok=True
    )

    with open(
        "reports/test_report.json",
        "w"
    ) as file:

        json.dump(
            final_report,
            file,
            indent=4
        )

    print(
        "\n" + "=" * 60
    )

    print(
        "🏁 AUTONOMOUS TESTING COMPLETE"
    )

    print(
        "=" * 60
    )

    print(
        f"Total tests: {total_tests}"
    )

    print(
        f"Passed: {passed_tests}"
    )

    print(
        f"Failed: {failed_tests}"
    )

    print(
        f"Overall status: {overall_status}"
    )

    print(
        "\n📄 Final report:"
    )

    print(
        "reports/test_report.json"
    )


if __name__ == "__main__":
    main()