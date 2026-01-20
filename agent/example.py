#!/usr/bin/env python3
"""
Example usage of the AI Web Summarizer Agent.

This script demonstrates various ways to use the Agent class
to summarize websites with different roles and configurations.
"""

from agent import Agent


def basic_example():
    """Basic usage with default settings."""
    print("=" * 60)
    print("Basic Example - Default Assistant")
    print("=" * 60)
    
    agent = Agent("WebSummarizer")
    summary = agent.summarize("https://example.com")
    print(summary)
    print()


def rapper_example():
    """Using the agent with a rapper personality."""
    print("=" * 60)
    print("Rapper Role Example")
    print("=" * 60)
    
    agent = Agent("WebSummarizer", role="assistant who also is a rapper")
    summary = agent.summarize("https://example.com")
    print(summary)
    print()


def analyst_example():
    """Using the agent as a professional analyst."""
    print("=" * 60)
    print("Professional Analyst Example")
    print("=" * 60)
    
    agent = Agent("WebSummarizer")
    
    # Customize with a professional tone
    agent.set_system_prompt("""
You are a professional business analyst who summarizes websites
in a formal, concise manner. Focus on key business metrics, value propositions,
and target audiences. Respond in markdown format.
""")
    
    agent.set_user_prompt_prefix("""
Analyze the following website content and provide:
1. Main purpose of the website
2. Key features or offerings
3. Target audience
4. Business model (if apparent)

Website content:
""")
    
    summary = agent.summarize("https://example.com")
    print(summary)
    print()


def custom_role_example():
    """Dynamically changing roles."""
    print("=" * 60)
    print("Dynamic Role Change Example")
    print("=" * 60)
    
    agent = Agent("WebSummarizer")
    
    # Start with comedian role
    agent.set_role("comedian")
    print("As a comedian:")
    print("-" * 60)
    summary = agent.summarize("https://example.com")
    print(summary)
    print()
    
    # Change to pirate role
    agent.set_role("pirate")
    print("As a pirate:")
    print("-" * 60)
    summary = agent.summarize("https://example.com")
    print(summary)
    print()


if __name__ == "__main__":
    print("\n")
    print("╔════════════════════════════════════════════════════════╗")
    print("║      AI Web Summarizer Agent - Usage Examples          ║")
    print("╚════════════════════════════════════════════════════════╝")
    print()
    
    # Run examples
    try:
        basic_example()
        # Uncomment to run other examples:
        # rapper_example()
        # analyst_example()
        # custom_role_example()
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure you have:")
        print("1. Created a .env file with your OPENAI_API_KEY")
        print("2. Installed dependencies: pip install -r requirements.txt")
