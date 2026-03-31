from providers.gemini import GeminiProvider


class Agent:
    def __init__(self):
        self.provider = GeminiProvider()
        self.memory = []

    def handle_query(self, query: str) -> str:
        self.memory.append({"role": "user", "content": query})

        prompt = self.build_prompt()
        response = self.provider.generate(prompt)

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