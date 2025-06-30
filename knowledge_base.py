"""
Knowledge base containing predefined Thoughtful AI questions and responses.
This module handles the storage and retrieval of company-specific information.
"""

import json
from typing import Dict, List, Tuple, Optional
from difflib import SequenceMatcher

class ThoughtfulAIKnowledgeBase:
    """Manages predefined questions and answers for Thoughtful AI customer support."""
    
    def __init__(self):
        """Initialize the knowledge base with predefined Q&A pairs."""
        self.qa_pairs = {
            "What does the eligibility verification agent (EVA) do?": {
                "answer": "EVA automates the process of verifying a patient's eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections.",
                "keywords": ["eva", "eligibility", "verification", "agent", "patient", "benefits", "eligibility verification agent"]
            },
            "What does the claims processing agent (CAM) do?": {
                "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements.",
                "keywords": ["cam", "claims", "processing", "agent", "submission", "management", "claims processing agent"]
            },
            "How does the payment posting agent (PHIL) work?": {
                "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden.",
                "keywords": ["phil", "payment", "posting", "agent", "accounts", "reconciliation", "payment posting agent"]
            },
            "Tell me about Thoughtful AI's Agents.": {
                "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others.",
                "keywords": ["thoughtful ai", "agents", "automation", "suite", "eva", "cam", "phil", "healthcare"]
            },
            "What are the benefits of using Thoughtful AI's agents?": {
                "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting.",
                "keywords": ["benefits", "advantages", "reduce costs", "efficiency", "errors", "administrative", "claims management"]
            },
            "What is Thoughtful AI?": {
                "answer": "Thoughtful AI is a leading artificial intelligence company that specializes in developing intelligent automation solutions for businesses. We focus on creating AI systems that enhance human capabilities and streamline complex workflows.",
                "keywords": ["what is", "thoughtful ai", "company", "about"]
            },
            "What services does Thoughtful AI offer?": {
                "answer": "Thoughtful AI offers a comprehensive suite of AI services including: intelligent document processing, automated data extraction, workflow automation, custom AI model development, and AI integration consulting. We help businesses automate repetitive tasks and make data-driven decisions.",
                "keywords": ["services", "offer", "products", "solutions", "what do you do"]
            },
            "How can I contact Thoughtful AI support?": {
                "answer": "You can contact Thoughtful AI support through multiple channels: Email us at support@thoughtfulai.com, use this chat interface for immediate assistance, or visit our website's contact page. Our support team is available Monday through Friday, 9 AM to 6 PM EST.",
                "keywords": ["contact", "support", "help", "reach", "email"]
            },
            "What are Thoughtful AI's pricing plans?": {
                "answer": "Thoughtful AI offers flexible pricing plans tailored to different business needs: Starter Plan for small teams, Professional Plan for growing businesses, and Enterprise Plan for large organizations. Contact our sales team for detailed pricing information and custom solutions.",
                "keywords": ["pricing", "cost", "plans", "price", "how much"]
            },
            "Is my data secure with Thoughtful AI?": {
                "answer": "Yes, data security is our top priority. Thoughtful AI implements enterprise-grade security measures including end-to-end encryption, SOC 2 compliance, GDPR compliance, and regular security audits. Your data is processed securely and never shared with third parties.",
                "keywords": ["security", "data protection", "privacy", "secure", "safe"]
            }
        }
    
    def find_best_match(self, user_question: str, threshold: float = 0.3) -> Optional[Tuple[str, Dict]]:
        """
        Find the best matching predefined question using fuzzy matching.
        
        Args:
            user_question: The user's input question
            threshold: Minimum similarity score to consider a match
            
        Returns:
            Tuple of (question, answer_data) if match found, None otherwise
        """
        user_question_lower = user_question.lower().strip()
        best_match = None
        best_score = 0
        
        for question, answer_data in self.qa_pairs.items():
            # Calculate similarity with the question itself
            question_similarity = SequenceMatcher(None, user_question_lower, question.lower()).ratio()
            
            # Calculate similarity with keywords
            keyword_similarity = 0
            for keyword in answer_data["keywords"]:
                if keyword in user_question_lower:
                    keyword_similarity += 0.2  # Boost for keyword matches
            
            # Combined score
            total_score = max(question_similarity, keyword_similarity)
            
            if total_score > best_score and total_score >= threshold:
                best_score = total_score
                best_match = (question, answer_data)
        
        return best_match
    
    def get_all_questions(self) -> List[str]:
        """Get all predefined questions for reference."""
        return list(self.qa_pairs.keys())
    
    def add_qa_pair(self, question: str, answer: str, keywords: List[str]):
        """Add a new Q&A pair to the knowledge base."""
        self.qa_pairs[question] = {
            "answer": answer,
            "keywords": keywords
        }
