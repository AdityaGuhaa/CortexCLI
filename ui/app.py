from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Static
from core.agent import Agent
from commands.slash_commands import CommandHandler


class ChatApp(App):

    CSS = """
    Screen {
        layout: vertical;
    }

    #chat {
        height: 1fr;
        border: solid green;
        padding: 1;
        overflow-y: auto;
    }

    Input {
        dock: bottom;
    }
    """

    def __init__(self):
        super().__init__()
        self.agent = Agent()
        self.command_handler = CommandHandler(self)
        self.chat_history = []   # ✅ FIX: store messages here

    def compose(self) -> ComposeResult:
        yield Header()
        self.chat = Static("", id="chat")
        yield self.chat
        self.input = Input(placeholder="Ask something...")
        yield self.input
        yield Footer()

    def on_input_submitted(self, event: Input.Submitted):
        user_input = event.value.strip()
        self.input.value = ""

        if not user_input:
            return

        self.add_message("You", user_input)

        if user_input.startswith("/"):
            self.command_handler.handle(user_input)
            return

        response = self.agent.handle_query(user_input)
        self.add_message("AI", response)

    def add_message(self, sender, message):
        self.chat_history.append(f"[{sender}] {message}")
        self.chat.update("\n".join(self.chat_history))

    def clear_chat(self):
        self.chat_history = []
        self.chat.update("")

if __name__ == "__main__":
    app = ChatApp()
    app.run()