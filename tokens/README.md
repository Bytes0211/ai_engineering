# Tokenization and Conversation Memory

Two separate modules demonstrating core LLM concepts:
1. **tokens.py** - How LLMs process text through tokenization
2. **memory_illusion.py** - How conversation "memory" actually works

## Overview

This project explores two fundamental concepts in LLM engineering:

1. **Tokenization**: How text is broken into tokens that LLMs can process
2. **Stateless Conversations**: How the illusion of memory is created in chat applications

Based on Week 1, Day 4 of the AI Engineering curriculum.

## What You'll Learn

### Tokenization Basics

- LLMs don't process text directly - they work with numerical tokens
- A token is roughly 4 characters or ¾ of a word in English
- Token counts determine both API costs and context limits
- Different models may tokenize text differently

**Example:**
```
Text: "Hi my name is Ed and I like banoffee pie"
Tokens: [13347, 856, 836, 374, 3279, 323, 358, 1093, 9120, 1885, 68, 4447]
Token Count: 12
```

### The Memory Illusion

A critical insight for LLM developers:

- **Every API call is completely stateless** - there's no memory between requests
- Chat applications simulate memory by sending the entire conversation history with each request
- This is exactly how ChatGPT works under the hood
- As conversations grow, costs increase (you pay for all previous tokens each time)

## Installation

### Prerequisites
- Python 3.12+
- `uv` package manager

### Setup

```bash
# Install dependencies
uv sync

# Create .env file for API key (optional, only needed for conversation demo)
echo "OPENAI_API_KEY=sk-proj-your-key-here" > .env
```

## Usage

### Tokenization Demo (No API Key Required)

```bash
# Run tokenization demonstration
uv run python tokens.py
```

This will:
1. Show how text is tokenized
2. Display token IDs and their text representations
3. Demonstrate encoding/decoding

### Conversation Memory Demo (Requires OpenAI API Key)

```bash
# Run conversation memory demonstration
uv run python memory_illusion.py
```

This will:
1. Make three API calls to demonstrate stateless behavior
2. Show how LLMs don't remember without conversation history
3. Show how including history creates the illusion of memory

### Tokenization Only (No API Key Needed)

```python
from tokens import print_tokens_breakdown, encode_text, decode_tokens

# See how text is tokenized
print_tokens_breakdown("Hello, world!")

# Get token IDs
tokens = encode_text("Your text here")
print(f"Token count: {len(tokens)}")

# Decode tokens back to text
original = decode_tokens(tokens)
```

### Run Tests

```bash
# Run all tests (both modules)
uv run python -m unittest discover -v

# Run tokenization tests only (no API calls)
uv run python -m unittest test_tokens.py -v

# Run memory illusion tests only (mocked API calls)
uv run python -m unittest test_memory_illusion.py -v
```

## Code Examples

### Example 1: Count Tokens in Your Prompt

```python
from tokens import encode_text

prompt = "You are a helpful assistant. Please summarize this article..."
tokens = encode_text(prompt)
print(f"This prompt uses {len(tokens)} tokens")
```

### Example 2: Understanding Conversation Costs

```python
# First message: just the initial prompt
messages_1 = [
    {"role": "user", "content": "Hi! I'm Ed!"}
]
# Cost: ~5 tokens

# Second message: includes entire conversation history
messages_2 = [
    {"role": "user", "content": "Hi! I'm Ed!"},
    {"role": "assistant", "content": "Hi Ed! How can I help?"},
    {"role": "user", "content": "What's my name?"}
]
# Cost: ~20 tokens (includes all previous messages)
```

### Example 3: Why Memory Doesn't "Just Work"

```python
from openai import OpenAI

client = OpenAI()

# First call
messages = [{"role": "user", "content": "My name is Alice"}]
response = client.chat.completions.create(model="gpt-4.1-mini", messages=messages)

# Second call - LLM WON'T remember Alice!
messages = [{"role": "user", "content": "What's my name?"}]
response = client.chat.completions.create(model="gpt-4.1-mini", messages=messages)
# Response: "I don't know your name"

# To make it "remember", include the history:
# Well its not really "remembering"". I am providing the COMPLETE
# CONVERSATION BACK. Note that the assistent role represents the
# the response from the agent. 
messages = [
    {"role": "user", "content": "My name is Alice"},
    {"role": "assistant", "content": "Nice to meet you, Alice!"},
    {"role": "user", "content": "What's my name?"}
]
response = client.chat.completions.create(model="gpt-4.1-mini", messages=messages)
# Response: "Your name is Alice"
```

## Key Concepts

### Why This Matters

1. **Cost Management**: Every token costs money. Understanding tokenization helps estimate and control costs
2. **Context Limits**: Models have maximum token limits (e.g., 128K for gpt-4.1-mini). Token counting ensures you stay within limits
3. **Performance**: More tokens = slower responses. Efficient tokenization improves response times
4. **Conversation Design**: Understanding stateless calls helps design better conversation flows

### Token Economics

- Input tokens: Cost for tokens you send
- Output tokens: Cost for tokens the model generates (usually more expensive)
- As conversations grow, input token costs increase linearly
- Long conversations may need truncation or summarization strategies

### Practical Implications

- Chat applications must store conversation history client-side or server-side
- Each new message requires sending the entire conversation
- Token limits can be reached in long conversations
- Strategies needed: truncation, summarization, or context windowing

## Project Structure

```
tokens/
├── tokens.py              # Tokenization functions (no API key needed)
├── memory_illusion.py     # Conversation memory demo (requires API key)
├── test_tokens.py         # Tokenization tests (no API calls)
├── test_memory_illusion.py # Memory demo tests (mocked API calls)
├── README.md              # This file
├── WARP.md                # Project-specific AI agent rules
├── pyproject.toml         # Dependencies managed by uv
└── .env                   # API keys (not committed)
```

## Functions Reference

### tokens.py

**`get_encoding_for_model(model: str) -> tiktoken.Encoding`**
Get the tiktoken encoding for a specific model.

**`encode_text(text: str, model: str = "gpt-4.1-mini") -> list[int]`**
Encode text into a list of token IDs.

**`decode_tokens(tokens: list[int], model: str = "gpt-4.1-mini") -> str`**
Decode token IDs back into text.

**`print_tokens_breakdown(text: str, model: str = "gpt-4.1-mini") -> None`**
Print a detailed breakdown showing each token ID and its text.

### memory_illusion.py

**`validate_api_key() -> Optional[str]`**
Validate OpenAI API key configuration.

**`demonstrate_stateless_conversation() -> None`**
Interactive demonstration of how conversation memory works.

## Dependencies

- **tiktoken**: OpenAI's official tokenization library
- **openai**: OpenAI API client (for conversation demo)
- **python-dotenv**: Environment variable management

## Common Questions

**Q: Do I need an API key to use this?**
A: No for `tokens.py` (tokenization). Yes for `memory_illusion.py` (conversation demo).

**Q: Why do token counts matter?**
A: Token counts determine: (1) API costs, (2) whether you're within context limits, (3) response speed.

**Q: Can I use this with other LLM providers?**
A: Tokenization functions work with any model that uses tiktoken. For other providers, they may have different tokenization schemes.

**Q: How do I reduce token usage?**
A: Write concise prompts, truncate old messages, summarize context, or use smaller models.

**Q: What's a "good" number of tokens?**
A: Depends on your use case. Generally: keep prompts under 1000 tokens for cost-effectiveness, reserve space for output.

## Resources

- [OpenAI Tokenizer Tool](https://platform.openai.com/tokenizer) - Visual tokenization
- [tiktoken GitHub](https://github.com/openai/tiktoken) - Official library
- [OpenAI Pricing](https://openai.com/api/pricing/) - Token costs
- Tutorial Source: `/home/scotton/dev/notes/llm/week1/day4.ipynb`

## Learning Outcomes

After completing this module, you should understand:

- ✅ How text is converted to tokens
- ✅ Why token counts affect costs and limits
- ✅ That LLM calls are stateless
- ✅ How chat applications create the illusion of memory
- ✅ How to count and optimize token usage
- ✅ The trade-offs in conversation history management

## Next Steps

- Implement conversation truncation strategies
- Build a simple chatbot with persistent history
- Compare tokenization across different model families
- Add token-based cost estimation
- Experiment with context window optimization

## License

Educational project - part of AI Engineering curriculum.