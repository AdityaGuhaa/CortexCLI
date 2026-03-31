from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Static
from textual.containers import VerticalScroll
from threading import Thread
import time

from rich.markdown import Markdown

from core.agent import Agent
from commands.slash_commands import CommandHandler


class ChatApp(App):

    TITLE = "CortexCLI"
    SUB_TITLE = "AI-powered Terminal Assistant"

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
        border: solid cyan;
    }
    """

    def __init__(self):
        super().__init__()
        self.title = "CortexCLI"  # ✅ Terminal window title

        self.agent = Agent()
        self.command_handler = CommandHandler(self)

        self.chat_history = []
        self.current_stream = ""

    def compose(self) -> ComposeResult:
        yield Header()

        self.chat_container = VerticalScroll(id="chat_container")
        yield self.chat_container

        self.input = Input(placeholder="Ask something... (/clear, /exit)")
        yield self.input

        yield Footer()

    def on_mount(self):
        self.chat_display = Static(
            Markdown("# CortexCLI\n\n_AI-powered terminal assistant ready..._")
        )
        self.chat_container.mount(self.chat_display)

    def on_input_submitted(self, event: Input.Submitted):
        user_input = event.value.strip()
        self.input.value = ""

        if not user_input:
            return

        # User message
        self.add_message("You", user_input)

        if user_input.startswith("/"):
            self.command_handler.handle(user_input)
            return

        self.show_loading()

        Thread(target=self.process_query, args=(user_input,), daemon=True).start()

    def process_query(self, query):
        response = self.agent.handle_query(query)
        self.call_from_thread(self.start_streaming, response)

    def start_streaming(self, full_text):
        self.remove_loading()

        self.current_stream = ""
        self.chat_history.append("**AI:** ")
        self.update_chat()

        def stream():
            for char in full_text:
                self.current_stream += char
                self.chat_history[-1] = f"**AI:** {self.current_stream}"

                self.call_from_thread(self.update_chat)
                time.sleep(0.01)

        Thread(target=stream, daemon=True).start()

    def update_chat(self):
        combined = "\n\n".join(self.chat_history)
        self.chat_display.update(Markdown(combined))
        self.chat_container.scroll_end()

    def add_message(self, sender, message):
        formatted = f"**{sender}:** {message}"
        self.chat_history.append(formatted)
        self.update_chat()

    def show_loading(self):
        combined = "\n\n".join(self.chat_history + ["_AI is thinking..._"])
        self.chat_display.update(Markdown(combined))
        self.chat_container.scroll_end()

    def remove_loading(self):
        self.update_chat()

    def clear_chat(self):
        self.chat_history = []
        self.agent.clear_memory()
        self.chat_display.update("")


if __name__ == "__main__":
    app = ChatApp()
    app.run()