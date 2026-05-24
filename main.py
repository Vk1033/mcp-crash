import asyncio

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain.agents import create_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatNVIDIA(model="mistralai/mistral-nemotron")

stdio_server_params = StdioServerParameters(
    command="uv",
    args=["run", "servers/math_server.py"],
)


async def main():
    print("Hello from mcp-crash!")


if __name__ == "__main__":
    asyncio.run(main())
