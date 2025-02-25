"""
本代码用于展示如何自定义一个模型，本模型基于UniAPI，
但是任何支持HTTPS调用的大模型都可以套用以下代码
"""
from types import SimpleNamespace
import requests

class QwenApiModelClient:
    def __init__(self, config, **kwargs):
        print(f"CustomModelClient config: {config}")
        self.api_key = config.get("api_key")
        self.api_url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
        self.model = config.get("model", "gpt-3.5-turbo")
        self.max_tokens = config.get("max_tokens", 1200)
        self.temperature = config.get("temperature", 0.8)
        self.top_p = config.get("top_p", 1)
        self.presence_penalty = config.get("presence_penalty", 1)

        print(f"Initialized CustomModelClient with model {self.model}")

    def create(self, params):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        data = {
            "max_tokens": self.max_tokens,
            "model": self.model,
            "temperature": self.temperature,
            "top_p": self.top_p,
            "presence_penalty": self.presence_penalty,
            "messages": params.get("messages", []),
        }

        response = requests.post(self.api_url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors

        api_response = response.json()

        # Convert API response to SimpleNamespace for compatibility
        client_response = SimpleNamespace()
        client_response.choices = []
        client_response.model = self.model

        for choice in api_response.get("choices", []):
            client_choice = SimpleNamespace()
            client_choice.message = SimpleNamespace()
            client_choice.message.content = choice.get("message", {}).get("content")
            client_choice.message.function_call = None
            client_response.choices.append(client_choice)

        return client_response

    def message_retrieval(self, response):
        """Retrieve the messages from the response."""
        choices = response.choices
        return [choice.message.content for choice in choices]

    def cost(self, response) -> float:
        """Calculate the cost of the response."""
        # Implement cost calculation if available from your API
        response.cost = 0
        return 0

    @staticmethod
    def get_usage(response):
        # Implement usage tracking if available from your API
        return {}

