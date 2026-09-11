
from playwright.sync_api import sync_playwright


def execute_test_plan(test_plan, max_retries=2):

    results = []

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:

            for step in test_plan["steps"]:

                action = step["action"]

                success = False
                last_error = None

                for attempt in range(max_retries + 1):

                    try:

                        if attempt > 0:
                            print(
                                f"\n🔄 Retry attempt {attempt} "
                                f"for action: {action}"
                            )

                        # --------------------------------
                        # NAVIGATE
                        # --------------------------------

                        if action == "navigate":

                            url = step["url"]

                            print(
                                f"\n🌐 Navigating to: {url}"
                            )

                            page.goto(
                                url,
                                wait_until="domcontentloaded"
                            )

                            page.wait_for_load_state(
                                "networkidle"
                            )

                            results.append({
                                "action": action,
                                "status": "PASS"
                            })

                            print(
                                "✅ Navigate action passed"
                            )

                        # --------------------------------
                        # CLICK
                        # --------------------------------

                        elif action == "click":

                            selector = step["selector"]

                            print(
                                f"\n🖱️ Clicking selector: {selector}"
                            )

                            locator = page.locator(selector)

                            locator.wait_for(
                                state="visible",
                                timeout=10000
                            )

                            locator.click()

                            results.append({
                                "action": action,
                                "status": "PASS"
                            })

                            print(
                                "✅ Click action passed"
                            )

                        # --------------------------------
                        # CLICK TEXT
                        # --------------------------------

                        elif action == "click_text":

                            text = step["text"]

                            print(
                                f"\n🖱️ Clicking text: {text}"
                            )

                            locator = page.get_by_text(
                                text.replace("...", "").strip(),
                                exact=True
                            )

                            locator.wait_for(
                                state="visible",
                                timeout=10000
                            )

                            locator.click(
                                no_wait_after=True
                            )

                            page.wait_for_load_state(
                                "domcontentloaded"
                            )

                            results.append({
                                "action": action,
                                "status": "PASS"
                            })

                            print(
                                "✅ Text click action passed"
                            )

                        # --------------------------------
                        # TYPE
                        # --------------------------------

                        elif action == "type":

                            selector = step["selector"]
                            text = step["text"]

                            print(
                                f"\n⌨️ Typing '{text}' "
                                f"into: {selector}"
                            )

                            locator = page.locator(
                                selector
                            )

                            locator.wait_for(
                                state="visible",
                                timeout=10000
                            )

                            locator.fill(text)

                            results.append({
                                "action": action,
                                "status": "PASS"
                            })

                            print(
                                "✅ Type action passed"
                            )

                        # --------------------------------
                        # SUBMIT
                        # --------------------------------

                        elif action == "submit":

                            selector = step["selector"]

                            print(
                                f"\n📨 Submitting form: {selector}"
                            )

                            locator = page.locator(
                                selector
                            )

                            locator.wait_for(
                                state="visible",
                                timeout=10000
                            )

                            locator.evaluate(
                                "(form) => form.submit()"
                            )

                            page.wait_for_load_state(
                                "domcontentloaded"
                            )

                            results.append({
                                "action": action,
                                "status": "PASS"
                            })

                            print(
                                "✅ Form submission passed"
                            )

                        # --------------------------------
                        # VERIFY TITLE
                        # --------------------------------

                        elif action == "verify_title":

                            expected_title = step["expected"]
                            actual_title = page.title()

                            print(
                                "\n🔍 Checking page title..."
                            )

                            print(
                                f"Expected: {expected_title}"
                            )

                            print(
                                f"Actual: {actual_title}"
                            )

                            if expected_title == actual_title:

                                results.append({
                                    "action": action,
                                    "status": "PASS"
                                })

                                print(
                                    "✅ Title verification passed"
                                )

                            else:

                                raise AssertionError(
                                    f"Expected title "
                                    f"'{expected_title}' "
                                    f"but got "
                                    f"'{actual_title}'"
                                )

                        # --------------------------------
                        # VERIFY URL
                        # --------------------------------

                        elif action == "verify_url":

                            expected_url = (
                                step["expected"].rstrip("/")
                            )

                            actual_url = (
                                page.url.rstrip("/")
                            )

                            print(
                                "\n🔍 Checking page URL..."
                            )

                            print(
                                f"Expected: {expected_url}"
                            )

                            print(
                                f"Actual: {actual_url}"
                            )

                            if expected_url == actual_url:

                                results.append({
                                    "action": action,
                                    "status": "PASS"
                                })

                                print(
                                    "✅ URL verification passed"
                                )

                            else:

                                raise AssertionError(
                                    f"Expected URL "
                                    f"'{expected_url}' "
                                    f"but got "
                                    f"'{actual_url}'"
                                )

                        # --------------------------------
                        # VERIFY TEXT
                        # --------------------------------

                        elif action == "verify_text":

                            expected_text = step["expected"]

                            print(
                                "\n🔍 Checking visible text..."
                            )

                            print(
                                f"Expected: {expected_text}"
                            )

                            locator = page.get_by_text(
                                expected_text,
                                exact=True
                            )

                            locator.wait_for(
                                state="visible",
                                timeout=10000
                            )

                            results.append({
                                "action": action,
                                "status": "PASS"
                            })

                            print(
                                "✅ Text verification passed"
                            )

                        # --------------------------------
                        # SCREENSHOT
                        # --------------------------------

                        elif action == "screenshot":

                            screenshot_path = step["path"]

                            print(
                                f"\n📸 Taking screenshot: "
                                f"{screenshot_path}"
                            )

                            page.screenshot(
                                path=screenshot_path,
                                full_page=True
                            )

                            results.append({
                                "action": action,
                                "status": "PASS",
                                "screenshot": screenshot_path
                            })

                            print(
                                "✅ Screenshot saved"
                            )

                        # --------------------------------
                        # UNKNOWN ACTION
                        # --------------------------------

                        else:

                            raise ValueError(
                                f"Unknown action: {action}"
                            )

                        success = True
                        break

                    except Exception as e:

                        last_error = str(e)

                        print(
                            f"\n⚠️ Action failed: {last_error}"
                        )

                        if attempt < max_retries:

                            print(
                                "⏳ Waiting before retry..."
                            )

                            page.wait_for_timeout(1000)

                # --------------------------------
                # FINAL FAILURE
                # --------------------------------

                if not success:

                    screenshot_path = (
                        "screenshots/test_failure.png"
                    )

                    page.screenshot(
                        path=screenshot_path,
                        full_page=True
                    )

                    results.append({
                        "action": action,
                        "status": "FAIL",
                        "error": last_error,
                        "screenshot": screenshot_path
                    })

                    print(
                        f"\n❌ Action failed after "
                        f"{max_retries + 1} attempts"
                    )

                    print(
                        f"📸 Screenshot saved: "
                        f"{screenshot_path}"
                    )

        except Exception as e:

            screenshot_path = (
                "screenshots/test_failure.png"
            )

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            print(
                f"\n❌ Test execution error: {e}"
            )

            print(
                f"📸 Screenshot saved: "
                f"{screenshot_path}"
            )

            results.append({
                "status": "FAIL",
                "error": str(e),
                "screenshot": screenshot_path
            })

        finally:

            browser.close()

    return results

