from mcp.server import MCPServer


mcp = MCPServer("Autonomous Web Testing Agent")


@mcp.tool()
def get_testing_capabilities() -> str:
    """
    Returns the actions supported by the autonomous testing agent.
    """

    return """
Supported browser testing actions:

- navigate
- click
- click_text
- type
- submit
- verify_title
- verify_url
- verify_text
- screenshot

The agent can also retry failed actions,
capture failure screenshots,
and generate test reports.
"""


@mcp.tool()
def create_test_requirement_template(
    website: str,
    task: str
) -> str:
    """
    Creates a structured testing requirement.
    """

    return (
        f"Open {website}. "
        f"Perform the following task: {task}. "
        f"Verify that the expected result is achieved."
    )


@mcp.resource("testing://capabilities")
def testing_capabilities() -> str:
    """
    Provides testing capabilities as an MCP resource.
    """

    return get_testing_capabilities()


if __name__ == "__main__":
    mcp.run()