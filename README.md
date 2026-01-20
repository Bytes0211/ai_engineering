# AI Engineering Project

A comprehensive AI/LLM engineering project based on hands-on tutorials, structured as a progressive learning journey with weekly modules and daily exercises.

## Overview

This project serves as a practical implementation companion to the LLM Engineering tutorial series located in `/home/scotton/dev/notes/llm/`. The tutorials are presented as Jupyter notebooks organized by week and day, and this project converts those concepts into production-ready Python code.

## Project Structure

```
ai_engineering/
├── week1/          # Week 1: Introduction to LLMs and APIs
│   ├── day1/       # First Frontier LLM project - web scraping and summarization
│   ├── day2/       # Chat Completions API and Ollama
│   ├── day4/       # Additional exercises
│   └── day5/       # Week 1 recap
├── week2/          # Week 2: Frontier Model APIs
│   ├── day1/       # Multiple LLM providers and prompt caching
│   ├── day2/       # Advanced API features
│   ├── day3/       # More exercises
│   ├── day4/       # Further development
│   └── day5/       # Week 2 recap
├── week3/          # Week 3: Advanced topics
├── week4/          # Week 4: Continued learning
├── week5/          # Week 5: Progressive modules
├── week6/          # Week 6: Advanced implementations
├── week7/          # Week 7: Further topics
├── week8/          # Week 8: Final modules
└── shared/         # Shared utilities and common code
```

## Key Learning Topics

### Week 1: Getting Started with LLMs
- **Day 1**: Building a web scraper with LLM summarization
  - OpenAI API integration
  - System and user prompts
  - Website content extraction
  
- **Day 2**: Understanding Chat Completions API
  - OpenAI-compatible endpoints
  - Working with Ollama (local models)
  - Gemini, DeepSeek integration

### Week 2: Frontier Model APIs
- **Day 1**: Multi-provider LLM integration
  - OpenAI, Anthropic, Google Gemini, DeepSeek, Groq, Grok
  - Prompt caching techniques
  - Cost optimization
  - Conversational AI with message history
  - LiteLLM and LangChain abstraction layers

### Week 3 and Beyond
- Advanced prompting techniques
- Fine-tuning and model customization
- Agentic AI systems
- Production deployment patterns

## Installation

### Prerequisites
- Python 3.12 or higher
- uv package manager (recommended) or pip
- Git for version control

### Setup
```bash
# Clone or navigate to the project
cd /home/scotton/dev/projects/ai_engineering

# Create virtual environment (if not already created)
python -m venv .venv
source .venv/bin/activate  # On Linux/Mac

# Install dependencies
uv pip install -r requirements.txt
# or if using pip:
# pip install -r requirements.txt
```

### Environment Variables
Create a `.env` file in the project root with your API keys:

```bash
# OpenAI
OPENAI_API_KEY=sk-proj-xxxxx

# Optional: Other providers
ANTHROPIC_API_KEY=sk-ant-xxxxx
GOOGLE_API_KEY=AIzxxxxx
DEEPSEEK_API_KEY=xxxxx
GROQ_API_KEY=xxxxx
GROK_API_KEY=xxxxx
OPENROUTER_API_KEY=xxxxx
```

## Usage

### Running Individual Modules
Each week/day module can be run independently:

```bash
# Example: Run week 1, day 1 exercises
python -m week1.day1.web_summarizer

# Example: Run week 2, day 1 multi-model comparison
python -m week2.day1.model_comparison
```

### Main Entry Point
```bash
python main.py
```

## Development Workflow

This project follows a structured learning approach:

1. **Review Tutorial**: Read the corresponding notebook in `/home/scotton/dev/notes/llm/week{N}/day{N}.ipynb`
2. **Understand Concepts**: Study the code examples and explanations
3. **Implement in Python**: Convert notebook code to production Python modules
4. **Extend and Experiment**: Add your own variations and improvements
5. **Document**: Keep notes of learnings and insights

## Design Principles

- **No Jupyter Notebooks**: All code is pure Python for production readiness
- **Modular Structure**: Each week/day is self-contained but can share utilities
- **Progressive Learning**: Build on previous lessons incrementally
- **Best Practices**: Follow Python conventions and clean code principles
- **Documentation**: Comprehensive docstrings and comments

## API Cost Management

### OpenAI
- Use `gpt-4.1-mini` or `gpt-5-nano` for cost-effective development
- Monitor usage at https://platform.openai.com/usage
- Set usage limits in your OpenAI account

### Free Alternatives
- **Ollama**: Run models locally (llama3.2, deepseek-r1:1.5b)
- **Groq**: Free tier for fast inference
- **Google Gemini**: Free tier available

## Contributing

This is a personal learning project, but contributions and suggestions are welcome:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request with clear descriptions

## Resources

- **Tutorial Source**: `/home/scotton/dev/notes/llm/`
- **Course Resources**: https://edwarddonner.com/2024/11/13/llm-engineering-resources/
- **OpenAI Docs**: https://platform.openai.com/docs
- **Anthropic Docs**: https://docs.anthropic.com
- **Google Gemini**: https://ai.google.dev
- **Ollama**: https://ollama.com

## License

This project is for educational purposes. Please respect the licensing of the original tutorial materials and API providers' terms of service.

## Acknowledgments

Tutorial series by Edward Donner and the LLM Engineering community. Special thanks to all contributors who share their implementations and improvements.

## Project Status

🚧 **In Development** - Progressive implementation following the tutorial series

### Completed
- [ ] Week 1, Day 1: Web summarizer
- [ ] Week 1, Day 2: Ollama integration
- [ ] Week 2, Day 1: Multi-provider APIs

### In Progress
- [ ] Converting tutorials to production code

### Planned
- [ ] All 8 weeks of tutorial content
- [ ] Additional custom projects
- [ ] Advanced agentic AI systems
