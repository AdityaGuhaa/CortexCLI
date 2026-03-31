from providers.gemini import GeminiProvider
from providers.ollama import OllamaProvider


class Agent:
    def __init__(self):
        self.providers = {
            "gemini": GeminiProvider(),
            "ollama": OllamaProvider()
        }

        self.current_provider = "gemini"
        self.memory = []

    def switch_provider(self, name: str) -> str:
        if name in self.providers:
            self.current_provider = name
            return f"Switched to {name}"
        return f"Unknown provider: {name}"

    def handle_query(self, query: str) -> str:
        self.memory.append({"role": "user", "content": query})

        prompt = self.build_prompt()
        provider = self.providers[self.current_provider]

        response = provider.generate(prompt)

        self.memory.append({"role": "assistant", "content": response})
        return response

    def build_prompt(self) -> str:
        formatted = []

        for msg in self.memory:
            role = "User" if msg["role"] == "user" else "AI"
            formatted.append(f"{role}: {msg['content']}")

        return "\n".join(formatted)

    def clear_memory(self):
        self.memory = []