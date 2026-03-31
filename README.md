# CortexCLI

CortexCLI is an advanced command-line interface chat application that provides seamless interaction with multiple artificial intelligence providers through a unified Textual-based terminal interface. Built with Python, this application offers developers and users a powerful tool for accessing various AI models without leaving their terminal environment.

## Features

- Interactive terminal-based chat interface using Textual framework
- Support for multiple AI providers (Google Gemini, OpenAI, Ollama)
- Slash command system for enhanced functionality
- Persistent chat history during sessions
- Clean and intuitive user interface
- Extensible architecture for adding new providers and features
- Docker containerization for easy deployment and consistent environments

## Architecture Overview

The application follows a modular architecture pattern with clearly defined components:

### Core Components

1. **Main Application (`main.py`)**
   - Entry point for the application
   - Initializes and runs the Textual ChatApp

2. **UI Layer (`ui/app.py`)**
   - Implements the Textual-based user interface
   - Handles user input events and display rendering
   - Manages chat history visualization
   - Integrates with the core agent for processing queries

3. **Core Services (`core/`)**
   - `agent.py`: Central processing unit that routes queries to appropriate AI providers
   - Placeholder files for router and context management functionality

4. **AI Providers (`providers/`)**
   - `gemini.py`: Implementation for Google Gemini API integration
   - Placeholder files for OpenAI and Ollama integrations
   - Standardized interfaces for consistent provider interaction

5. **Commands (`commands/slash_commands.py`)**
   - Implementation of slash commands for enhanced functionality
   - Currently supports /clear and /exit commands

6. **Utilities (`utils/`)**
   - Placeholder directory for utility functions and helpers

## Installation

### Prerequisites

- Python 3.8 or higher (for direct installation)
- pip package manager
- Virtual environment (recommended)
- Docker (for containerized deployment)

### Dependencies

The application requires the following Python packages:
- textual: Advanced Textual User Interface framework
- rich: Rich text and beautiful formatting in the terminal
- google-generativeai: Google Generative AI client library
- openai: Official OpenAI Python client library
- ollama: Client library for Ollama local AI models
- python-dotenv: Environment variable management

### Setup Process (Direct Installation)

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd CortexCLI
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   Create a `.env` file in the project root with your API keys:
   ```
   GEMINI_API_KEY=your_google_gemini_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here  # If using OpenAI
   ```

### Setup Process (Docker Installation)

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd CortexCLI
   ```

2. Build the Docker image:
   ```bash
   docker build -t cortexcli .
   ```

3. Run the container with environment variables:
   ```bash
   docker run -it --env-file .env cortexcli
   ```

   Or use docker-compose:
   ```bash
   docker-compose up
   ```

4. For development with live code changes:
   ```bash
   docker-compose run --rm cortexcli
   ```

## Usage

### Running the Application (Direct Installation)

To start the CortexCLI application:
```bash
python main.py
```

Once launched, you'll be presented with a terminal-based chat interface where you can interact with the AI providers.

### Running the Application (Docker)

To run the application in a Docker container:
```bash
docker run -it --env-file .env cortexcli
```

Or with docker-compose:
```bash
docker-compose up
```

### Interaction Methods

1. **Direct Queries**
   Simply type your question or prompt and press Enter to send it to the AI provider.

2. **Slash Commands**
   Special commands prefixed with '/' provide additional functionality:
   - `/clear`: Clears the current chat history from the display
   - `/exit`: Exits the application gracefully

### AI Provider Selection

Currently, the application is configured to use Google Gemini as the primary provider. Future enhancements will allow dynamic selection between different AI providers.

## Configuration

### Environment Variables

The application uses environment variables for secure API key management:
- `GEMINI_API_KEY`: Required for Google Gemini integration
- `OPENAI_API_KEY`: Required for OpenAI integration (when implemented)
- Additional provider-specific variables as needed

Create a `.env` file in the project root directory with your API keys.

## Development

### Project Structure

```
CortexCLI/
├── commands/
│   └── slash_commands.py
├── core/
│   ├── agent.py
│   ├── context_manager.py (placeholder)
│   └── router.py (placeholder)
├── providers/
│   ├── gemini.py
│   ├── openai.py (placeholder)
│   └── ollama.py (placeholder)
├── ui/
│   ├── app.py
│   └── components.py (placeholder)
├── utils/
│   ├── config.py (placeholder)
│   └── file_parser.py (placeholder)
├── Dockerfile
├── docker-compose.yml
├── main.py
├── requirements.txt
└── README.md
```

### Adding New Providers

To extend the application with additional AI providers:

1. Create a new provider file in the `providers/` directory
2. Implement the required interface methods
3. Update the agent configuration to include the new provider
4. Add any necessary environment variables

### Docker Development

For development with Docker:

1. Modify code files locally (they are mounted as volumes in the container)
2. Rebuild the image when adding new dependencies:
   ```bash
   docker-compose build
   ```
3. Run tests in the container:
   ```bash
   docker-compose run --rm cortexcli python -m pytest
   ```

### Code Standards

- Follow PEP 8 Python coding standards
- Use type hints for function parameters and return values
- Maintain consistent naming conventions
- Document complex functionality with clear comments

## Troubleshooting

### Common Issues

1. **API Key Errors**
   - Verify that your API keys are correctly set in the `.env` file
   - Ensure that the environment variables are properly loaded

2. **Dependency Issues**
   - Confirm all dependencies are installed via `pip install -r requirements.txt`
   - Check Python version compatibility

3. **Display Problems**
   - Ensure terminal supports Textual framework requirements
   - Check terminal dimensions and color support

### Getting Help

For issues not covered in this documentation:
- Check the project's issue tracker
- Consult the Textual framework documentation
- Review the documentation for specific AI provider APIs

## Future Enhancements

Planned improvements include:
- Full implementation of OpenAI and Ollama providers
- Enhanced context management for conversational continuity
- Advanced routing capabilities for intelligent provider selection
- Extended slash command system with plugin support
- Configuration file support for persistent settings
- Improved error handling and user feedback mechanisms

## Contributing

Contributions are welcome. Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request with a clear description of the changes

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Textual framework for the terminal UI capabilities
- Google Generative AI for the Gemini integration
- OpenAI for their API interfaces
- Ollama for local AI model support