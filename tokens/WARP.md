# Warp AI Rules for Tokens Project

## Project Context
This module is part of Week 1, Day 4 of the AI Engineering learning project. It demonstrates two core concepts:
1. **Tokenization**: How text is converted into tokens for LLM processing
2. **Stateless Conversations**: How LLM "memory" is an illusion created by passing conversation history

Based on: `/home/scotton/dev/notes/llm/week1/day4.ipynb`

## What This Project Teaches

### Tokenization
- LLMs don't work with text directly; they work with tokens
- Different words/phrases are broken into different numbers of tokens
- Token count directly affects API costs
- Use `tiktoken` to see how your prompts will be tokenized

### Conversation Memory
- Each LLM API call is completely stateless
- There is NO built-in memory between calls
- "Memory" is simulated by sending the entire conversation history with each request
- This is exactly how ChatGPT works behind the scenes
- Each call costs more as the conversation grows (you pay for all previous tokens)

## Module Structure

### tokens.py
Tokenization functionality (no API key required):
- `get_encoding_for_model()` - Get tiktoken encoding for a model
- `encode_text()` - Convert text to token IDs
- `decode_tokens()` - Convert token IDs back to text
- `print_tokens_breakdown()` - Display each token and its text

### memory_illusion.py
Conversation memory demonstration (requires OpenAI API key):
- `validate_api_key()` - Check OpenAI API key configuration
- `demonstrate_stateless_conversation()` - Show how conversation memory works

### test_tokens.py
Unit tests for tokenization (no API calls):
- Tokenization roundtrip tests
- Encoding and decoding tests
- Token breakdown tests

### test_memory_illusion.py
Unit tests for conversation memory with mocked API calls:
- API key validation tests
- Conversation demonstration tests
- Message structure validation

## Usage

### Tokenization Demo (No API Key)
```bash
# Run tokenization demo
uv run python tokens.py

# Use directly in Python
uv run python -c "from tokens import print_tokens_breakdown; print_tokens_breakdown('Your text here')"
```

### Memory Illusion Demo (Requires OpenAI API Key)
```bash
# Run conversation memory demonstration
uv run python memory_illusion.py
```

### Run Tests
```bash
# Run all tests
uv run python -m unittest discover -v

# Run tokenization tests only
uv run python -m unittest test_tokens.py -v

# Run memory illusion tests only
uv run python -m unittest test_memory_illusion.py -v
```

## Key Learnings from Day 4

### Why Tokenization Matters
1. **Cost Management**: Tokens = money. Understanding tokenization helps estimate costs
2. **Context Limits**: Models have token limits (e.g., 8K, 128K tokens). Need to count tokens to stay within limits
3. **Prompt Engineering**: Knowing how text tokenizes helps write efficient prompts

### The Memory Illusion
```python
# This doesn't work - LLM has no context
messages = [
    {"role": "user", "content": "Hi! I'm Ed!"}
]
# ... make API call ...

messages = [
    {"role": "user", "content": "What's my name?"}  # LLM doesn't know!
]

# This works - we provide the context
messages = [
    {"role": "user", "content": "Hi! I'm Ed!"},
    {"role": "assistant", "content": "Hi Ed!"},
    {"role": "user", "content": "What's my name?"}  # Now it "knows"
]
```

### Practical Implications
1. **Conversation cost grows**: Each turn costs more as history accumulates
2. **Context management**: Need strategies to truncate or summarize old messages
3. **Stateless design**: Every request must be self-contained
4. **Token budgeting**: Balance between context and cost

## Dependencies
- `tiktoken` - OpenAI's tokenization library
- `openai` - OpenAI API client
- `python-dotenv` - Environment variable management

## Environment Setup
Create a `.env` file with:
```
OPENAI_API_KEY=sk-proj-your-key-here
```

## Notes for Development
- Tokenization works offline (no API key needed)
- Conversation demo requires valid OpenAI API key
- Tests use mocking to avoid API costs
- Different models use different encodings
- Token counts can vary between model families

## Related Concepts
- **Token limits**: gpt-4.1-mini supports up to 128K tokens
- **Prompt caching**: Some providers cache prompts to reduce costs
- **Context window**: The total tokens (input + output) a model can process
- **Token efficiency**: Shorter prompts = lower costs and faster responses

## Future Enhancements
- Add token counting for conversations
- Implement conversation truncation strategies
- Compare tokenization across different model families
- Add cost estimation based on token counts
- Visualize token boundaries in text
