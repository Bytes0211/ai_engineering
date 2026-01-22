# WARP.md - Brochure Module

This file provides guidance to WARP (warp.dev) when working with the brochure module.

## Project Overview

Company Brochure Generator - An AI-powered tool that generates professional company brochures by analyzing website content using LLMs. Converts Week 1 Day 5 tutorial from Jupyter notebook into production Python code.

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
# Run using the installed command
uv run brochure "CompanyName" "https://example.com"

# With streaming output
uv run brochure "CompanyName" "https://example.com" --stream

# Or run directly with python
uv run python brochure.py "CompanyName" "https://example.com"

# Run examples
uv run python example.py
```

### Testing
```bash
# Run all unit tests
uv run python -m unittest test_brochure.py -v

# Run specific test class
uv run python -m unittest test_brochure.TestBrochureGeneration -v

# Run single test
uv run python -m unittest test_brochure.TestBrochureGeneration.test_create_brochure -v
```

Tests cover:
- BrochureGenerator initialization with valid/invalid API keys
- Link selection prompt generation and processing
- Content aggregation from multiple pages
- Brochure generation with mocked dependencies
- Streaming brochure generation
- Error handling

## Architecture

### Core Components
- **BrochureGenerator class** (`brochure.py`): Orchestrates brochure generation
  - Initializes with OpenAI client using environment variables
  - Uses dual-model strategy: gpt-5-nano for link selection, gpt-4.1-mini for brochure generation
  - Coordinates between Scraper and OpenAI API
  - Supports both standard and streaming output

- **Scraper class** (`../src/scraper.py`): Handles HTTP requests and HTML parsing
  - Shared utility imported from the src/ directory
  - Uses BeautifulSoup for content extraction
  - Truncates content to 2,000 characters per page

### Key Design Patterns
- **Composition**: BrochureGenerator composes Scraper rather than inheriting
- **Two-stage LLM pipeline**: First stage selects relevant links, second stage generates brochure
- **JSON structured outputs**: Link selection uses response_format for reliable parsing
- **Streaming support**: Generator pattern for real-time output

### Data Flow
1. User calls `generator.create_brochure(company_name, url)`
2. Generator fetches all links from landing page via Scraper
3. Generator uses GPT-5-nano to select relevant links (About, Careers, etc.)
4. Generator fetches content from landing page + selected links
5. Generator builds user prompt with aggregated content (truncated to 5K chars)
6. Generator sends to GPT-4.1-mini for brochure creation
7. Returns markdown brochure

## Important Constraints

### Content Limitations
- Landing page content truncated at 2,000 characters (Scraper limitation)
- Each linked page truncated at 2,000 characters
- Total brochure prompt truncated at 5,000 characters
- JavaScript-rendered sites will not work - basic HTTP requests only
- CloudFront-protected sites may return 403 errors

### API Configuration
- OpenAI API key must be in `.env` file (loaded with `load_dotenv(override=True)`)
- Default link selection model: `gpt-5-nano` (fast, cheap)
- Default brochure model: `gpt-4.1-mini` (better quality)
- Both models are configurable at initialization
- No retry logic or error handling for API failures

### Dependencies
- **Critical**: Must have access to `../src/scraper.py`
- Uses `sys.path.insert()` to import from src directory
- All dependencies managed via `uv` in `pyproject.toml`

## Code Style Conventions

- Docstrings use Google style format with Args/Returns/Raises sections
- File headers include: filename, author (scotton), creation date, description
- Class attributes documented in docstrings
- Type hints for all function arguments and return values
- Constants use UPPER_SNAKE_CASE (LINK_SYSTEM_PROMPT, BROCHURE_SYSTEM_PROMPT)
- Environment variables loaded with `override=True` to ensure fresh values

## Testing Approach

- All tests use mocks to avoid real API calls
- Mock dependencies before importing module (`sys.modules` mocking)
- Patch paths target `brochure.brochure.ClassName` (not `brochure.ClassName`)
- Tests verify both behavior and API call structure
- Error cases are tested (network failures, missing API keys)

## Prompt Engineering

### Link Selection Prompt
- Uses one-shot prompting with JSON example
- Instructs model to identify brochure-relevant links
- Excludes privacy/TOS links
- Returns structured JSON with type and URL

### Brochure Generation Prompt
- Focuses on prospective customers, investors, and recruits
- Requests markdown output (no code blocks)
- Emphasizes company culture, customers, and careers
- Can be customized for different tones (humorous, formal, etc.)

## Git Commit Convention

Use conventional commit format: `type(scope): brief description`

### Commit Types
- **feat**: New feature or functionality
- **fix**: Bug fix
- **docs**: Documentation changes
- **refactor**: Code refactoring without functionality change
- **test**: Adding or updating tests
- **chore**: Maintenance tasks (dependencies, config, infrastructure)

### Project Scopes
- **brochure**: Brochure generation logic
- **llm**: LLM integration general
- **openai**: OpenAI API integration
- **scraper**: Web scraping functionality
- **prompt**: Prompt engineering
- **test**: Test suite updates

### Guidelines
- Keep first line under 72 characters
- Use imperative mood ("add" not "added")
- Always include: `Co-Authored-By: Warp <agent@warp.dev>`
- Reference tutorial source: `feat(brochure): add streaming support based on day5.ipynb`

## Additional Notes

- This module demonstrates agentic AI patterns (multi-stage LLM workflow)
- Content generation is a common LLM use case applicable to any business vertical
- Emphasizes production readiness: error handling, testing, CLI interface
- Based on: `/home/scotton/dev/notes/llm/week1/day5.ipynb`
