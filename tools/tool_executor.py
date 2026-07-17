# Import required libraries
from langchain_core.tools import BaseTool

class ToolExecutor:
    """Execute LangChain tools by name.

    The ToolExecutor acts as a simple dispatcher between the LLM
    and the available tools. Given a tool name and input arguments,
    it finds the matching tool, executes it, and returns the result.

    This class does not contain any reasoning logic. Its sole
    responsibility is executing tools.
    """

    def __init__(self, tools: list[BaseTool]):
        """
        Initialize the executor with available tools.

        Args:
            tools:
                List of LangChain tools that the executor can run.
        """
         
        self.tools = {
             tool.name:tool
             for tool in tools
        }
    
    def execute(
        self,
        tool_name: str,
        tool_args: dict
    ):
        """Execute a tool by name.

        Args:
            tool_name (str): Name of the tool requested by the LLM.
            tool_args (dict): Dictionary containing the tool arguments.

        Returns:
            Result returned by the tool

        Raises:
            ValueError:
                If the requested tool does not exist.
        """

        tool = self.tools.get(tool_name)

        if tool is None:
            raise ValueError(
                f"Unknown tool: {tool_name}"
            )
        
        return tool.invoke(tool_args)