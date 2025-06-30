"""
Streamlit-based customer support AI agent for Thoughtful AI.
Provides interactive chat interface with predefined responses and AI fallback.
"""

import streamlit as st
from datetime import datetime
from typing import Optional
from ai_agent import ThoughtfulAIAgent

# Page configuration
st.set_page_config(
    page_title="Thoughtful AI Customer Support",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="auto"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "agent" not in st.session_state:
    st.session_state.agent = ThoughtfulAIAgent()

def add_message(role: str, content: str, metadata: Optional[dict] = None):
    """Add a message to the conversation history."""
    if metadata is None:
        metadata = {}
    message = {
        "role": role,
        "content": content,
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "metadata": metadata
    }
    st.session_state.messages.append(message)

def display_message(message: dict):
    """Display a single message in the chat interface."""
    with st.chat_message(message["role"]):
        st.write(message["content"])
        
        # Show metadata for agent responses
        if message["role"] == "assistant" and message.get("metadata"):
            metadata = message["metadata"]
            
            # Create columns for metadata display
            col1, col2, col3 = st.columns([1, 1, 2])
            
            with col1:
                if metadata.get("source") == "predefined":
                    st.caption("📚 Knowledge Base")
                elif metadata.get("source") == "ai_generated":
                    st.caption("🤖 AI Generated")
                elif metadata.get("source") == "fallback":
                    st.caption("⚠️ Fallback Response")
                elif metadata.get("source") == "error":
                    st.caption("❌ Error Response")
            
            with col2:
                if "confidence" in metadata:
                    confidence = metadata["confidence"]
                    confidence_text = f"Confidence: {confidence:.0%}"
                    if confidence >= 0.8:
                        st.caption(f"✅ {confidence_text}")
                    elif confidence >= 0.5:
                        st.caption(f"⚡ {confidence_text}")
                    else:
                        st.caption(f"⚠️ {confidence_text}")
            
            with col3:
                st.caption(f"🕒 {message['timestamp']}")

def main():
    """Main application function."""
    
    # Header
    st.title("🤖 Thoughtful AI Customer Support")
    st.markdown("Welcome! I'm here to help you with questions about Thoughtful AI and provide general assistance.")
    
    # Sidebar with information
    with st.sidebar:
        st.header("💡 How I Can Help")
        
        st.markdown("""
        **I can assist you with:**
        - Questions about Thoughtful AI services
        - Company information and pricing
        - Technical support inquiries
        - General AI-related questions
        """)
        
        if st.session_state.agent.is_openai_available():
            st.success("🔗 AI Fallback: Available")
        else:
            st.warning("⚠️ AI Fallback: Limited (API key needed)")
        
        st.markdown("---")
        
        # Sample questions
        st.subheader("📋 Sample Questions")
        sample_questions = [
            "What does EVA do?",
            "What does CAM do?",
            "How does PHIL work?",
            "Tell me about Thoughtful AI's Agents",
            "What are the benefits of using Thoughtful AI's agents?"
        ]
        
        for question in sample_questions:
            if st.button(question, key=f"sample_{question}", use_container_width=True):
                # Add user message
                add_message("user", question)
                
                # Process and add agent response
                with st.spinner("Thinking..."):
                    response = st.session_state.agent.process_message(
                        question, 
                        st.session_state.messages
                    )
                
                add_message("assistant", response["response"], response)
                st.rerun()
        
        st.markdown("---")
        
        # Clear conversation button
        if st.button("🗑️ Clear Conversation", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
    
    # Display conversation history
    if st.session_state.messages:
        st.subheader("💬 Conversation")
        
        for message in st.session_state.messages:
            display_message(message)
    else:
        # Welcome message
        st.info("👋 Ask me anything about Thoughtful AI or any other topic you need help with!")
    
    # Chat input
    user_input = st.chat_input("Type your message here...")
    
    if user_input:
        # Add user message
        add_message("user", user_input)
        
        # Display user message immediately
        with st.chat_message("user"):
            st.write(user_input)
        
        # Process and display agent response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.agent.process_message(
                    user_input, 
                    st.session_state.messages
                )
            
            # Display response
            st.write(response["response"])
            
            # Display metadata
            col1, col2, col3 = st.columns([1, 1, 2])
            
            with col1:
                if response.get("source") == "predefined":
                    st.caption("📚 Knowledge Base")
                elif response.get("source") == "ai_generated":
                    st.caption("🤖 AI Generated")
                elif response.get("source") == "fallback":
                    st.caption("⚠️ Fallback Response")
                elif response.get("source") == "error":
                    st.caption("❌ Error Response")
            
            with col2:
                if "confidence" in response:
                    confidence = response["confidence"]
                    confidence_text = f"Confidence: {confidence:.0%}"
                    if confidence >= 0.8:
                        st.caption(f"✅ {confidence_text}")
                    elif confidence >= 0.5:
                        st.caption(f"⚡ {confidence_text}")
                    else:
                        st.caption(f"⚠️ {confidence_text}")
            
            with col3:
                current_time = datetime.now().strftime("%H:%M:%S")
                st.caption(f"🕒 {current_time}")
        
        # Add agent response to history
        add_message("assistant", response["response"], response)
        
        # Rerun to update the conversation display
        st.rerun()

if __name__ == "__main__":
    main()
