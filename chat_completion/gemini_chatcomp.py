# Auto-Generated
# File Name: gemini_chatcomp.py 
# Author: scotton
# Creation Date: January-20-2026
# Modified Date: January-20-2026

import os
import json
from openai import OpenAI
from dotenv import load_dotenv

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

load_dotenv(override=True)
google_api_key = os.getenv('GOOGLE_API_KEY')

gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)

payload = {
    "model": "gemini-2.5-flash-lite",
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

response = gemini.chat.completions.create(model="gemini-2.5-flash-lite", messages=[{"role": "user", "content": "Tell me a fun fact"}])

print("✅ Response received!\n")
print("=" * 60)
print("📄 API Response:")
print("=" * 60)
print(json.dumps(response.model_dump(), indent=2))
print("\n" + "=" * 60)

