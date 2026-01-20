# Auto-Generated
# File Name: openai_chatcomp.py 
# Author: scotton
# Creation Date: January-20-2026
# Modified Date: January-20-2026

# Create OpenAI client

import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI()

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

response = openai.chat.completions.create(model="gpt-5-nano", messages=[{"role": "user", "content": "Tell me a fun fact"}])

print("✅ Response received!\n")
print("=" * 60)
print("📄 API Response:")
print("=" * 60)
print(json.dumps(response.model_dump(), indent=2))
print("\n" + "=" * 60)
