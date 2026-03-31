# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
This is a CLI chat application built with Python using the Textual framework. The application supports multiple AI providers (Gemini, OpenAI, Ollama) and includes slash commands for enhanced functionality.

## Code Architecture
- `main.py`: Entry point that initializes and runs the Textual ChatApp
- `ui/app.py`: Main Textual application with UI components and event handling
- `core/agent.py`: Core agent that routes queries to the appropriate AI provider
- `providers/`: Directory containing provider implementations (Gemini, OpenAI, Ollama)
- `commands/slash_commands.py`: Handler for slash commands like /clear and /exit
- `utils/`: Utility functions (currently minimal implementation)

## Development Commands
To run the application:
```bash
python main.py
```

To install dependencies:
```bash
pip install -r requirements.txt
```

Key dependencies:
- textual: Textual UI framework
- google-generativeai: Google Gemini API client
- openai: OpenAI API client
- ollama: Ollama API client
- python-dotenv: Environment variable management

## Environment Setup
The application uses environment variables for API keys:
- GEMINI_API_KEY: For Google Gemini provider

## Application Flow
1. User interface is handled by Textual framework in `ui/app.py`
2. User inputs are processed in the `on_input_submitted` method
3. Slash commands (starting with '/') are handled by `CommandHandler`
4. Regular queries are processed by the `Agent` class in `core/agent.py`
5. Agent routes queries to the configured provider (currently Gemini)

## Current Implementation Status
- Core UI framework is functional with chat history display
- Gemini provider is implemented and integrated
- Slash commands for clearing chat (/clear) and exiting (/exit) are available
- OpenAI and Ollama provider files exist but appear to be placeholders
- Some utility files exist but are currently empty