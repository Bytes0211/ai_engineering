"""brochure.py

Company brochure generator using LLMs to analyze website content.

This module creates professional brochures for companies by:
1. Fetching website content and extracting relevant links
2. Using GPT to identify which links are most relevant for a brochure
3. Generating a markdown brochure from the aggregated content

Based on week1/day5.ipynb from AI Engineering course.

Author: scotton
Created: 2026-01-21
"""

import os
import json
import sys
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Add parent directory to path to import scraper from src/
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from scraper import Scraper


LINK_SYSTEM_PROMPT = """
You are provided with a list of links found on a webpage.
You are able to decide which of the links would be most relevant to include in a brochure about the company,
such as links to an About page, or a Company page, or Careers/Jobs pages.
You should respond in JSON as in this example:

{
    "links": [
        {"type": "about page", "url": "https://full.url/goes/here/about"},
        {"type": "careers page", "url": "https://another.full.url/careers"}
    ]
}
"""

BROCHURE_SYSTEM_PROMPT = """
You are an assistant that analyzes the contents of several relevant pages from a company website
and creates a short brochure about the company for prospective customers, investors and recruits.
Respond in markdown without code blocks.
Include details of company culture, customers and careers/jobs if you have the information.
"""


class BrochureGenerator:
    """Generates company brochures using LLM analysis of website content.
    
    This class orchestrates the process of fetching website content, identifying
    relevant pages, and generating a professional brochure using OpenAI's API.
    
    Attributes:
        client (OpenAI): Initialized OpenAI API client
        scraper (Scraper): Web scraping utility for content extraction
        link_selection_model (str): Model for link relevance analysis
        brochure_model (str): Model for brochure generation
    """
    
    def __init__(
        self,
        api_key: str | None = None,
        link_selection_model: str = "gpt-5-nano",
        brochure_model: str = "gpt-4.1-mini"
    ):
        """Initialize the BrochureGenerator.
        
        Args:
            api_key: OpenAI API key. If None, loads from environment
            link_selection_model: Model to use for link selection (default: gpt-5-nano)
            brochure_model: Model to use for brochure generation (default: gpt-4.1-mini)
            
        Raises:
            ValueError: If API key is not provided and not in environment
        """
        if api_key is None:
            load_dotenv(override=True)
            api_key = os.getenv("OPENAI_API_KEY")
        
        if not api_key:
            raise ValueError(
                "OpenAI API key not found. Please set OPENAI_API_KEY environment "
                "variable or pass api_key parameter."
            )
        
        self.client = OpenAI(api_key=api_key)
        self.scraper = Scraper()
        self.link_selection_model = link_selection_model
        self.brochure_model = brochure_model
    
    def _get_links_user_prompt(self, url: str) -> str:
        """Build user prompt for link selection.
        
        Args:
            url: The company website URL
            
        Returns:
            User prompt containing the list of links from the website
        """
        user_prompt = f"""
Here is the list of links on the website {url} -
Please decide which of these are relevant web links for a brochure about the company, 
respond with the full https URL in JSON format.
Do not include Terms of Service, Privacy, email links.

Links (some might be relative links):

"""
        links = self.scraper.fetch_website_links(url)
        user_prompt += "\n".join(links)
        return user_prompt
    
    def select_relevant_links(self, url: str) -> dict:
        """Select relevant links from a company website using LLM.
        
        Args:
            url: The company website URL
            
        Returns:
            Dictionary with 'links' key containing list of relevant link objects
            Each link object has 'type' and 'url' keys
        """
        print(f"Selecting relevant links for {url} by calling {self.link_selection_model}")
        response = self.client.chat.completions.create(
            model=self.link_selection_model,
            messages=[
                {"role": "system", "content": LINK_SYSTEM_PROMPT},
                {"role": "user", "content": self._get_links_user_prompt(url)}
            ],
            response_format={"type": "json_object"}
        )
        result = response.choices[0].message.content
        links = json.loads(result)
        print(f"Found {len(links.get('links', []))} relevant links")
        return links
    
    def fetch_page_and_all_relevant_links(self, url: str) -> str:
        """Fetch landing page content and all relevant linked pages.
        
        Args:
            url: The company website URL
            
        Returns:
            Formatted string containing landing page and all relevant pages content
        """
        contents = self.scraper.fetch_website_contents(url)
        relevant_links = self.select_relevant_links(url)
        result = f"## Landing Page:\n\n{contents}\n## Relevant Links:\n"
        for link in relevant_links.get("links", []):
            result += f"\n\n### Link: {link['type']}\n"
            try:
                result += self.scraper.fetch_website_contents(link["url"])
            except Exception as e:
                result += f"Error fetching content: {str(e)}"
        return result
    
    def _get_brochure_user_prompt(self, company_name: str, url: str) -> str:
        """Build user prompt for brochure generation.
        
        Args:
            company_name: Name of the company
            url: The company website URL
            
        Returns:
            User prompt containing company info and website content
        """
        user_prompt = f"""
You are looking at a company called: {company_name}
Here are the contents of its landing page and other relevant pages;
use this information to build a short brochure of the company in markdown without code blocks.\n\n
"""
        user_prompt += self.fetch_page_and_all_relevant_links(url)
        user_prompt = user_prompt[:5_000]  # Truncate if more than 5,000 characters
        return user_prompt
    
    def create_brochure(self, company_name: str, url: str) -> str:
        """Generate a company brochure.
        
        Args:
            company_name: Name of the company
            url: The company website URL
            
        Returns:
            Markdown-formatted brochure content
        """
        response = self.client.chat.completions.create(
            model=self.brochure_model,
            messages=[
                {"role": "system", "content": BROCHURE_SYSTEM_PROMPT},
                {"role": "user", "content": self._get_brochure_user_prompt(company_name, url)}
            ],
        )
        return response.choices[0].message.content
    
    def stream_brochure(self, company_name: str, url: str):
        """Generate and stream a company brochure with real-time output.
        
        Args:
            company_name: Name of the company
            url: The company website URL
            
        Yields:
            str: Chunks of the generated brochure as they arrive
        """
        stream = self.client.chat.completions.create(
            model=self.brochure_model,
            messages=[
                {"role": "system", "content": BROCHURE_SYSTEM_PROMPT},
                {"role": "user", "content": self._get_brochure_user_prompt(company_name, url)}
            ],
            stream=True
        )
        
        for chunk in stream:
            content = chunk.choices[0].delta.content or ""
            if content:
                yield content


def main():
    """Interactive brochure generator with user prompts."""
    print("=" * 60)
    print("Company Brochure Generator")
    print("=" * 60)
    print()
    
    # Get company name
    company_name = input("Enter the company name: ").strip()
    if not company_name:
        print("Error: Company name cannot be empty.")
        sys.exit(1)
    
    # Get website URL
    url = input("Enter the company website URL: ").strip()
    if not url:
        print("Error: URL cannot be empty.")
        sys.exit(1)
    
    # Ask if user wants streaming output
    stream_choice = input("Stream output in real-time? (y/n) [n]: ").strip().lower()
    use_streaming = stream_choice in ['y', 'yes']
    
    print()
    print("Generating brochure...")
    print()
    
    try:
        generator = BrochureGenerator()
        
        if use_streaming:
            print(f"# Brochure for {company_name}\n")
            for chunk in generator.stream_brochure(company_name, url):
                print(chunk, end="", flush=True)
            print()  # Final newline
        else:
            brochure = generator.create_brochure(company_name, url)
            print(f"# Brochure for {company_name}\n")
            print(brochure)
    except KeyboardInterrupt:
        print("\n\nBrochure generation cancelled.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError generating brochure: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
