# Auto-Generated
# File Name: memory_illusion.py 
# Author: scotton
# Creation Date: January-22-2026
# Modified Date: January-22-2026

"""Demonstration of how LLM conversation memory works.

This module demonstrates that LLM API calls are completely stateless.
The illusion of "memory" in chat applications is created by passing
the entire conversation history with each request.

Based on week1/day4.ipynb
"""

import os
from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI


def validate_api_key() -> Optional[str]:
    """Validate that OpenAI API key is properly configured.
    
    Returns:
        The API key if valid, None otherwise
    """
    load_dotenv(override=True)
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("Error: No API key was found. Please set OPENAI_API_KEY in .env file")
        return None
    elif not api_key.startswith("sk-proj-"):
        print("Warning: API key doesn't start with sk-proj-; please verify it's correct")
        return api_key
    else:
        print("API key found and looks good!")
        return api_key


def demonstrate_stateless_conversation() -> None:
    """Demonstrate how LLM conversation memory works.
    
    Shows that:
    1. Each LLM call is stateless
    2. Memory is simulated by passing entire conversation history
    3. Without conversation history, the LLM has no context
    """
    api_key = validate_api_key()
    if not api_key:
        return
    
    client = OpenAI()
    
    print("\n=== Demonstrating Stateless Conversation ===\n")
    
    # First message - introduce ourselves
    print("1. First call - introducing ourselves:")
    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hi! I'm Steven!"}
    ]
    response = client.chat.completions.create(model="gpt-4.1-mini", messages=messages)
    print(f"Response: {response.choices[0].message.content}\n")
    
    # Second call WITHOUT conversation history - LLM doesn't remember
    print("2. Second call WITHOUT history - asking our name:")
    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "What's my name?"}
    ]
    response = client.chat.completions.create(model="gpt-4.1-mini", messages=messages)
    print(f"Response: {response.choices[0].message.content}\n")
    
    # Third call WITH conversation history - now it "remembers"
    # Well its not really "remembering"". I am providing the COMPLETE
    # CONVERSATION BACK. Note that the assistent role represents the
    # the response from the agent.  
    print("3. Third call WITH history - now it remembers:")
    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hi! I'm Steven!"},
        {"role": "assistant", "content": "Hi Steven! How can I assist you today?"},
        {"role": "user", "content": "What's my name?"}
    ]
    response = client.chat.completions.create(model="gpt-4.1-mini", messages=messages)
    print(f"Response: {response.choices[0].message.content}\n")
    
    print("=== Key Takeaway ===")
    print("Every LLM call is stateless. 'Memory' is created by passing the")
    print("entire conversation history with each request.")


def main() -> None:
    """Main function demonstrating conversation memory."""
    demonstrate_stateless_conversation()


if __name__ == "__main__":
    main()


