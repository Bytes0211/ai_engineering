# Course Notes

## Table of Contents

- [Agentic AI](#agentic-ai)
  - [What Agentic AI Means](#-what-agentic-ai-means)
  - [How Agentic AI Works](#-how-agentic-ai-works)
  - [Agentic AI vs. Generative AI](#-agentic-ai-vs-generative-ai)
  - [Real-World Examples](#️-real-world-examples)
  - [Why Agentic AI Matters](#-why-agentic-ai-matters)
- [AI Model Overview](#ai-model-overview)
  - [AI Model Taxonomy Hierarchy](#-ai-model-taxonomy-hierarchy)
  - [Frontier LLMs vs. Foundation LLMs](#-frontier-llms-vs-foundation-llms)
    - [What Are Foundation Models?](#-what-are-foundation-models)
    - [What Are Frontier Models?](#-what-are-frontier-models)
    - [The Core Difference](#-the-core-difference)
    - [Quick Comparison Table](#-quick-comparison-table)
    - [Foundation and Frontier Models](#-foundation-and-frontier-models)
  - [Reasoning Models vs. Agentic Models](#-reasoning-models-vs-agentic-models)
    - [Reasoning Models](#-reasoning-models)
    - [Agentic Models (or Agentic Systems)](#-agentic-models-or-agentic-systems)
    - [The Cleanest Distinction](#-the-cleanest-distinction)
    - [How They Relate](#-how-they-relate)
    - [Why People Confuse Them](#-why-people-confuse-them)
  - [Model Use Cases](#model-use-cases)
    - [1. Chat Interfaces](#-1-chat-interfaces)
    - [2. Cloud APIs](#️-2-cloud-apis)
    - [3. Direct Inference with Open-Source Models](#️-3-direct-inference-with-opensource-models)
    - [Additional Ways to Use Models (Often Overlooked)](#-additional-ways-to-use-models-often-overlooked)
  - [Model Usage Summary Table](#-model-usage-summary-table)
- [Chat Completions API — What Is It](#-chat-completions-api--what-is-it)
  - [How Chat Completions Work](#-how-chat-completions-work)
  - [Example Request (from Azure's documentation)](#-example-request-from-azures-documentation)
  - [Message Roles](#-message-roles)
  - [Key Features](#️-key-features)
  - [Endpoints (from DeepWiki)](#-endpoints-from-deepwiki)
  - [Chat Completions Summary Table](#-chat-completions-summary-table)
- [What a Transformer Is (in AI)](#-what-a-transformer-is-in-ai)
  - [Key Concepts Inside a Transformer](#-key-concepts-inside-a-transformer)
  - [Why Transformers Matter](#-why-transformers-matter)
  - [Transformer vs. Older Models](#-transformer-vs-older-models)
  - [Clean Mental Model](#-clean-mental-model-1)
- [Tokens (AI / Transformers)](#-tokens-ai--transformers)
  - [Why Tokens Exist](#-why-tokens-exist)
  - [Examples of Tokenization](#-examples-of-tokenization)
  - [How Tokens Fit Into Transformers](#-how-tokens-fit-into-transformers-from-your-previous-question)
  - [How Many Characters Is a Token?](#-how-many-characters-is-a-token)
  - [Clean Mental Model](#-clean-mental-model)
- [Parameters](#-parameters)
  - [What Parameters Look Like](#-what-parameters-look-like)
  - [Why Parameters Matter](#-why-parameters-matter)
  - [Simple Example](#-simple-example)
  - [Clean Mental Model](#-clean-mental-model-2)
- [Context Window](#context-window)
  - [What an AI Context Window Is](#-what-an-ai-context-window-is)
  - [What the Context Window Controls](#-what-the-context-window-controls)
  - [Why Context Window Matters in Practice](#-why-context-window-matters-in-practice)
  - [Clean Mental Model](#-clean-mental-model-3)
  - [Context Window Comparison Across Major Models](#-context-window-comparison-across-major-models)
  - [Which Models Handle Long Context Best?](#-which-models-handle-long-context-best)
- [What Internal Reasoning Tokens Are](#-what-internal-reasoning-tokens-are)
  - [Why They Exist](#-why-they-exist)
  - [How Internal Reasoning Tokens Flow Through the Model](#-how-internal-reasoning-tokens-flow-through-the-model)
  - [Where They Live in the Context Window](#️-where-they-live-in-the-context-window)
  - [They Enable Multi-Pass Thinking](#-they-enable-multi-pass-thinking)
  - [Why You Don't See Them](#-why-you-dont-see-them)
  - [Clean Mental Model](#-clean-mental-model-4)

## Agentic AI

Agentic AI is one of the most important shifts happening in AI right now, and the search results you triggered give a very clear foundation. I’ll synthesize them into a crisp, practical explanation you can use in engineering, architecture, or strategy discussions.

---

### 🤖 What *Agentic AI* Means  

Agentic AI refers to **AI systems that can plan, reason, and take actions autonomously**—not just generate content. Instead of waiting for a prompt and producing a single output, an agentic system can:

- Understand goals  
- Break them into steps  
- Choose tools or APIs  
- Execute actions  
- Reflect and improve  

IBM describes agentic AI as systems that “accomplish a specific goal with limited supervision” and exhibit autonomy, goal‑driven behavior, and adaptability.  
Google Cloud emphasizes that agentic AI can “set goals, plan, and execute tasks with minimal human intervention”.  
Microsoft (via the University of Cincinnati summary) defines it as AI that “plans, reasons and acts to complete tasks with minimal human oversight”.

---

### 🧩 How Agentic AI Works  

Across the sources, the core loop looks like this:

#### 1. **Perception**  

Gather information from text, sensors, APIs, databases, or user input.

#### 2. **Reasoning**  

Use an LLM to interpret context, constraints, and goals.

#### 3. **Planning**  

Break the goal into steps and choose a strategy.

#### 4. **Action**  

Call tools, APIs, or external systems to execute tasks.

#### 5. **Reflection**  

Evaluate results and adjust future actions.

This loop is what makes agentic systems feel “alive” compared to traditional prompt‑response models.

---

### 🆚 Agentic AI vs. Generative AI  

| Generative AI | Agentic AI |
|---------------|------------|
| Produces content (text, code, images) | Achieves goals through actions |
| Requires explicit prompts | Operates with autonomy and initiative |
| No memory of long‑term objectives | Maintains goals and multi‑step plans |
| Cannot act on the world | Can call tools, APIs, and systems |

Generative AI is *creative*.  
Agentic AI is *productive*.

---

### 🛠️ Real‑World Examples  

The search results highlight several concrete examples:

#### ✈️ Travel booking  

An agent can plan a trip, compare prices, and book flights/hotels automatically.

#### 📅 Scheduling  

Parse emails, find availability, and schedule meetings without human intervention.

#### 🧾 Document workflows  

Review, classify, or extract data and then take follow‑up actions (e.g., file, notify, escalate).

#### 🛒 E‑commerce automation  

Monitor inventory, adjust pricing, or trigger supply‑chain actions.

#### 🧑‍💼 Enterprise automation  

Multi‑step workflows like onboarding, approvals, or compliance checks.

---

### 🧠 Why Agentic AI Matters  

Agentic AI is the bridge between **LLMs** and **real automation**.

It enables systems that can:

- Work continuously toward goals  
- Handle ambiguity  
- Adapt to changing conditions  
- Integrate with enterprise systems  
- Reduce human supervision  

[ToC](#table-of-contents)

## AI Model Overview

### 🧬 AI Model Taxonomy Hierarchy

```txt
AI Ecosystem
│
├── 1. Narrow / Task‑Specific Models
│       ├── Spam Classifiers
│       ├── Sentiment Models
│       ├── Recommendation Models
│       └── Vision Classifiers
│
└── 2. Foundation Models  (Broad, General‑Purpose)
        │
        ├── 2.1 Base Foundation Models
        │       ├── BERT
        │       ├── CLIP
        │       ├── Stable Diffusion
        │       ├── Llama (base)
        │       ├── Mistral (base)
        │       ├── Qwen (base)
        │       └── Other Multimodal Base Models
        │
        ├── 2.2 Fine‑Tuned Foundation Models
        │       ├── Llama‑3/4‑Instruct (Open Source)
        │       ├── Mistral‑Instruct (Open Source)
        │       ├── Stable Diffusion XL Variants
        │       └── Domain‑Specific Tuned Models
        │
        ├── 2.3 Multimodal Models
        │       ├── Gemini (Google DeepMind)
        │       └── GPT‑4o (OpenAI)
        │
        ├── 2.4 Reasoning Models  (Specialized Subset)
        │       ├── OpenAI o1 / o3‑mini
        │       ├── DeepSeek‑R1
        │       ├── QwQ‑32B
        │       ├── Claude 3.7 Sonnet Thinking
        │       └── Gemini Flash Thinking
        │
        └── 2.5 Frontier Models  (Most Advanced Subset)
                ├── GPT‑4 / GPT‑4.1 Class [OpenAi]
                ├── Claude 3 (Opus, Sonnet, Haiku) [Anthropic]
                ├── Gemini Ultra [Google]
                ├── DeepSeek‑V3 / R1 [DeepSeek]
                └── xAI Grok‑2 [X.ai]


Agentic Systems  (Built *on top of* Foundation + Reasoning Models)
│
├── Workflow Agents
├── Research Agents
├── RAG Agents (Retrieval‑Augmented Agents)
├── Multi‑Agent Systems
├── Task‑Oriented Copilots
└── Autonomous Assistants

```

### 🧠 Frontier LLMs vs. Foundation LLMs  

The two terms sound similar, but they describe **different tiers of AI models**.

---

#### 🧩 What Are **Foundation Models**?

Foundation models are **large, general‑purpose models** trained on broad, diverse datasets and designed to be adapted to many downstream tasks.  
They include models like BERT, GPT‑3, CLIP, Llama, and Mistral base models.

Key characteristics from the search results:  

- Trained on **broad, massive datasets**  
- Serve as **base layers** for fine‑tuning or prompting  
- Can be multimodal (text, images, audio, video)  
- Represent the **core infrastructure** of modern AI systems

Think of them as the *trunk* of the AI tree — general, flexible, and adaptable.

---

#### 🚀 What Are **Frontier Models**?

Frontier models are a **subset of foundation models**, but at the *cutting edge* of capability.  
They represent the **most advanced, highest‑performing, next‑generation** models available.

Key characteristics from the search results:  

- Push the **boundaries of current AI capabilities**  
- Represent the **state‑of‑the‑art** in performance and safety research  
- Often developed by top “frontier labs” like OpenAI, Anthropic, Google DeepMind  
- Exceed the capabilities of existing advanced models

Examples include GPT‑4, Claude 3 Opus, Gemini Ultra — the models at the very top of the capability curve.

---

#### 🧭 The Core Difference  

**All frontier models are foundation models, but not all foundation models are frontier models.**
So frontier models are a subset of foundation models

This is supported directly by the sources:

- Foundation models = broad, general‑purpose base models  
- Frontier models = the **most advanced** models that surpass current capabilities  
- Taxonomy places frontier models as a **higher tier** above foundation models

---

#### 📊 Quick Comparison Table

| Feature | Foundation Models | Frontier Models |
|--------|-------------------|-----------------|
| Purpose | General‑purpose base models | Push the limits of AI capability |
| Scope | Broad, adaptable | Most advanced subset of foundation models |
| Examples | BERT, CLIP, Llama, Mistral | GPT‑4, Claude 3, Gemini Ultra |
| Training Data | Large, diverse datasets | Same, but with extreme scale and optimization |
| Role | Infrastructure for downstream tasks | Cutting‑edge research and top‑tier performance |
| Who Builds Them | Many labs (Meta, Mistral, etc.) | “Frontier labs” (OpenAI, Anthropic, Google DeepMind) |

#### 📊 Foundation and Frontier Models

##### 🧱 **Foundation Models**

These are large, general‑purpose models trained on broad data and adaptable to many downstream tasks.

| Model | Type | Open Source | Company / Lab |
|-------|------|-------------|----------------|
| **BERT** | Foundation | Yes | Google |
| **CLIP** | Foundation | Yes | OpenAI |
| **GPT-OSS** | Foundation | Yes | OpenAI |
| **GPT‑3** | Foundation | No | OpenAI |
| **Llama 2 / Llama 3** | Foundation LLM | Yes | Meta |
| **Mistral 7B / Mixtral** | Foundation LLM | Yes | Mistral AI |
| **Qwen - 2** | Foundation LLM | Yes | Alibaba Cloud |
| **Gemma** | Foundation LLM | Yes | Google |
| **Phi** | Foundation LLM | Yes | Microsoft |
| **DeepSeek** | Foundation LLM | Yes | DeepSeek AI |
| **Stable Diffusion** | Foundation (image) | Yes | Stability AI |
| **DALL‑E** | Foundation (image) | No | OpenAI |
| **Flamingo** | Foundation (vision‑language) | No | DeepMind |
| **MusicGen** | Foundation (audio) | Yes | Meta |
| **RT‑2** | Foundation (robotics) | No | Google DeepMind |

##### 🚀 **Frontier Models**

These are the **most advanced, cutting‑edge** models that exceed the capabilities of existing systems.

| Model | Type | Open Source | Company / Lab |
|-------|------|-------------|----------------|
| **GPT‑4 / GPT‑4.1 / GPT‑5‑class** | Frontier LLM | No | OpenAI |
| **Claude 3 (Opus, Sonnet, Haiku)** | Frontier LLM | No | Anthropic |
| **Gemini Ultra** | Frontier LLM | No | Google DeepMind |
| **DeepSeek‑V3 / DeepSeek‑R1** | Frontier LLM | Partially (R1‑Distill) | DeepSeek |
| **xAI Grok‑2** | Frontier LLM | Partially | xAI |
| **Frontier‑scale multimodal models** (e.g., Gemini Ultra Vision, GPT‑4o‑class) | Frontier | No | OpenAI / Google DeepMind |

---

### 🧠 **Reasoning Models vs. Agentic Models**

#### 🧩 **Reasoning Models**

A *reasoning model* is an LLM that has been optimized to think more deeply, follow multi‑step logic, and solve complex problems.

These models focus on:

- Chain‑of‑thought reasoning  
- Planning and decomposition  
- Math and logic  
- Long‑horizon problem solving  
- Self‑correction  

Examples:

- OpenAI o1 / o3‑mini  
- DeepSeek‑R1  
- QwQ‑32B  
- Gemini 2.0 Flash Thinking  
- Claude 3.7 Sonnet Thinking  

**Key idea:**  
A reasoning model is still *just a model*. It doesn’t act on the world by itself.

---

#### 🤖 **Agentic Models (or Agentic Systems)**

An *agentic model* is not a model at all — it’s a **system** built around a model.

Agentic systems add:

- Tool use  
- Memory  
- Planning loops  
- Environment interaction  
- Autonomy  
- Multi‑step execution  
- Error recovery  
- Goal‑directed behavior  

Examples:

- AI agents that book travel  
- Workflow‑executing copilots  
- Multi‑agent systems  
- Agentic RAG  
- Autonomous research agents  
- Assistants that call APIs, run code, browse, schedule, etc.

**Key idea:**  
Agentic systems use LLMs (often reasoning models) as the *brain*, but the agent is the whole machine — not the model.

---

#### 🧭 **The Cleanest Distinction**

| Concept | What It Is | What It Does |
|--------|-------------|---------------|
| **Reasoning Model** | A type of LLM | Thinks better |
| **Agentic Model/System** | A system built around an LLM | Acts, decides, uses tools |

---

#### 🔗 **How They Relate**

Reasoning models are **ingredients**.  
Agentic systems are **recipes**.

A reasoning model can power an agent, but it is **not** an agent by itself.

Think of it like this:

- A reasoning model is a brilliant mathematician.  
- An agent is a mathematician who also has a laptop, internet access, a calendar, and the ability to execute tasks.

---

#### 🧠 **Why People Confuse Them**

Modern reasoning models (like o1 or DeepSeek‑R1) *feel* more agent‑like because they:

- Plan  
- Reflect  
- Break tasks into steps  
- Produce structured tool calls  

But they still don’t act autonomously without an agent framework around them.

---

### Model Use Cases

The **three primary ways to use AI models**, plus **additional modes** that most teams overlook. I’ll keep it crisp but meaningful so you can plug this directly into architecture docs or onboarding materials.

---

#### 🧠 1. **Chat Interfaces**

These are conversational UIs where the model interacts with users in natural language.

##### What this means  

- A user types or speaks a prompt  
- The model responds conversationally  
- Often includes memory, context windows, and tool‑use  
- Usually hosted by a platform (Copilot, ChatGPT, Claude, Gemini, etc.)

##### Common Use Cases  

- Customer support assistants  
- Internal knowledge assistants  
- Coding copilots  
- Document Q&A  
- Brainstorming, writing, summarization  
- Agentic workflows (multi‑step reasoning + tool calls)

##### When to use  

- You need **human‑in‑the‑loop** interaction  
- You want rapid prototyping  
- You don’t want to manage infrastructure  
- You need a UI for non‑technical users  

---

### ☁️ 2. **Cloud APIs**

Models accessed programmatically through an API endpoint (e.g., Bedrock, OpenAI, Anthropic, Azure OpenAI, Google Vertex).

#### How Clouod APIs Work

- Your application sends a request to a cloud endpoint  
- The model returns text, embeddings, images, or structured output  
- You pay per token or per request  
- No infrastructure to manage

#### Cloud API Use Cases  

- RAG pipelines  
- Chatbots embedded in apps  
- Automated document processing  
- Code generation services  
- Workflow automation  
- Multimodal apps (vision, audio, video)

#### When to use Cloud APIs

- You need **scalability**  
- You want **enterprise‑grade reliability**  
- You need **high‑end frontier models**  
- You don’t want to host models yourself  

---

### 🖥️ 3. **Direct Inference with Open‑Source Models**

Running models locally or on your own servers using frameworks like **Ollama, Hugging Face, vLLM, llama.cpp, TensorRT‑LLM**, etc.

#### How Direct Inference Work

- You download the model weights  
- You run inference on your hardware (CPU/GPU)  
- You control performance, privacy, and cost  
- You can fine‑tune or quantize models

#### Direct Inference Common Use Cases  

- On‑prem or air‑gapped environments  
- Privacy‑sensitive workloads  
- Custom fine‑tuning  
- Edge devices (Jetson, mobile, embedded)  
- Cost‑optimized inference at scale  
- Hybrid RAG (local + cloud fallback)

#### When to use Direct Inference

- You need **full control**  
- You want **zero per‑token cost**  
- You need **offline or private inference**  
- You want to customize or extend the model  

---

### ➕ Additional Ways to Use Models (Often Overlooked)

#### 4. **Model Embeddings**

Using models to convert text, images, or documents into vector embeddings.

##### Model Embedding Use Cases  

- Semantic search  
- RAG retrieval  
- Clustering and classification  
- Recommendation systems  
- Similarity detection  
- Fraud detection  

---

#### 5. **Fine‑Tuning / Continued Training**

Training a model on domain‑specific data to improve performance.

##### Fine-Tuning / Continued Training Use Cases  

- Industry‑specific chatbots  
- Legal/medical assistants  
- Code‑base‑specific copilots  
- Product catalog enrichment  
- Custom reasoning tasks  

---

#### 6. **Agents and Tool‑Using Systems**

Models that can call APIs, run code, browse the web, or orchestrate workflows.

##### Agents and Tool-Using Systems Use Cases  

- Automated research  
- Multi‑step business processes  
- Travel booking  
- Scheduling  
- Data extraction + action  
- Enterprise automation  

---

#### 7. **Batch Processing Pipelines**

Running models over large datasets in bulk.

##### Batch Processsing Pipelines Use Cases  

- Document classification  
- Large‑scale summarization  
- Data labeling  
- Image/video analysis  
- ETL enrichment in data lakes  

---

#### 8. **Edge and Mobile Deployment**

Running small or quantized models on devices.

##### Edge and Mobile Depoyment Use Cases  

- On‑device assistants  
- Real‑time vision (drones, robotics)  
- Offline translation  
- Privacy‑preserving inference  

---

### 🧭 Model Usage Summary Table

| Method | Description | Best For |
|--------|-------------|----------|
| **Chat Interfaces** | Human‑facing conversational UI | Support, ideation, copilots |
| **Cloud APIs** | Programmatic access to hosted models | Scalable apps, RAG, automation |
| **Direct Inference (Open Source)** | Run models locally/on‑prem | Privacy, customization, cost control |
| **Embeddings** | Vector representations | Search, RAG, recommendations |
| **Fine‑Tuning** | Domain‑specific training | Specialized assistants |
| **Agents** | Models that act via tools | Automation, workflows |
| **Batch Processing** | Large‑scale offline inference | Document pipelines |
| **Edge Deployment** | On‑device inference | Robotics, mobile, offline apps |

---

[ToC](#table-of-contents)

## 💬 Chat Completions API — What Is It

Code can be found in the `/projects/ai_engineering/chat_completions/`

The **Chat Completions API** is an endpoint used to generate model responses in a **chat‑style format**, where the input is a list of messages and the output is a model‑generated message.

OpenAI describes it as an API that “generates a model response from a list of messages comprising a conversation”.

Azure’s documentation reinforces that chat models are **optimized for conversational interfaces**, expecting input in a structured chat transcript format and returning a model‑written message.

DeepWiki adds that the Chat Completions API is the **message‑based interface** for text generation and supports streaming, tool calling, and structured outputs.

---

### 🧩 How Chat Completions Work  

You send a request containing:

- A **model** (e.g., `gpt-4o`)
- A **messages array** (system/developer/user messages)
- Optional parameters (temperature, max tokens, top_p, etc.)

The API returns:

- A **completion** containing the model’s next message  
- Metadata (id, usage, finish_reason, etc.)

---

### 🧱 Example Request (from Azure’s documentation)

```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Assistant is a large language model."},
        {"role": "user", "content": "Who were the founders of Microsoft?"}
    ]
)
```

This example is directly aligned with Azure’s Chat Completions documentation.

---

### 🧭 Message Roles  

The API supports several message types:

- **developer** (replaces system messages for newer models)  
- **system** (instructions for older models)  
- **user** (human input)  
- **assistant** (model output)

---

### ⚙️ Key Features  

According to the search results:

#### ✔️ Multi‑turn conversation support  

The API is designed for chat‑style interactions where messages accumulate over time.

#### ✔️ Supports text, images, and audio (depending on model)  

The messages array can contain different content types for multimodal models.

#### ✔️ Streaming responses  

The API can stream partial outputs in real time.

#### ✔️ Tool calling / function execution  

The API supports structured tool calls for automation workflows.

#### ✔️ Structured outputs  

You can enforce JSON schemas or typed outputs using structured output features.

---

### 🧱 Endpoints (from DeepWiki)

The Chat Completions resource supports:

- `POST /chat/completions` — create a new completion  
- `GET /chat/completions/{id}` — retrieve a stored completion  
- `POST /chat/completions/{id}` — update metadata  
- `DELETE /chat/completions/{id}/messages` — delete messages  
- `GET /chat/completions` — list completions  

These endpoints are documented in the DeepWiki reference.

---

### 📊 Chat Completions Summary Table

| Feature | Description | Source |
|--------|-------------|--------|
| Purpose | Generate model responses from chat messages |  |
| Input Format | Array of messages with roles |  |
| Optimized For | Conversational interfaces |  |
| Supports | Text, images, audio (model‑dependent) |  |
| Advanced Features | Streaming, tool calling, structured outputs |  |
| Endpoints | Create, retrieve, update, list, delete |  |

---

[ToC](#table-of-contents)

## 🧠 **What a Transformer Is (in AI)**  

A **Transformer** is the neural‑network architecture that unlocked the modern AI era. If you think of today’s LLMs as skyscrapers, the Transformer is the steel frame that makes them possible.

A **Transformer** is a deep‑learning architecture designed to process sequences (like text, audio, or tokens) using a mechanism called **attention**.  
It was introduced in the 2017 paper *“Attention Is All You Need”* and replaced older sequence models like RNNs and LSTMs.

The core idea:

> Instead of reading text word‑by‑word in order, a Transformer looks at **all words at once** and learns which ones matter most.

This ability to model relationships across long distances in text is what makes Transformers so powerful.

---

### 🔍 **Key Concepts Inside a Transformer**

#### 1. **Self‑Attention**

The model learns how much each token should “pay attention” to every other token.

Example:  
In the sentence *“The cat that chased the mouse was hungry”*,  
the word **“was”** needs to attend to **“cat”**, not **“mouse”**.

Self‑attention lets the model figure that out automatically.

---

#### 2. **Multi‑Head Attention**

Instead of one attention pattern, the model learns many in parallel.

Each “head” focuses on something different:

- syntax  
- long‑range dependencies  
- semantic meaning  
- relationships between entities  

This is why Transformers understand context so well.

---

#### 3. **Positional Encoding**

Transformers don’t read text sequentially, so they need a way to know **order**.

Positional encodings give each token a sense of:

- position  
- distance  
- relative ordering  

---

#### 4. **Stacked Layers**

Transformers are built by stacking many layers of:

- attention  
- feed‑forward networks  
- normalization  

More layers → deeper reasoning and richer representations.

---

### 🚀 **Why Transformers Matter**

Transformers enabled:

- **Large Language Models (LLMs)**  
  GPT, Claude, Gemini, Llama, Mistral, Qwen

- **Multimodal models**  
  GPT‑4o, Gemini, CLIP, Flamingo

- **Diffusion models**  
  Stable Diffusion uses a Transformer backbone for text encoding

- **Speech models**  
  Whisper, AudioLM

Transformers are the foundation of nearly every frontier AI system today.

---

### 📊 **Transformer vs. Older Models**

| Model Type | Limitation | How Transformers Fix It |
|------------|------------|--------------------------|
| RNN | Slow, sequential | Parallel processing |
| LSTM | Struggles with long context | Global attention |
| CNN | Local patterns only | Long‑range relationships |
| Transformer | None of the above | Scales to billions of parameters |

Transformers scale beautifully — that’s why LLMs can grow to 70B, 400B, or even more parameters.

---

### 🧭 **Clean Mental Model**

A Transformer is like a room full of experts all reading the same sentence at once.  
Each expert focuses on a different relationship, and together they build a deep understanding of the text.

---

## 🧠 **Tokens (AI / Transformers)**  

A **token** is one of the smallest units of text that an AI model reads, processes, and predicts.  
If you imagine language as a stream of tiny building blocks, tokens are those blocks.

They’re not exactly words — they’re **pieces** of words.

A **token** is a chunk of text (or audio, or image embedding) that a model converts into a numerical representation so it can understand and generate language.

Depending on the model, a token might be:

- a whole word  
- part of a word  
- a punctuation mark  
- a space  
- a subword like “ing”, “pre”, “##tion”  
- an emoji  
- a special symbol (like `<start>` or `<end>`)

Transformers don’t operate on raw text — they operate on **tokens**, which are then turned into vectors.

---

### 🔍 **Why Tokens Exist**  

Models need a consistent way to break text into manageable pieces.  
Tokens solve this by:

- reducing vocabulary size  
- handling rare words  
- supporting multiple languages  
- making training efficient  
- enabling models to generalize better

This is why modern tokenizers use **subword units** (like Byte Pair Encoding or SentencePiece).

---

### 🧩 **Examples of Tokenization**

#### Example 1 — Simple English sentence  

Text:  

```txt
Transformers are amazing!
```

Possible tokens:  

```txt
["Transform", "ers", "are", "amazing", "!"]
```

#### Example 2 — Word with unusual spelling  

Text:  

```txt
uncharacteristically
```

Tokens might be:  

```txt
["un", "character", "istic", "ally"]
```

#### Example 3 — Emoji  

```txt
"🔥" → ["🔥"]
```

#### Example 4 — Spaces matter  

```
"hello" vs " hello"
```

These tokenize differently because leading spaces are part of the token.

---

### 🧠 **How Tokens Fit Into Transformers (from your previous question)**  

Transformers don’t read text directly.  
They read **token embeddings**.

The flow looks like this:

```txt
Text → Tokenizer → Tokens → Embeddings → Transformer Layers → Output Tokens → Text
```

Tokens are the bridge between human language and the model’s internal math.

---

### 📏 **How Many Characters Is a Token?**  

There’s no fixed size, but a common rule of thumb:

- **1 token ≈ 3–4 characters of English**
- **75 tokens ≈ 1 paragraph**
- **1,000 tokens ≈ 750 words**

This varies by language and tokenizer.

---

### 🧭 **Clean Mental Model**  

A token is like a Lego brick.  
Words are built from tokens.  
Sentences are built from words.  
Transformers operate on the bricks, not the finished structure.

---

[ToC](#table-of-contents)

## 🧠 Parameters  

In AI—especially in modern neural networks like Transformers—**parameters are the internal numerical values the model learns during training**. They’re the knobs, weights, and biases that determine how the model behaves, thinks, and responds.

A clean way to say it:

> **Parameters are the learned values inside a model that shape how it transforms input into output.**

They’re not rules written by humans.  
They’re patterns the model *discovers* from data.

Every parameter influences how strongly one piece of information affects another.

In a Transformer, parameters control things like:

- how much one token attends to another  
- how information flows through layers  
- how embeddings are transformed  
- how the model predicts the next token  

If you imagine the model as a giant mathematical machine, parameters are the dials that define its behavior.

---

### 🔢 What Parameters Look Like  

A parameter is just a number—usually a floating‑point value like:

```txt
0.1284
-0.0047
1.9321
```

A small model might have **millions** of these.  
Frontier models have **hundreds of billions**.

Each one is tiny and meaningless alone.  
Together, they encode the model’s entire “knowledge”.

---

### 🧩 Why Parameters Matter  

Parameters determine:

- how well the model understands language  
- how coherent its responses are  
- how much reasoning it can perform  
- how much context it can use  
- how well it generalizes to new tasks  

More parameters ≠ always better, but they do enable richer representations.

---

### 🧪 Simple Example  

Imagine a tiny neural network layer:

\[
\text{output} = W \cdot x + b
\]

- **W** (weights) = parameters  
- **b** (biases) = parameters  
- **x** = input  
- **output** = transformed representation  

During training, the model adjusts **W** and **b** to reduce error.

---

### 🧭 Clean Mental Model  

Think of parameters as:

- the **memory** of the model  
- the **knowledge** it has absorbed  
- the **settings** that define how it processes information  
- the **internal wiring** that shapes its intelligence  

They’re the reason a model can translate languages, write code, or solve math problems—without being explicitly programmed to do so.

---

## Context Window

The **AI context window** is one of the most important — and most misunderstood — concepts in modern language models. Once you grasp it, a lot of AI behavior suddenly makes sense.

---

### 🧠 **What an AI Context Window Is**

The **context window** is the maximum amount of information (tokens) an AI model can “hold in mind” at once while generating a response.

Think of it as the model’s **working memory**.

- It includes your prompt  
- plus any previous messages  
- plus the model’s own internal reasoning tokens  
- plus the output it generates  

All of that must fit inside the window.

If the window is 128k tokens, the model can only consider 128k tokens of text at a time. Anything beyond that gets **forgotten**, truncated, or summarized.

---

### 🔍 **What the Context Window Controls**

#### 1. **How much the model can remember in a conversation**

If you exceed the window, older messages fall out of memory.

#### 2. **How much text the model can analyze at once**

Large windows allow:

- long documents  
- multi‑file codebases  
- entire research papers  
- long transcripts  

#### 3. **How well the model maintains coherence**

Bigger windows → better long‑range reasoning.

#### 4. **How much reasoning the model can perform internally**

Reasoning models (like o1‑style systems) use many internal tokens.  
These also count toward the window.

---

### 🧩 **Why Context Window Matters in Practice**

#### **A. Long conversations**

If you chat for hours, older parts may fall out of the window unless the system summarizes them.

#### **B. Document analysis**

If you upload a 200‑page PDF to a model with a 32k window, it can’t read it all at once.

#### **C. Codebase understanding**

Large windows allow models to ingest entire repositories.

#### **D. Reasoning depth**

More window = more internal chain‑of‑thought capacity.

---

### 🧠 **Clean Mental Model**

The context window is the model’s **short‑term memory**.

- Bigger window → more it can think about at once  
- Smaller window → more it forgets or truncates  

It doesn’t affect the model’s intelligence, but it dramatically affects **how much** it can reason over.

---
### 📊 **Context Window Comparison Across Major Models**

Below is a high‑level comparison of typical context window sizes across GPT, Claude, Gemini, Llama, and Mistral.  
(Exact numbers vary by version, but these are the widely referenced ranges.)

---

#### 🔵 **GPT (OpenAI)**
GPT models have steadily expanded their windows.

| Model | Typical Context Window |
|------|-------------------------|
| GPT‑3.5 | ~4k – 16k tokens |
| GPT‑4 | ~8k – 32k tokens |
| GPT‑4 Turbo | ~128k tokens |
| GPT‑4.1 / GPT‑4o family | ~128k tokens (common) |

**Strength:** Stable long‑context performance, strong compression.  
**Note:** GPT models often *summarize older context* to stay within limits.

---

#### 🟣 **Claude (Anthropic)**
Claude is the **long‑context leader**.

| Model | Typical Context Window |
|------|-------------------------|
| Claude 2 | 100k tokens |
| Claude 2.1 | 200k tokens |
| Claude 3 Opus/Sonnet/Haiku | 200k tokens |
| Claude 3.5 Sonnet | 200k tokens |
| Claude 3.7 | 200k tokens |

**Strength:** Exceptional long‑document recall and reasoning.  
**Note:** Claude is known for *high‑fidelity retrieval* even near the window limit.

---

#### 🟡 **Gemini (Google DeepMind)**
Gemini models are designed for multimodal + long‑context tasks.

| Model | Typical Context Window |
|------|-------------------------|
| Gemini 1.0 Pro | ~32k tokens |
| Gemini 1.5 Pro | **1M tokens** |
| Gemini 1.5 Flash | **1M tokens** |
| Gemini 2.0 | 1M+ tokens (varies by tier) |

**Strength:** Massive windows (up to 1 million tokens).  
**Note:** Gemini’s long‑context performance is optimized for multimodal (video, audio, images).

---

#### 🟢 **Llama (Meta)**
Open‑source models with growing context windows.

| Model | Typical Context Window |
|------|-------------------------|
| Llama 2 | 4k – 32k tokens |
| Llama 3 | 8k – 128k tokens |
| Llama 3.1 | 128k tokens |
| Llama 3.2 | 128k tokens |

**Strength:** Flexible and extendable (rope scaling).  
**Note:** Community variants often push windows to 256k–1M, but performance varies.

---

#### 🟠 **Mistral (Mistral AI)**

Mistral focuses on efficiency and long‑context scaling.

| Model | Typical Context Window |
|------|-------------------------|
| Mistral 7B | 8k tokens |
| Mixtral 8x7B | 32k tokens |
| Mixtral 8x22B | 64k tokens |
| Mistral Large | 128k tokens |

**Strength:** Strong performance per parameter + efficient long‑context.  
**Note:** MoE architecture helps maintain speed even with larger windows.

---

#### 🧭 **How They Compare at a Glance**

| Model Family | Typical Context Window | Notes |
|--------------|------------------------|-------|
| **GPT** | 32k–128k | Strong reasoning + stable long‑context |
| **Claude** | 200k | Best long‑context recall + accuracy |
| **Gemini** | **1M** | Largest windows available |
| **Llama** | 8k–128k | Open‑source, extendable |
| **Mistral** | 8k–128k | Efficient MoE scaling |

---

### 🧩 **Which Models Handle Long Context Best?**

###$ 🥇 **Gemini 1.5 Pro / Flash**  

Unmatched raw window size (1M tokens).

#### 🥈 **Claude 3.x**  

Best *quality* of long‑context reasoning and retrieval.

#### 🥉 **GPT‑4.1 / GPT‑4o**  

Strong balance of reasoning + long‑context stability.

#### 🟦 **Llama & Mistral**  

Great for open‑source deployments, but smaller windows unless extended.

---

### 🧠 **1. Reasoning models use the context window as *workspace*, not just memory**

Traditional LLMs treat the context window as:

- input text  
- conversation history  
- output tokens  

Reasoning models treat it as:

- **scratchpad**  
- **planning space**  
- **intermediate reasoning buffer**  
- **self‑reflection area**  

They generate far more internal tokens (deliberate steps) before producing the final answer.

**Effect:**  

Reasoning models “think inside the window,” so they need more room for internal chains of thought.

---

#### 🔍 **2. They generate *internal reasoning tokens* that count toward the window**

Models like:

- OpenAI o1  
- DeepSeek‑R1  
- QwQ‑32B  
- Gemini Flash Thinking  
- Claude Thinking models  

…all produce **hidden reasoning traces** before giving the final answer.

These internal steps:

- are not shown to the user  
- still consume tokens  
- reduce available space for user input  
- require larger windows to maintain coherence  

This is why reasoning models often have:

- higher token usage  
- slower responses  
- larger minimum context requirements  

---

#### 🧩 **3. They rely heavily on *long‑range dependencies***  

Reasoning models frequently need to:

- refer back to earlier parts of the prompt  
- maintain multi‑step logic  
- track variables, constraints, and assumptions  
- preserve intermediate results  

This requires:

- **stable long‑context attention**  
- **less degradation near the window limit**  
- **better compression of earlier tokens**  

Reasoning models are trained to maintain fidelity across long spans of text.

---

#### ⚙️ **4. They compress and summarize context more aggressively**

To free up space for reasoning, these models:

- summarize earlier parts of the conversation  
- compress irrelevant details  
- retain only the logical structure  
- drop stylistic or redundant content  

This is why reasoning models often feel more “focused” or “structured.”

They’re optimizing the window for **thinking**, not **chatting**.

---

#### 🔄 **5. They loop internally — using the window for iterative refinement**

Reasoning models often perform:

- multi‑pass reasoning  
- self‑critique  
- plan → evaluate → revise cycles  

Each cycle consumes tokens.

This is fundamentally different from classic LLMs, which generate output in a single forward pass.

---

#### 📏 **6. They require larger context windows to reach peak performance**

Because reasoning models use the window as a workspace, they benefit from:

- 128k  
- 200k  
- 1M token windows  

A reasoning model with a small window is like a mathematician with a tiny notepad.

---

## 🧠 Internal Reasoning Tokens

Internal reasoning tokens are one of the most important — and least visible — innovations behind modern reasoning‑optimized models. They’re the hidden “scratch work” the model performs before giving you an answer.

Internal reasoning tokens are **tokens the model generates for itself**, not for the user.  
They represent the model’s *private chain of thought* — the intermediate steps it uses to:

- break down a problem  
- explore options  
- check its own work  
- revise incorrect steps  
- plan multi‑step solutions  

These tokens **never appear in the final output**, but they still count toward the context window.

---

### 🔍 Why They Exist

Classic LLMs generate answers in a single forward pass.  
Reasoning models do something different:

> They generate *internal* text that helps them think before they speak.

This internal text is where the model:

- decomposes the problem  
- tries multiple approaches  
- evaluates partial solutions  
- rejects bad reasoning  
- converges on a final answer  

It’s the AI equivalent of scratch paper.

---

### 🧩 How Internal Reasoning Tokens Flow Through the Model

A simplified view:

```txt
User Prompt
   ↓
Model generates hidden reasoning tokens
   ↓
Model evaluates and refines those tokens
   ↓
Model produces final answer (visible to user)
```

Those hidden tokens might include:

- step‑by‑step logic  
- intermediate calculations  
- hypotheses  
- self‑critique  
- alternative paths  
- summaries of earlier reasoning  

They’re not shown, but they shape the final output.

---

### ⚙️ **Where They Live in the Context Window**

Internal reasoning tokens **consume part of the context window**, just like user input.

Example:

- Model has a 128k context window  
- User prompt uses 10k tokens  
- Model may generate 20k–40k internal reasoning tokens  
- Remaining space is used for the final answer  

This is why reasoning models often need **larger context windows** than standard LLMs.

---

### 🔄 They Enable Multi‑Pass Thinking

Reasoning models don’t just generate internal tokens once.  
They often loop:

1. Generate reasoning tokens  
2. Evaluate them  
3. Rewrite or refine them  
4. Try alternative paths  
5. Produce final answer  

This iterative refinement is what gives reasoning models:

- deeper logic  
- fewer hallucinations  
- better math  
- stronger planning  
- more consistent answers  

---

### 🧠 Why You Don’t See Them

Internal reasoning tokens are hidden because:

- they can be messy  
- they may contain false starts  
- they may include incorrect intermediate steps  
- they’re not meant to be consumed by humans  

You only see the polished final answer.

---

### 🧭 Internal Reasoning Tokens Clean Mental Model

#### Internal reasoning tokens = the model’s scratchpad.

- **Tokens** = the pieces of text  
- **Embeddings** = the numerical meaning of those pieces  
- **Activations** = the model’s real‑time thinking  
- **Parameters** = the model’s long‑term knowledge  
- **Internal reasoning tokens** = the model’s private notes while solving the problem  

They’re the bridge between raw intelligence and the final answer.

---

## Context Windows and Retrieval (RAG)

Context windows and Retrieval‑Augmented Generation (RAG) work together in a way that’s almost architectural: the context window is the **workspace**, and RAG is the **supply chain** feeding that workspace. Once you see how they interact, the strengths and limitations of long‑context models become much clearer.

---

### 🧠 1. The Context Window Sets the Hard Limit

A model can only “think over” the tokens inside its context window.  
RAG doesn’t bypass this limit — it **feeds** the window.

So if a model has a 128k window:

- your prompt  
- retrieved documents  
- system instructions  
- internal reasoning tokens  
- the model’s output  

…all must fit inside that 128k.

RAG is powerful, but it still has to play inside the boundaries of the window.

---

### 📥 2. RAG Decides *What* Goes Into the Window

RAG’s job is to **retrieve only the most relevant chunks** from an external knowledge base and insert them into the prompt.

This means:

- the model doesn’t need to store everything in parameters  
- the context window becomes a curated, on‑demand memory buffer  
- irrelevant information stays out, preserving space  

RAG is essentially a **filter** that protects the context window from overload.

---

### 🧩 3. Chunking Strategy Determines How Much Fits

Because the window is finite, RAG pipelines break documents into **chunks**.

Chunk size affects:

- recall  
- precision  
- context window usage  
- hallucination risk  

Examples:

- **Small chunks (200–500 tokens)** → more precise retrieval, but more chunks  
- **Large chunks (1k–4k tokens)** → richer context, but fewer can fit in the window  

Choosing chunk size is a balancing act between **context richness** and **window capacity**.

---

### 🔍 4. RAG Uses the Window for Grounding, Not Reasoning

RAG fills the window with **facts**.  
The model uses its parameters + reasoning tokens to interpret those facts.

So the window becomes:

- a temporary knowledge store  
- a grounding buffer  
- a reference sheet  

The model’s reasoning happens *on top of* the retrieved context.

---

### 🔄 5. Long Context Models Reduce RAG Load

Models with huge windows (Gemini 1.5, Claude 3.x) can:

- ingest entire documents  
- reduce chunking complexity  
- require fewer retrieval passes  
- maintain more global context  

This shifts RAG from “retrieve small pieces” to “retrieve entire sections”.

But even with million‑token windows, RAG still matters because:
- retrieval improves relevance  
- retrieval reduces noise  
- retrieval avoids wasting window space  

Long context doesn’t replace RAG — it **amplifies** it.

---

### ⚙️ 6. RAG Pipelines Often Use Multi‑Stage Retrieval to Fit the Window

To avoid overflowing the window, modern RAG systems use:

- vector search  
- reranking  
- summarization  
- compression  
- deduplication  

This ensures only the most relevant content enters the window.

Think of it as:
**RAG = bouncer  
Context window = VIP room**

Only the best content gets in.

---

### 🧠 7. Reasoning Models Use the Window Differently

Reasoning‑optimized models (o1‑style, DeepSeek‑R1, Claude Thinking) generate **internal reasoning tokens** that also consume window space.

This means:

- RAG must leave room for the model to think  
- too much retrieved text can choke the reasoning process  
- retrieval must be more selective for reasoning models  

RAG for reasoning models is more like **precision surgery** than bulk retrieval.

---

### 🧭 Context Window and RAG Clean Mental Model

- Context window = workspace
- RAG = the system that fills the workspace with relevant information
- Reasoning tokens = the model’s internal thinking inside that workspace

They all share the same finite space, so good RAG design is about **maximizing relevance per token**.

---
