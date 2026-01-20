# Warp AI Agent Rules for AI Engineering Project

## Project Context

This is an AI/LLM engineering learning project that converts Jupyter notebook tutorials from `/home/scotton/dev/notes/llm/` into production Python code. The project is structured as weekly modules with daily exercises, progressively building AI engineering skills.

## Code Structure and Organization

### Directory Structure
- **Weekly Modules**: `week{N}/` - Contains all code for that week
- **Daily Exercises**: `week{N}/day{N}/` - Specific day's implementations
- **Shared Utilities**: `shared/` - Common code used across modules
- **No Notebooks**: All code must be in `.py` files, never `.ipynb`

### File Naming Conventions
- Use snake_case for all Python files: `web_summarizer.py`, `model_comparison.py`
- Module names should be descriptive of their function
- Test files: `test_{module_name}.py`

### Code Organization
```python
# Standard structure for modules:
# 1. Docstring at top
# 2. Imports (standard lib, third-party, local)
# 3. Constants
# 4. Functions/Classes
# 5. Main execution block (if applicable)
```

## Dependencies and Environment

### Package Management
- Use `uv` for dependency management (preferred)
- Fallback to `pip` if needed
- All dependencies must be declared in `pyproject.toml`
- Pin versions for reproducibility

### Environment Variables
- Store all API keys in `.env` file
- Never commit `.env` to version control
- Use `python-dotenv` for loading environment variables
- Validate required keys at runtime

### Required Libraries
Common dependencies for this project:
- `openai` - OpenAI API client (also used for compatible APIs)
- `anthropic` - Anthropic Claude API
- `google-generativeai` - Google Gemini API  
- `python-dotenv` - Environment variable management
- `requests` - HTTP client
- `beautifulsoup4` - Web scraping (if needed)
- `litellm` - Multi-provider LLM abstraction (optional)
- `langchain-openai` - LangChain integration (optional)

## Coding Standards

### Style Guide
- Follow PEP 8 Python style guide
- Use type hints for function arguments and return values
- Maximum line length: 100 characters
- Use descriptive variable names (no single letters except in loops)

### Documentation
- Every module must have a docstring explaining its purpose
- Every function/class must have a docstring
- Use Google-style docstrings format:
```python
def summarize_website(url: str, model: str = "gpt-4.1-mini") -> str:
    """Summarize the content of a website using an LLM.
    
    Args:
        url: The URL of the website to summarize
        model: The model to use for summarization (default: gpt-4.1-mini)
        
    Returns:
        A string containing the summary of the website content
        
    Raises:
        ValueError: If URL is invalid or inaccessible
    """
```

### Error Handling
- Always validate API keys before making calls
- Provide helpful error messages for missing configuration
- Handle network errors gracefully
- Log errors appropriately

### Best Practices
- Keep functions small and focused (single responsibility)
- Avoid global variables
- Use configuration objects or dataclasses for complex settings
- Separate business logic from API calls
- Write testable code

## Tutorial Conversion Guidelines

### From Notebook to Python
When converting code from `/home/scotton/dev/notes/llm/*.ipynb`:

1. **Extract Code Cells**: Convert executable code cells to functions
2. **Remove Display Code**: Remove `display()`, `Markdown()` - use `print()` or return values
3. **Add Error Handling**: Notebooks assume success; production code needs error handling
4. **Modularize**: Break large cells into logical functions
5. **Add CLI**: Consider adding `argparse` for command-line usage
6. **Configuration**: Extract hardcoded values to constants or config

### Example Transformation
```python
# Notebook cell:
# response = openai.chat.completions.create(model="gpt-4.1-mini", messages=messages)
# display(Markdown(response.choices[0].message.content))

# Production code:
def get_completion(
    client: OpenAI, 
    messages: list[dict], 
    model: str = "gpt-4.1-mini"
) -> str:
    """Get a chat completion from OpenAI API.
    
    Args:
        client: Initialized OpenAI client
        messages: List of message dictionaries
        model: Model name to use
        
    Returns:
        The completion text
    """
    try:
        response = client.chat.completions.create(
            model=model, 
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"Failed to get completion: {e}")
        raise
```

## API and LLM Specific Rules

### API Key Management
- Load keys using `dotenv.load_dotenv()`
- Check for required keys at module initialization
- Provide clear error messages for missing keys

### Model Selection
- Default to cost-effective models for development:
  - OpenAI: `gpt-4.1-mini` or `gpt-5-nano`
  - Anthropic: `claude-3-5-haiku-latest`
  - Google: `gemini-2.5-flash-lite`
  - Local: `llama3.2` via Ollama

### Cost Optimization
- Use smaller models for testing
- Implement prompt caching where available
- Consider local models (Ollama) for development
- Track token usage in production code

### Multi-Provider Support
- Use OpenAI-compatible clients where possible
- Abstract provider-specific code
- Make provider selection configurable

## Testing

### Test Structure
- Create `tests/` directory at project root
- Mirror the project structure in tests
- Use `pytest` as test framework

### What to Test
- API client initialization
- Message formatting
- Error handling
- Configuration validation
- (Mock API calls in tests to avoid costs)

## Git Workflow

### Commit Messages
- Use conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`
- Be descriptive: "Add web summarizer for week 1 day 1"
- Reference tutorial source: "Based on week1/day1.ipynb"

### Branching
- `main` - stable code only
- `week{N}` - working branches for each week
- `feature/{name}` - for experimental features

### What to Commit
- All `.py` source files
- `README.md`, `WARP.md`, documentation
- `pyproject.toml`, `requirements.txt`
- `.gitignore`

### What NOT to Commit
- `.env` files (API keys)
- `__pycache__/` directories
- `.venv/` virtual environment
- Jupyter notebook outputs
- Large data files
- API response logs with sensitive data

## Development Workflow

### Adding New Week/Day Module
1. Create directory: `week{N}/day{N}/`
2. Review tutorial: `/home/scotton/dev/notes/llm/week{N}/day{N}.ipynb`
3. Plan the structure (what functions/classes needed)
4. Implement core functionality
5. Add error handling and logging
6. Write docstrings
7. Test manually
8. Update README with progress
9. Commit with clear message

### Code Review Checklist
- [ ] No hardcoded API keys
- [ ] All functions have type hints
- [ ] All functions have docstrings
- [ ] Error handling implemented
- [ ] No notebook-specific code (display, Markdown)
- [ ] Follows project structure
- [ ] Updated documentation

## Special Considerations

### Ollama Integration
- Check if Ollama is running before making requests
- Provide helpful message if not running
- Default to `llama3.2` for compatibility
- Consider `llama3.2:1b` for smaller machines

### Prompt Engineering
- Keep prompts in constants or configuration
- Make prompts easily modifiable
- Document prompt variations
- Version significant prompt changes

### Conversation History
- Use list of message dictionaries format
- Preserve conversation context appropriately
- Be mindful of context window limits
- Implement truncation if needed

## Debugging and Troubleshooting

### Common Issues
1. **Missing API Key**: Check `.env` file, reload with `load_dotenv(override=True)`
2. **Import Errors**: Verify virtual environment activated and dependencies installed
3. **Ollama Not Running**: Run `ollama serve` in terminal
4. **Rate Limits**: Implement retry logic with exponential backoff

### Logging
- Use Python `logging` module
- Set appropriate log levels
- Include context in log messages
- Don't log sensitive information (API keys, responses with PII)

## Additional Notes

- This project is for learning; prioritize understanding over perfection
- Experiment with variations and improvements
- Document learnings and insights
- Share interesting findings
- Keep production readiness in mind throughout

## References
- Tutorial source: `/home/scotton/dev/notes/llm/`
- Project structure inspired by production Python best practices
- API documentation: See README.md Resources section
