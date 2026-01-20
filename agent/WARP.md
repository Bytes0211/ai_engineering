# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview
AI Web Summarizer Agent - A Python application that uses OpenAI's API to scrape and summarize website content with customizable AI personalities and prompts. The project consists of three core modules: `agent.py` (AI orchestration), `scraper.py` (web content extraction), and `example.py` (usage demonstrations).

## Development Commands

### Environment Setup
```bash
# This project uses uv for dependency management
# Install dependencies (uv will handle virtual environment)
uv sync

# Environment configuration
# Create .env file with: OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
```

### Running the Application
```bash
# Run example demonstrations
uv run ./example.py

# Or with python
uv run python example.py
```

### Testing
```bash
# Run all unit tests
uv run python -m unittest test_agent.py -v

# Run specific test class
uv run python -m unittest test_agent.TestLanguageFeature -v

# Run single test
uv run python -m unittest test_agent.TestLanguageFeature.test_language_persists_after_role_change -v
```

Tests cover:
- Agent initialization with default and custom parameters
- Language support and dynamic language switching
- Prompt customization (role, system prompt, user prompt)
- Message building for OpenAI API
- Summarization integration with mocked dependencies

## Architecture

### Core Components
- **Agent class** (`agent.py`): Manages OpenAI API interactions, prompt construction, and summarization orchestration
  - Initializes with OpenAI client using environment variables
  - Maintains configurable system and user prompts
  - Coordinates between Scraper and OpenAI API
  - Default model: `gpt-4.1-mini`

- **Scraper class** (`scraper.py`): Handles HTTP requests and HTML parsing
  - Uses BeautifulSoup for content extraction
  - Strips navigation elements (scripts, styles, images, inputs)
  - Truncates content to 2,000 characters for API efficiency
  - Sets User-Agent header to simulate browser requests

- **Example script** (`example.py`): Demonstrates various agent configurations and usage patterns

### Key Design Patterns
- **Composition**: Agent class composes Scraper rather than inheriting
- **Template method**: Prompt construction uses configurable templates with role/prefix customization
- **Message builder pattern**: `messages_for()` constructs OpenAI API message format

### Data Flow
1. User calls `agent.summarize(url)`
2. Agent delegates to `scraper.fetch_website_contents(url)`
3. Scraper fetches HTML, parses with BeautifulSoup, extracts text (truncated to 2K chars)
4. Agent builds message array with system prompt + user prompt + website content
5. Agent sends to OpenAI API (`chat.completions.create`)
6. Returns markdown summary from API response

## Important Constraints

### Content Limitations
- Website content is hard-truncated at 2,000 characters in `scraper.py:51`
- JavaScript-rendered sites (React, Vue, Angular) will not work - basic HTTP requests only
- CloudFront-protected sites may return 403 errors

### API Configuration
- OpenAI API key must be in `.env` file (loaded with `load_dotenv(override=True)`)
- Default model is `gpt-4.1-mini` but can be overridden in `summarize()` call
- No retry logic or error handling for API failures

### Prompt Customization
- Use `set_role()` to modify the default "snarky, humorous" tone while keeping structure
- Use `set_language()` to change response language (default: English)
- Use `set_system_prompt()` for complete system prompt replacement
- Use `set_user_prompt_prefix()` to change analysis instructions
- Default behavior: short, snarky summaries in markdown (not wrapped in code blocks)
- Language setting persists when changing roles

## Code Style Conventions
- Docstrings use Google style format with Args/Returns/Raises sections
- File headers include: filename, author (scotton), creation/modified dates
- Class attributes documented in docstrings
- Truncation uses underscore separators (e.g., `2_000`)
- Environment variables loaded with `override=True` to ensure fresh values
