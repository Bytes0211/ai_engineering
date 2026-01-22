# Dev Notes

## Ollama

### 🧩 What Ollama Is  

Ollama is a **local LLM runtime** that lets you download, run, and manage large language models entirely on your machine. It provides:

- A lightweight **server** that runs models locally  
- A **CLI** for running, managing, and customizing models  
- A **Modelfile** system for building your own variants  
- An **HTTP API** for programmatic use  

It’s designed to make local LLMs as easy as running a Docker container.

### 🛠️ Core Ollama CLI Commands  

The CLI is the primary interface for interacting with Ollama. Here are the essential commands, with citations.

#### ▶️ Run Models  

- `ollama run <model>` — Run a model interactively or with a prompt  
- Supports multiline input, images, embeddings, and JSON output

#### ⬇️ Download / Manage Models  

- `ollama pull <model>` — Download a model from the registry  
- `ollama ls` or `ollama list` — List installed models  
- `ollama rm <model>` — Remove a model  
- `ollama show <model>` — Display model details

#### 🧱 Create or Modify Models  

- `ollama create -f Modelfile` — Build a custom model from a Modelfile  
- `ollama cp <src> <dest>` — Copy a model

#### 🖥️ Server & Process Management  

- `ollama serve` — Start the Ollama server (default port 11434)  
- `ollama ps` — List running models  
- `ollama stop <model>` — Stop a running model

#### 🔐 Authentication  

- `ollama signin` / `ollama signout` — Manage cloud authentication

---

### 🧭 Quick Summary Table

| Command | Purpose | Source |
|--------|---------|--------|
| `ollama run` | Run/chat with a model |  |
| `ollama pull` | Download a model |  |
| `ollama ls` / `list` | List installed models |  |
| `ollama rm` | Remove a model |  |
| `ollama create` | Build a model from a Modelfile |  |
| `ollama serve` | Start the Ollama server |  |
| `ollama ps` | List running models |  |
| `ollama stop` | Stop a running model |  |
| `ollama show` | Show model info |  |
| `ollama signin/signout` | Cloud auth |  |

## 💬 Chat Completions API — What Is It 

The **Chat Completions API** is an endpoint used to generate model responses in a **chat‑style format**, where the input is a list of messages and the output is a model‑generated message.  
OpenAI describes it as an API that “generates a model response from a list of messages comprising a conversation”.

Azure’s documentation reinforces that chat models are **optimized for conversational interfaces**, expecting input in a structured chat transcript format and returning a model‑written message.

DeepWiki adds that the Chat Completions API is the **message‑based interface** for text generation and supports streaming, tool calling, and structured outputs.

---
For more information see [course notes](course_notes.md)

Here is the core coponents of the code. For mre deatil review [chatcomp.py](./my_code/chat_completion/chatcomp.py)

```py
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
```

---

### 🧩 How It Works  

You send a request containing:

- A **model** (e.g., `gpt-4o`)
- A **messages array** (system/developer/user messages)
- Optional parameters (temperature, max tokens, top_p, etc.)

The API returns:

- A **completion** containing the model’s next message  
- Metadata (id, usage, finish_reason, etc.)

---
