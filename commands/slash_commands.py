class CommandHandler:
    def __init__(self, app):
        self.app = app

    def handle(self, command: str):
        if command == "/clear":
            self.app.clear_chat()
        elif command == "/exit":
            self.app.exit()
        else:
            self.app.add_message("System", f"Unknown command: {command}")