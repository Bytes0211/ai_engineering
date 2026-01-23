# Company Brochure Generator

An AI-powered tool that generates professional company brochures by analyzing website content using LLMs.

Based on Week 1, Day 5 tutorial from AI Engineering course.

## Overview

This module creates comprehensive company brochures by:
1. Fetching the landing page and extracting all links
2. Using GPT to intelligently select relevant links (About, Careers, etc.)
3. Aggregating content from selected pages
4. Generating a markdown brochure suitable for prospective customers, investors, and recruits

## Features

- **Smart Link Selection**: Uses GPT-5-nano to identify relevant company pages
- **Content Aggregation**: Fetches and combines content from multiple pages
- **Professional Output**: Generates markdown brochures with company culture, customers, and career information
- **Streaming Support**: Option to stream brochure generation in real-time
- **Configurable Models**: Choose different models for link selection and brochure generation
- **CLI Interface**: Command-line tool for easy usage

## Installation

This project uses `uv` for dependency management.

```bash
# Navigate to the brochure directory
cd ~/dev/projects/ai_engineering/brochure

# Install dependencies using uv
uv sync

# Or install in development mode
uv pip install -e .
```

## Configuration

Set your OpenAI API key in `.env` file:

```bash
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
```

## Usage

### Command Line

```bash
# Run directly with python
uv run python brochure.py "HuggingFace" "https://huggingface.co"

# With streaming output
uv run python brochure.py "HuggingFace" "https://huggingface.co" --stream
```

### Python API

```python
from brochure.brochure import BrochureGenerator

# Initialize generator
generator = BrochureGenerator()

# Generate brochure
brochure = generator.create_brochure("HuggingFace", "https://huggingface.co")
print(brochure)

# Or stream the output
for chunk in generator.stream_brochure("HuggingFace", "https://huggingface.co"):
    print(chunk, end="", flush=True)
```

### Custom Models

```python
# Use different models
generator = BrochureGenerator(
    link_selection_model="gpt-4.1-mini",  # For link selection
    brochure_model="gpt-5-nano"           # For brochure generation
)
```

## Architecture

### Components

- **BrochureGenerator**: Main class orchestrating the brochure generation process
- **Scraper**: Web scraping utility (from ../src/) for extracting content and links
- **OpenAI Client**: Handles LLM API calls for link selection and content generation

### Process Flow

1. **Link Discovery**: Fetch all links from company landing page
2. **Link Selection**: GPT analyzes links and identifies relevant pages (About, Careers, etc.)
3. **Content Aggregation**: Fetch content from landing page and selected links
4. **Brochure Generation**: GPT creates a professional brochure from aggregated content

### Prompt Engineering

The module uses two specialized prompts:

1. **Link Selection Prompt**: Instructs the model to identify brochure-relevant links and return structured JSON
2. **Brochure Prompt**: Guides the model to create a professional brochure with specific sections

## Testing

Run the test suite:

```bash
# Run all tests
uv run python -m unittest test_brochure.py -v

# Run specific test class
uv run python -m unittest test_brochure.TestBrochureGeneration -v

# Run single test
uv run python -m unittest test_brochure.TestBrochureGeneration.test_create_brochure -v
```

Tests cover:
- Initialization with various API key configurations
- Link selection prompt generation and processing
- Content aggregation from multiple pages
- Brochure generation and streaming
- Error handling

## Limitations

- Inherits Scraper limitations (2,000 character truncation per page)
- Cannot handle JavaScript-rendered content
- Brochure prompt truncated at 5,000 characters total
- Requires working internet connection
- Subject to OpenAI API rate limits and costs

## Cost Optimization

- Default uses `gpt-5-nano` for link selection (faster, cheaper)
- Default uses `gpt-4.1-mini` for brochure generation (better quality)
- Content is truncated to manage token usage
- Consider local models (Ollama) for development/testing

## Examples

### Example Output

```markdown
# HuggingFace

HuggingFace is the leading platform for machine learning collaboration...

## Company Overview
...

## Products & Services
...

## Company Culture
...

## Career Opportunities
...
```

## Dependencies

- `openai`: OpenAI API client
- `python-dotenv`: Environment variable management
- `beautifulsoup4`: HTML parsing
- `requests`: HTTP requests
- `scraper`: Web scraping utility (from ../src/)

## Related Modules

- `agent/`: Web summarization agent (Week 1, Days 1-4)
- `week1/`: Other Week 1 exercises

## References

- Tutorial source: `~/dev/notes/llm/week1/day5.ipynb`
- OpenAI API: https://platform.openai.com/docs/api-reference
- Course resources: https://edwarddonner.com/2024/11/13/llm-engineering-resources/
