# AI Web Summarizer Agent

An intelligent agent that uses OpenAI's API to fetch and summarize website content with customizable roles and prompts.

## Features

- **Web Scraping**: Extracts text content and links from websites using BeautifulSoup
- **AI-Powered Summarization**: Uses OpenAI's GPT models to generate concise, engaging summaries
- **Customizable Roles**: Configure the agent's personality (e.g., assistant, rapper, expert analyst)
- **Multi-Language Support**: Generate summaries in any language (default: English)
- **Flexible Prompts**: Customize both system and user prompts to fit your needs
- **Clean Output**: Returns markdown-formatted summaries ready for display

## Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Setup

1. Clone or navigate to this directory:
```bash
cd /home/scotton/dev/projects/agent
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```bash
OPENAI_API_KEY=your-api-key-here
```

## Running Tests

```bash
# Run all tests (using uv)
uv run python -m unittest test_agent.py -v

# Run specific test class
uv run python -m unittest test_agent.TestLanguageFeature -v

# Run single test
uv run python -m unittest test_agent.TestLanguageFeature.test_language_persists_after_role_change -v
```

## Usage

### Basic Example

```python
from agent import Agent

# Create an agent with default settings
agent = Agent("WebSummarizer")

# Summarize a website
summary = agent.summarize("https://example.com")
print(summary)
```

### Custom Role

```python
# Create an agent with a custom role
agent = Agent("WebSummarizer", role="expert analyst")

# Or change the role later
agent.set_role("rapper")

summary = agent.summarize("https://example.com")
print(summary)
```

### Multi-Language Support

```python
# Create an agent that responds in Spanish
agent = Agent("WebSummarizer", language="Spanish")
summary = agent.summarize("https://example.com")
print(summary)

# Change language dynamically
agent.set_language("French")
summary = agent.summarize("https://example.com")
print(summary)

# Combine custom role with language
agent = Agent("WebSummarizer", role="expert analyst", language="German")
summary = agent.summarize("https://example.com")
print(summary)
```

### Custom Prompts

```python
agent = Agent("WebSummarizer")

# Set a custom system prompt
agent.set_system_prompt("""
You are a professional business analyst who summarizes websites
in a formal, concise manner. Focus on key business metrics and value propositions.
""")

# Set a custom user prompt prefix
agent.set_user_prompt_prefix("""
Analyze the following website content and provide:
1. Main purpose of the website
2. Key features or offerings
3. Target audience

Website content:
""")

summary = agent.summarize("https://example.com")
print(summary)
```

### Using the Scraper Directly

```python
from scraper import Scraper

scraper = Scraper()

# Fetch website contents
content = scraper.fetch_website_contents("https://example.com")
print(content)

# Fetch all links from a website
links = scraper.fetch_website_links("https://example.com")
print(links)
```

## Project Structure

```
agent/
├── agent.py           # Main Agent class for AI-powered summarization
├── scraper.py         # Web scraping utilities
├── requirements.txt   # Python dependencies
├── .env              # Environment variables (create this)
├── .env.example      # Example environment variables
├── .gitignore        # Git ignore rules
└── README.md         # This file
```

## API Reference

### Agent Class

#### `__init__(self, name, role="assistant", language="English")`
Initialize the agent with a name, optional role, and language.

**Parameters:**
- `name` (str): The name of the agent
- `role` (str): The role description for the system prompt (default: "assistant")
- `language` (str): The language for responses (default: "English")

#### `set_role(self, role)`
Change the role used in the system prompt.

**Parameters:**
- `role` (str): The new role (e.g., "rapper", "expert analyst", "comedian")

#### `set_language(self, language)`
Change the language for responses.

**Parameters:**
- `language` (str): The language for responses (e.g., "English", "Spanish", "French", "German")

#### `set_system_prompt(self, prompt)`
Set a completely custom system prompt.

**Parameters:**
- `prompt` (str): The system prompt to use

#### `set_user_prompt_prefix(self, prefix)`
Set a custom user prompt prefix.

**Parameters:**
- `prefix` (str): The user prompt prefix

#### `summarize(self, url, model="gpt-4.1-mini")`
Fetch and summarize a website from a given URL.

**Parameters:**
- `url` (str): The URL of the website to summarize
- `model` (str): The OpenAI model to use (default: "gpt-4.1-mini")

**Returns:**
- `str`: The markdown-formatted summary

### Scraper Class

#### `fetch_website_contents(self, url)`
Fetch and extract textual content from a webpage.

**Parameters:**
- `url` (str): The URL of the webpage to fetch

**Returns:**
- `str`: The page title and body text (truncated to 2,000 characters)

#### `fetch_website_links(self, url)`
Fetch and extract all hyperlinks from a webpage.

**Parameters:**
- `url` (str): The URL of the webpage to fetch

**Returns:**
- `list[str]`: A list of all valid hyperlinks found on the page

## Limitations

- **JavaScript-rendered sites**: The scraper uses basic HTTP requests and cannot render JavaScript. Sites built with React, Vue, or Angular may not work properly.
- **Protected sites**: Websites protected by CloudFront or similar services may return 403 errors.
- **Content truncation**: Website content is truncated to 2,000 characters to stay within API limits.

## Environment Variables

Required environment variables in `.env`:

```
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
```

## Dependencies

- `beautifulsoup4`: HTML parsing and web scraping
- `requests`: HTTP requests
- `openai`: OpenAI API client
- `python-dotenv`: Environment variable management

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is for educational and personal use.

## Author

scotton  
Created: January 2026
