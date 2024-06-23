import pytest
import unittest

from easyrag_tools.tools.hello_world_tool import HelloWorldTool


@pytest.fixture
def my_url() -> str:
    my_url = "https://www.bing.com"
    return my_url


@pytest.fixture
def my_tool_provider(my_url) -> HelloWorldTool:
    my_tool_provider = HelloWorldTool(my_url)
    return my_tool_provider


class TestTool:
    def test_hello_world_tool(self, my_tool_provider):
        result = my_tool_provider.greeting(query="Microsoft")
        assert result == "Hello Microsoft"


# Run the unit tests
if __name__ == "__main__":
    unittest.main()