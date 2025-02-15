import os
import httpx
from pathlib import Path
import json

AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")

class OpenAI:
    def __init__(self, token: str):
        self.token = token

    def _get_tools(self) -> dict[str, any]:
        tools_json_path = os.path.join(os.path.dirname(__file__), "tools.json")
        print(tools_json_path)
        with open(tools_json_path, "r") as file:
            return json.load(file)["tools"]

    def completion(self, user_input: str) -> dict[str, any]:
        response = httpx.post(
            "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [{"role": "user", "content": user_input}],
            },
        )
        return response

    def get_tool_to_use(self, user_input: str) -> dict[str, any]:
        response = httpx.post(
            "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [{"role": "user", "content": user_input}],
                "tools": self._get_tools()
            },
        )
        return response.json()
    
    def get_embeddings(self, user_input: str) -> dict[str, any]:
        response = httpx.post(
            "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [{"role": "user", "content": user_input}],
            },
        )
        return response



