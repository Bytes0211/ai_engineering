# Prompt Generator

An interactive CLI tool for generating structured LLM prompts for various business communication scenarios with direct API integration.

## Overview

This tool provides a user-friendly interface to select from pre-configured prompt templates, choose an LLM model, and get responses directly from OpenRouter API. Supports GPT-4.1 Mini and Claude 3.5 Haiku with markdown-formatted output.

## Files

- `prompt_generator.py` - Interactive prompt generator CLI with OpenRouter API integration
- `prompt_templates.json` - Template definitions for all prompt types (markdown output enabled)
- `example_content.md` - Reference file with example content for each template
- `test_prompt_generator.py` - Unit tests for the prompt generator
- `.env.example` - Example environment variables file

## Features

- **10 Pre-configured Templates**: Business communication, customer support, data analysis, strategy, HR, marketing, documentation, engineering, compliance, and executive communication
- **Interactive Selection**: Browse and select from numbered menu
- **Model Selection**: Choose between GPT-4.1 Mini or Claude 3.5 Haiku
- **Flexible Input**: Use default content or provide your own
- **Multi-line Input**: Support for complex, multi-line content
- **OpenRouter API Integration**: Direct integration with OpenRouter for multi-model access
- **Markdown Output**: All responses formatted in markdown for easy reading
- **Error Handling**: Graceful handling of invalid inputs, interruptions, and API errors

## Available Prompt Templates

1. **Business Communication** - Rewrite messages into professional business language
2. **Customer Support & Service** - Draft empathetic customer support responses
3. **Data Analysis & Insights** - Translate data into actionable business insights
4. **Strategy, Planning & Decision Support** - Provide strategic analysis and recommendations
5. **HR, People, and Leadership** - Rewrite feedback and communications constructively
6. **Marketing, Sales & Customer Messaging** - Create compelling, benefits-focused messaging
7. **Documentation, SOPs & Knowledge Base** - Convert information into structured documentation
8. **Product, Engineering & Technical Work** - Translate technical content for mixed audiences
9. **Compliance, Risk & Governance** - Explain policies in plain language
10. **Executive-Level Communication** - Create concise, strategic summaries for leadership

## Setup

### Prerequisites

1. Python 3.12+
2. OpenRouter API key (get one at https://openrouter.ai/keys)

### Installation

```bash
# Install dependencies
uv sync

# Create .env file from example
cp .env.example .env

# Add your OpenRouter API key to .env
OPENROUTER_API_KEY=your_actual_api_key_here
```

## Usage

### Basic Usage

```bash
uv run python prompt_generator.py
```

### Interactive Flow

1. **Select a template**: Choose from the numbered menu (1-10)
2. **Select a model**: Choose GPT-4.1 Mini (1) or Claude 3.5 Haiku (2)
3. **Review default content**: See example content for the selected template
4. **Choose content source**:
   - Type `y` to use default content
   - Type `n` to enter your own content
5. **Enter content** (if custom):
   - Type or paste your content
   - Press Enter twice when finished
6. **Get response**: Receive markdown-formatted response from the LLM

### Example Session

```
======================================================================
Available Prompt Templates
======================================================================

 1. Business Communication
    Rewrite messages into professional business language

 2. Customer Support & Service
    Draft empathetic customer support responses

...

Select a prompt (1-10): 1

✓ Selected: Business Communication

Default content: Hey team, can we hurry up on the report? Its taking too long.

Use default content? (y/n) [n]: n

Enter your content (press Enter twice when done):
The project deadline needs to be pushed back again


======================================================================
Generated Prompt JSON
======================================================================

[
  {
    "role": "system",
    "content": "You are a professional business communication assistant..."
  },
  {
    "role": "developer",
    "content": "Always respond in a polished, professional tone..."
  },
  {
    "role": "user",
    "content": "Rewrite this message to be more professional: The project deadline needs to be pushed back again"
  }
]

You can copy the JSON above to use with your LLM API.
```

## Adding New Templates

Edit `prompt_templates.json` to add new templates:

```json
{
  "id": 11,
  "name": "Your Template Name",
  "description": "Brief description of what it does",
  "default_content": "Example content for users to see",
  "system_prompt": "System-level instructions for the LLM",
  "developer_prompt": "Developer-level constraints and guidelines",
  "user_prompt_template": "Template with {content} placeholder"
}
```

## Dependencies

- Python 3.12+
- `requests` - HTTP client for API requests
- `python-dotenv` - Environment variable management

## Supported Models

Via OpenRouter API:
- **GPT-4.1 Mini** (`openai/gpt-4.1-mini`) - Fast and cost-effective
- **Claude 3.5 Haiku** (`anthropic/claude-3-5-haiku-latest`) - Efficient and balanced

## Testing

```bash
# Run all tests
uv run python -m unittest test_prompt_generator.py -v

# Run specific test
uv run python -m unittest test_prompt_generator.TestPromptGenerator.test_load_templates -v
```

## Tips

- **Press Ctrl+C** anytime to exit gracefully
- **Use defaults** for quick testing and examples
- **Multi-line content** is fully supported - just press Enter twice when done
- **Markdown output** makes responses easy to read and copy
- **Customize templates** in `prompt_templates.json` for your specific needs
- **Switch models** to compare responses between GPT and Claude

## Related

- Based on AI Engineering course materials
- Similar to `brochure.py` interactive pattern
- Part of the ai_engineering project
