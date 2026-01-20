# File Name: agent.py 
# Author: scotton
# Creation Date: January-17-2026
# Modified Date: January-18-2026

import os
from dotenv import load_dotenv
from openai import OpenAI
from scraper import Scraper


class Agent:
    """
    An AI agent that can summarize websites using OpenAI's API.
    
    This class provides methods to create prompts, build messages, and
    interact with LLMs to analyze and summarize web content.
    
    Attributes:
        name (str): The name of the agent.
        language (str): The language for responses.
        openai (OpenAI): The OpenAI client instance.
        scraper (Scraper): The web scraper instance.
        system_prompt (str): The system prompt defining the agent's role.
        user_prompt_prefix (str): The prefix for user prompts.
    """

    def __init__(self, name, role="assistant", language="English"):
        """Initialize the Agent with a name, role, and language.
        
        Args:
            name (str): The name of the agent.
            role (str): The role description for the system prompt.
            language (str): The language for responses (default: "English").
        """
        self.name = name
        self.language = language
        
        # Load environment variables and initialize OpenAI client
        load_dotenv(override=True)
        self.openai = OpenAI()
        
        # Initialize the scraper
        self.scraper = Scraper()
        
        # Set default system prompt with customizable role and language
        self.system_prompt = f"""
You are an {role} that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
Respond in {language}.
"""
        
        # Set default user prompt prefix
        self.user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.
"""
    
    def set_system_prompt(self, prompt):
        """Set a custom system prompt.
        
        Args:
            prompt (str): The system prompt to use.
        """
        self.system_prompt = prompt
    
    def set_user_prompt_prefix(self, prefix):
        """Set a custom user prompt prefix.
        
        Args:
            prefix (str): The user prompt prefix to use.
        """
        self.user_prompt_prefix = prefix
    
    def set_role(self, role):
        """Change the role used in the system prompt.
        
        Args:
            role (str): The role description (e.g., "assistant", "rapper", "expert analyst").
        """
        self.system_prompt = f"""
You are an {role} that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
Respond in {self.language}.
"""
    
    def set_language(self, language):
        """Change the language for responses.
        
        Args:
            language (str): The language for responses (e.g., "English", "Spanish", "French").
        """
        self.language = language
        # Update system prompt to reflect new language
        current_role = "assistant"  # Extract current role if needed
        self.system_prompt = f"""
You are an {current_role} that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
Respond in {language}.
"""
    
    def messages_for(self, website_content):
        """Build the messages list for the OpenAI API.
        
        Args:
            website_content (str): The website content to analyze.
        
        Returns:
            list: A list of message dictionaries with role and content.
        """
        return [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": self.user_prompt_prefix + website_content}
        ]
    
    def summarize(self, url, model="gpt-4.1-mini"):
        """Fetch and summarize a website from a given URL.
        
        Args:
            url (str): The URL of the website to summarize.
            model (str): The OpenAI model to use (default: "gpt-4.1-mini").
        
        Returns:
            str: The summary of the website content.
        """
        # Fetch website contents
        website = self.scraper.fetch_website_contents(url)
        
        # Create messages
        messages = self.messages_for(website)
        
        # Call OpenAI API
        response = self.openai.chat.completions.create(
            model=model,
            messages=messages
        )
        
        return response.choices[0].message.content

