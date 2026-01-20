# Auto-Generated
# File Name: ollama_chatcomp.py.py 
# Author: scotton
# Creation Date: January-20-2026
# Modified Date: January-20-2026

import os
import json
import subprocess
from openai import OpenAI
from dotenv import load_dotenv

OLLAMA_BASE_URL = "http://localhost:11434/v1"

# Get list of available models from ollama
print("=" * 60)
print("🔍 Fetching available Ollama models...")
print("=" * 60 + "\n")

try:
    result = subprocess.run(['ollama', 'ls'], capture_output=True, text=True, check=True)
    output_lines = result.stdout.strip().split('\n')
    
    # Parse model names (first column after header)
    models = []
    for line in output_lines[1:]:  # Skip header
        if line.strip():
            model_name = line.split()[0]
            models.append(model_name)
    
    if not models:
        print("❌ No models found. Please pull a model using 'ollama pull <model_name>'")
        exit(1)
    
    print("Available models:\n")
    for idx, model in enumerate(models, 1):
        print(f"  {idx}. {model}")
    
    print("\n" + "=" * 60)
    
    # Get user selection
    while True:
        try:
            selection = input("\nSelect a model (enter number): ").strip()
            model_idx = int(selection) - 1
            if 0 <= model_idx < len(models):
                selected_model = models[model_idx]
                break
            else:
                print(f"Please enter a number between 1 and {len(models)}")
        except ValueError:
            print("Please enter a valid number")
        except KeyboardInterrupt:
            print("\n\n❌ Cancelled by user")
            exit(0)
    
    print(f"\n✅ Selected model: {selected_model}\n")
    
except subprocess.CalledProcessError:
    print("❌ Error running 'ollama ls'. Make sure Ollama is installed and running.")
    exit(1)
except FileNotFoundError:
    print("❌ Ollama command not found. Please install Ollama first.")
    exit(1)

# Initialize Ollama client
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')

payload = {
    "model": selected_model,
    "messages": [
        {"role": "user", "content": "Tell me a fun fact"}]
}

print("=" * 60)
print("🚀 Sending request to Ollama API...")
print("=" * 60)
print(f"\n📦 Payload:")
print(json.dumps(payload, indent=2))
print("\n" + "=" * 60)
print("⏳ Waiting for response...")
print("=" * 60 + "\n")

response = ollama.chat.completions.create(
    model=selected_model,
    messages=payload["messages"]
)

print("✅ Response received!\n")
print("=" * 60)
print("📄 API Response:")
print("=" * 60)

# Convert response to dict for pretty printing
response_dict = {
    "id": response.id,
    "object": response.object,
    "created": response.created,
    "model": response.model,
    "choices": [
        {
            "index": choice.index,
            "message": {
                "role": choice.message.role,
                "content": choice.message.content
            },
            "finish_reason": choice.finish_reason
        }
        for choice in response.choices
    ],
    "usage": {
        "prompt_tokens": response.usage.prompt_tokens,
        "completion_tokens": response.usage.completion_tokens,
        "total_tokens": response.usage.total_tokens
    } if response.usage else None
}

print(json.dumps(response_dict, indent=2))
print("\n" + "=" * 60)
