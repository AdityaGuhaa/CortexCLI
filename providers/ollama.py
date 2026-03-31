import requests
import os


class OllamaProvider:
    def __init__(self):
        self.base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.api_key = os.getenv("OLLAMA_API_KEY")  # optional
        self.model = "llama3"

    def generate(self, prompt: str) -> str:
        try:
            headers = {}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"

            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                },
                headers=headers
            )

            data = response.json()
            return data.get("response", "No response")

        except Exception as e:
            return f"[OLLAMA ERROR] {str(e)}"