# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

The **prompt_generator** module is an interactive CLI tool for generating structured LLM prompts for various business communication scenarios with direct API integration. It provides a user-friendly interface to select from pre-configured prompt templates, choose an LLM model (GPT-4.1 Mini or Claude 3.5 Haiku), and receive markdown-formatted responses via OpenRouter API.

This is a standalone utility within the larger AI Engineering learning project at `/home/scotton/dev/projects/ai_engineering/`.

## Core Architecture

### Three-Layer Structure

1. **Template Storage** (`prompt_templates.json`)
   - Single source of truth for all prompt configurations
   - JSON structure with 10+ pre-configured templates covering business domains
   - Each template includes: `id`, `name`, `description`, `default_content`, `system_prompt`, `developer_prompt`, `user_prompt_template`
   - The `user_prompt_template` uses `{content}` placeholder for dynamic substitution

2. **Interactive CLI** (`prompt_generator.py`)
   - Main entry point for the application
   - Implements menu-driven workflow: display templates → select model → collect content → send to API → display response
   - Handles multi-line input (user presses Enter twice to finish)
   - Graceful keyboard interrupt handling throughout
   - Integrates with OpenRouter API for multi-model LLM access
   - Dependencies: `requests`, `python-dotenv`

3. **Reference File** (`example_content.md`)
   - Example content for each template organized by template name
   - NOT used by the running application - kept as reference/documentation
   - Provides sample inputs demonstrating what each template handles

### Message Format

Prompts are built using a three-role pattern:
```json
[
  {"role": "system", "content": "High-level persona and instructions"},
  {"role": "developer", "content": "Constraints and behavioral guidelines + markdown output instruction"},
  {"role": "user", "content": "Actual user request with dynamic content"}
]
```

The `send_to_openrouter()` function automatically combines system and developer roles into a single system message for API compatibility.

### Model Selection

Supported models via OpenRouter:
- `openai/gpt-4.1-mini` - GPT-4.1 Mini
- `anthropic/claude-3-5-haiku-latest` - Claude 3.5 Haiku

## Common Development Tasks

### Setup

```bash
# Install dependencies
uv sync

# Create .env file from example
cp .env.example .env

# Add your OpenRouter API key to .env
# OPENROUTER_API_KEY=your_actual_api_key_here
```

### Running the Tool

```bash
# Standard execution
uv run python prompt_generator.py

# Direct Python (if venv activated)
python prompt_generator.py
```

### Testing Changes to Templates

1. Edit `prompt_templates.json` directly
2. Run `uv run python prompt_generator.py`
3. Select the modified template by number
4. Verify the generated JSON output

### Adding New Template

Add to `prompt_templates.json`:
```json
{
  "id": 11,
  "name": "Template Name",
  "description": "One-line description shown in menu",
  "default_content": "Example content users can test with",
  "system_prompt": "High-level instructions for LLM persona",
  "developer_prompt": "Constraints on tone, format, behavior",
  "user_prompt_template": "Request with {content} placeholder"
}
```

The `id` must be unique and sequential. No code changes needed - templates are loaded dynamically.

### Validating Template JSON

```bash
# Quick validation
python -m json.tool prompt_templates.json > /dev/null

# Pretty-print to check formatting
python -m json.tool prompt_templates.json
```

### Running Tests

```bash
# Run all tests
uv run python -m unittest test_prompt_generator.py -v

# Run specific test class
uv run python -m unittest test_prompt_generator.TestPromptGenerator -v

# Run specific test method
uv run python -m unittest test_prompt_generator.TestPromptGenerator.test_load_templates -v
```

## Dependencies and Environment

**Required Dependencies**:
- `requests` - For making HTTP requests to OpenRouter API
- `python-dotenv` - For loading environment variables from .env file

**Environment Variables**:
- `OPENROUTER_API_KEY` - API key for OpenRouter (required)
- Stored in `.env` file (never commit to version control)
- Use `.env.example` as template

The project uses `uv` for dependency management (inherited from parent project).

## Code Patterns

### Error Handling

The codebase follows defensive error handling:
- File operations: Explicit checks with `Path.exists()` before loading
- User input: Try-except blocks with helpful error messages
- Keyboard interrupts: Caught at every input point with graceful exit messages
- JSON parsing: Specific `json.JSONDecodeError` handling

### User Input Pattern

Multi-line input uses empty line counting:
```python
empty_line_count = 0
while True:
    line = input()
    if line == "":
        empty_line_count += 1
        if empty_line_count >= 2:
            break
    else:
        empty_line_count = 0
    lines.append(line)
```

This allows natural content entry including single blank lines within content.

### Template Selection

Uses `next()` with generator expression for efficient lookup:
```python
selected_template = next(
    (p for p in templates["prompts"] if p["id"] == selected_id),
    None
)
```

## File Relationships

- `prompt_generator.py` reads from `prompt_templates.json` (hardcoded relative path)
- `prompt_generator.py` loads `.env` file for API key using python-dotenv
- Both must be in the same directory for the tool to work
- `test_prompt_generator.py` tests the prompt generator functions
- `example_content.md` is standalone - not read by any code (reference only)
- `.env.example` provides template for environment variables
- No generated files or state persistence

## Integration Points

**OpenRouter API Integration**:
- The tool directly integrates with OpenRouter API
- Supports multiple LLM providers through a single endpoint
- API endpoint: `https://openrouter.ai/api/v1/chat/completions`
- Authentication via Bearer token in Authorization header
- Automatic conversion of developer role to system role for compatibility

**Response Format**:
- All templates configured to output markdown format
- Makes responses more readable in terminal
- Easy to copy and use in documentation

## Parent Project Context

This module follows conventions from `/home/scotton/dev/projects/ai_engineering/`:
- Uses `uv` for package management
- Follows PEP 8 style with type hints
- Google-style docstrings for all functions
- Maximum 100 character line length
- Module docstring at top of `prompt_generator.py`
- Test file named `test_{module_name}.py` pattern
- Environment variables stored in `.env` file
- API key management using python-dotenv
