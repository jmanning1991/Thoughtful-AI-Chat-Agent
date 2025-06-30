# Thoughtful AI Customer Support Agent

## Overview

This repository contains a Streamlit-based customer support AI agent specifically designed for Thoughtful AI. The application provides an interactive chat interface that combines predefined knowledge base responses with AI-powered fallback capabilities using OpenAI's API. The system is designed to handle customer inquiries efficiently by first attempting to match questions against a curated knowledge base, and falling back to AI generation when needed.

## System Architecture

The application follows a modular, three-layer architecture:

1. **Presentation Layer**: Streamlit web interface (`app.py`)
2. **Business Logic Layer**: AI agent orchestration (`ai_agent.py`)
3. **Data Layer**: Knowledge base management (`knowledge_base.py`)

This separation of concerns allows for easy maintenance, testing, and scalability. The architecture prioritizes deterministic responses from the knowledge base while providing intelligent fallback through OpenAI integration.

## Key Components

### AI Agent (`ai_agent.py`)
- **Purpose**: Central orchestrator that coordinates response generation
- **Responsibilities**: Message processing, knowledge base querying, OpenAI fallback handling
- **Design Decision**: Hybrid approach combining rule-based and AI-generated responses to ensure accuracy for common queries while maintaining flexibility

### Knowledge Base (`knowledge_base.py`)
- **Purpose**: Stores and manages predefined Q&A pairs specific to Thoughtful AI
- **Responsibilities**: Fuzzy string matching, keyword-based search, confidence scoring
- **Design Decision**: Uses `difflib.SequenceMatcher` for fuzzy matching to handle variations in user phrasing while maintaining response accuracy

### Streamlit Interface (`app.py`)
- **Purpose**: Provides user-friendly chat interface
- **Responsibilities**: Session management, message display, conversation history
- **Design Decision**: Chose Streamlit for rapid prototyping and built-in session state management

## Data Flow

1. User submits message through Streamlit interface
2. AI Agent receives message and conversation history
3. Knowledge Base performs fuzzy matching against predefined Q&A pairs
4. If match found with sufficient confidence: return predefined response
5. If no match or low confidence: fallback to OpenAI API generation
6. Response returned to Streamlit interface with metadata (source, confidence)
7. Message added to conversation history for context

## External Dependencies

### Core Dependencies
- **Streamlit**: Web interface framework chosen for rapid development and built-in features
- **OpenAI**: Fallback AI generation when knowledge base responses are insufficient
- **difflib**: Python standard library for fuzzy string matching (no external dependency)

### Environment Variables
- `OPENAI_API_KEY`: Required for AI fallback functionality

## Deployment Strategy

The application is designed for cloud deployment with the following considerations:

### Environment Setup
- Requires Python 3.7+ environment
- Environment variables for API keys
- Streamlit server configuration for production deployment

### Scalability Considerations
- Stateless design allows for horizontal scaling
- Knowledge base is loaded in memory for fast access
- OpenAI API calls are made only when necessary to manage costs

### Production Recommendations
- Implement caching for OpenAI responses
- Add logging and monitoring
- Consider database storage for conversation history
- Implement rate limiting for API calls

## User Preferences

Preferred communication style: Simple, everyday language.

## Recent Changes

- June 30, 2025: Updated knowledge base with specific Thoughtful AI healthcare automation agents (EVA, CAM, PHIL)
- June 30, 2025: Updated sample questions in UI to focus on the three main agents
- June 30, 2025: Configured OpenAI API integration for AI fallback responses
- June 30, 2025: Initial setup with modular architecture

## Changelog

Changelog:
- June 30, 2025. Initial setup
- June 30, 2025. Updated knowledge base with required Thoughtful AI agent information