from promptflow.core import ToolProvider, tool
import urllib.request


class HelloWorldTool(ToolProvider):

    def __init__(self, url: str):
        super().__init__()
        # Load content from url might be slow, so we do it in __init__ method to make sure it is loaded only once.
        self.content = urllib.request.urlopen(url).read()

    @tool
    def greeting(self, query: str) -> str:
        # Replace with your tool code.
        return "Hello " + query