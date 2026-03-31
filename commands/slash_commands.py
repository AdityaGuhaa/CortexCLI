class CommandHandler:
    def __init__(self, app):
        self.app = app

    def handle(self, command: str):
        parts = command.split()

        if parts[0] == "/clear":
            self.app.clear_chat()

        elif parts[0] == "/exit":
            self.app.exit()

        elif parts[0] == "/model":
            if len(parts) < 2:
                self.app.add_message("System", "Usage: /model [gemini|ollama]")
                return

            result = self.app.agent.switch_provider(parts[1])
            self.app.add_message("System", result)

        else:
            self.app.add_message("System", f"Unknown command: {command}")