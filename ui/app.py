from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Static
from textual.containers import VerticalScroll
from threading import Thread

from core.agent import Agent
from commands.slash_commands import CommandHandler


class ChatApp(App):

    CSS = """
    Screen {
        layout: vertical;
    }

    #chat_container {
        height: 1fr;
        border: round green;
        padding: 1;
    }

    Input {
        dock: bottom;
    }
    """

    def __init__(self):
        super().__init__()
        self.agent = Agent()
        self.command_handler = CommandHandler(self)
        self.chat_history = []

    def compose(self) -> ComposeResult:
        yield Header()

        # ✅ Proper scroll container
        self.chat_container = VerticalScroll(id="chat_container")
        yield self.chat_container

        self.input = Input(placeholder="Ask something... (/clear, /exit)")
        yield self.input

        yield Footer()

    def on_mount(self):
        # Start with empty chat
        self.chat_display = Static("")
        self.chat_container.mount(self.chat_display)

    def on_input_submitted(self, event: Input.Submitted):
        user_input = event.value.strip()
        self.input.value = ""

        if not user_input:
            return

        self.add_message("You", user_input, "cyan")

        if user_input.startswith("/"):
            self.command_handler.handle(user_input)
            return

        self.show_loading()

        Thread(target=self.process_query, args=(user_input,), daemon=True).start()

    def process_query(self, query):
        response = self.agent.handle_query(query)
        self.call_from_thread(self.finish_response, response)

    def finish_response(self, response):
        self.remove_loading()
        self.add_message("AI", response, "green")

    def add_message(self, sender, message, color):
        formatted = f"[bold {color}]{sender}:[/] {message}"
        self.chat_history.append(formatted)

        self.chat_display.update("\n\n".join(self.chat_history))

        # ✅ Auto scroll to bottom
        self.chat_container.scroll_end()

    def show_loading(self):
        self.chat_display.update(
            "\n\n".join(self.chat_history + ["[yellow]AI is thinking...[/]"])
        )
        self.chat_container.scroll_end()

    def remove_loading(self):
        self.chat_display.update("\n\n".join(self.chat_history))

    def clear_chat(self):
        self.chat_history = []
        self.agent.clear_memory()
        self.chat_display.update("")


if __name__ == "__main__":
    app = ChatApp()
    app.run()