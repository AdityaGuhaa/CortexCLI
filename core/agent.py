from providers.gemini import GeminiProvider


class Agent:
    def __init__(self):
        self.provider = GeminiProvider()
        self.memory = []   # 🧠 store conversation

    def handle_query(self, query: str) -> str:
        # Add user message
        self.memory.append({
            "role": "user",
            "content": query
        })

        # Convert memory → prompt
        prompt = self.build_prompt()

        # Get response
        response = self.provider.generate(prompt)

        # Add AI response to memory
        self.memory.append({
            "role": "assistant",
            "content": response
        })

        return response

    def build_prompt(self) -> str:
        """Convert chat history into a single prompt"""
        formatted = []

        for msg in self.memory:
            if msg["role"] == "user":
                formatted.append(f"User: {msg['content']}")
            else:
                formatted.append(f"AI: {msg['content']}")

        return "\n".join(formatted)

    def clear_memory(self):
        self.memory = []