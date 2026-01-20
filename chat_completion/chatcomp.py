# Auto-Generated
# File Name: chatcomp.py 
# Author: scotton
# Creation Date: January-20-2026
# Modified Date: January-20-2026

import os
import requests
import json
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

payload = {
    "model": "gpt-5-nano",
    "messages": [
        {"role": "user", "content": "Tell me a fun fact"}]
}

print("=" * 60)
print("🚀 Sending request to OpenAI API...")
print("=" * 60)
print(f"\n📦 Payload:")
print(json.dumps(payload, indent=2))
print("\n" + "=" * 60)
print("⏳ Waiting for response...")
print("=" * 60 + "\n")

response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers=headers,
    json=payload
)

print("✅ Response received!\n")
print("=" * 60)
print("📄 API Response:")
print("=" * 60)
print(json.dumps(response.json(), indent=2))
print("\n" + "=" * 60)


