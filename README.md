# Thoughtful AI Customer Support Agent

A Streamlit-based customer support AI agent specifically designed for Thoughtful AI. This application provides an interactive chat interface that combines predefined knowledge base responses with AI-powered fallback capabilities using OpenAI's API.

## Features

- **Predefined Responses**: Instant answers to common Thoughtful AI questions about healthcare automation agents (EVA, CAM, PHIL)
- **AI Fallback**: OpenAI-powered responses for questions outside the knowledge base
- **Interactive UI**: User-friendly Streamlit chat interface with conversation history
- **Confidence Scoring**: Visual indicators showing response source and confidence levels
- **Error Handling**: Graceful handling of invalid inputs and API failures

## Healthcare Automation Agents

The agent can answer questions about Thoughtful AI's specialized healthcare automation agents:

- **EVA (Eligibility Verification Agent)**: Automates patient eligibility and benefits verification
- **CAM (Claims Processing Agent)**: Streamlines claims submission and management
- **PHIL (Payment Posting Agent)**: Automates payment posting and reconciliation

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd thoughtful-ai-support-agent
```

2. Install dependencies:
```bash
pip install -r requirements-repo.txt
```

3. Set up environment variables:
```bash
export OPENAI_API_KEY="your-openai-api-key"
```

## Configuration

Create a `.streamlit/config.toml` file with the following configuration:

```toml
[server]
headless = true
address = "0.0.0.0"
port = 5000
```

## Usage

1. Start the application:
```bash
streamlit run app.py --server.port 5000
```

2. Open your browser and navigate to `http://localhost:5000`

3. Start asking questions about Thoughtful AI or any other topic!

## Project Structure

```
├── app.py                 # Main Streamlit application
├── ai_agent.py           # AI agent orchestration logic
├── knowledge_base.py     # Predefined Q&A pairs for Thoughtful AI
├── .streamlit/
│   └── config.toml       # Streamlit server configuration
├── requirements-repo.txt # Python dependencies
├── README.md            # This file
└── .gitignore           # Git ignore patterns
```

## Architecture

The application follows a modular three-layer architecture:

1. **Presentation Layer** (`app.py`): Streamlit web interface
2. **Business Logic Layer** (`ai_agent.py`): Message processing and response orchestration
3. **Data Layer** (`knowledge_base.py`): Knowledge base management with fuzzy matching

## Environment Variables

- `OPENAI_API_KEY`: Required for AI fallback functionality (optional but recommended)

## Sample Questions

Try asking about:
- "What does EVA do?"
- "What does CAM do?"
- "How does PHIL work?"
- "Tell me about Thoughtful AI's Agents"
- "What are the benefits of using Thoughtful AI's agents?"

## Response Sources

The agent provides visual indicators for response sources:

- 📚 **Knowledge Base**: Predefined responses (highest confidence)
- 🤖 **AI Generated**: OpenAI-powered responses
- ⚠️ **Fallback Response**: Basic response when AI is unavailable
- ❌ **Error Response**: Error handling messages

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions about this application or Thoughtful AI services, contact:
- Email: support@thoughtfulai.com
- Use the chat interface for immediate assistance
