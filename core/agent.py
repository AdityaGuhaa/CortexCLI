from providers.gemini import GeminiProvider

class Agent:
    def __init__(self):
        self.provider = GeminiProvider()

    def handle_query(self, query: str) -> str:
        return self.provider.generate(query)