"""
AI Agent module that handles both predefined responses and OpenAI fallback.
This module orchestrates the conversation flow and response generation.
"""

import os
import json
from typing import Dict, Optional, Tuple
from openai import OpenAI
from knowledge_base import ThoughtfulAIKnowledgeBase

class ThoughtfulAIAgent:
    """Customer support AI agent with predefined responses and AI fallback."""
    
    def __init__(self):
        """Initialize the AI agent with knowledge base and OpenAI client."""
        self.knowledge_base = ThoughtfulAIKnowledgeBase()
        
        # Initialize OpenAI client
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "")
        if self.openai_api_key:
            self.openai_client = OpenAI(api_key=self.openai_api_key)
        else:
            self.openai_client = None
    
    def process_message(self, user_message: str, conversation_history: list = None) -> Dict:
        """
        Process a user message and return an appropriate response.
        
        Args:
            user_message: The user's input message
            conversation_history: Previous conversation messages
            
        Returns:
            Dictionary containing response, source, and confidence
        """
        if not user_message or not user_message.strip():
            return {
                "response": "I'm here to help! Please ask me a question about Thoughtful AI or any other topic you need assistance with.",
                "source": "system",
                "confidence": 1.0,
                "error": None
            }
        
        try:
            # First, try to find a predefined response
            match = self.knowledge_base.find_best_match(user_message)
            
            if match:
                question, answer_data = match
                return {
                    "response": answer_data["answer"],
                    "source": "predefined",
                    "confidence": 1.0,
                    "matched_question": question,
                    "error": None
                }
            
            # If no predefined match, use OpenAI fallback
            if self.openai_client:
                ai_response = self._get_ai_response(user_message, conversation_history)
                return {
                    "response": ai_response,
                    "source": "ai_generated",
                    "confidence": 0.8,
                    "error": None
                }
            else:
                return {
                    "response": "I don't have a specific answer for that question about Thoughtful AI. For detailed information, please contact our support team at support@thoughtfulai.com or visit our website.",
                    "source": "fallback",
                    "confidence": 0.5,
                    "error": "OpenAI API not available"
                }
                
        except Exception as e:
            return {
                "response": "I apologize, but I'm experiencing technical difficulties. Please try again in a moment or contact our support team directly at support@thoughtfulai.com.",
                "source": "error",
                "confidence": 0.0,
                "error": str(e)
            }
    
    def _get_ai_response(self, user_message: str, conversation_history: list = None) -> str:
        """
        Get response from OpenAI for non-Thoughtful AI questions.
        
        Args:
            user_message: The user's input message
            conversation_history: Previous conversation messages
            
        Returns:
            AI-generated response string
        """
        try:
            # Build conversation context
            messages = [
                {
                    "role": "system",
                    "content": """You are a helpful customer support AI assistant. 
                    You should provide helpful, accurate, and professional responses to user questions.
                    Keep responses concise but informative. If you don't know something, be honest about it.
                    Maintain a friendly and professional tone appropriate for customer support."""
                }
            ]
            
            # Add conversation history if available
            if conversation_history:
                for msg in conversation_history[-6:]:  # Last 6 messages for context
                    if msg["role"] in ["user", "assistant"]:
                        messages.append({
                            "role": msg["role"],
                            "content": msg["content"]
                        })
            
            # Add current user message
            messages.append({
                "role": "user",
                "content": user_message
            })
            
            # the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
            # do not change this unless explicitly requested by the user
            response = self.openai_client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            raise Exception(f"Failed to get AI response: {str(e)}")
    
    def get_available_topics(self) -> list:
        """Get list of topics the agent can help with."""
        return self.knowledge_base.get_all_questions()
    
    def is_openai_available(self) -> bool:
        """Check if OpenAI integration is available."""
        return self.openai_client is not None
