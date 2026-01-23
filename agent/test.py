# Auto-Generated
# File Name: test.py 
# Author: scotton
# Creation Date: January-22-2026
# Modified Date: January-22-2026

import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display

# Add OpenRouter Key from .env file
load_dotenv(override=True)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Check if OpenRouter API Key is set
if OPENROUTER_API_KEY:
    print(f"OpenRouter API Key exists. First 10 chars: {OPENROUTER_API_KEY[:10]}")
else:
    print("OpenRouter API Key not set (and this is optional)")

# Create OpenAI client for OpenRouter
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=OPENROUTER_API_KEY,
)
response = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>",     # Optional. Site title for rankings on openrouter.ai.
  },
  # model="openai/gpt-5.2",
  model="openai/gpt-5.2",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
)
print(f"Model used: {response.model}")
reply = response.choices[0].message
print(f"Reply: {reply}")
