# AI Productivity Assistant

A model-agnostic CLI + API tool that uses LLM providers to generate structured productivity guides and study plans, saving the outputs to a local file. Powered by [LiteLLM](https://docs.litellm.ai/docs/providers), it supports **100+ LLM providers** — just change the model name in your `.env` file to switch between them.

---

## Features & Tech Stack
- **CLI Interface:** Standard user input prompt.
- **Model Agnostic:** Switch between any LLM provider (Groq, OpenAI, Gemini, Anthropic, Azure, Ollama, and 100+ more) by changing a single environment variable.
- **Structured Output:** Automatically generates plans containing a Goal, Key Steps, Timeline, Tools, and Recommendations.
- **History Logging:** Saves runs to `outputs/response.txt` with execution timestamps.
- **Tech Stack:** Python 3, LiteLLM, FastAPI, `python-dotenv`.

---

## Setup & Run

### 1. Installation
```bash
# Set up virtual environment and install packages
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Environment Configuration
Create a `.env` file in the root directory (use `.env.example` as a template):
```env
# Set the API key for the provider you want to use
GROQ_API_KEY=your_api_key_here

# Format: provider/model_id
MODEL_NAME=groq/llama-3.3-70b-versatile

API_SECRET_TOKEN=your_api_secret_token
```

**Supported providers include:** Groq, OpenAI, Gemini, Anthropic, Azure, Ollama, Hugging Face, and many more. See [LiteLLM Provider Docs](https://docs.litellm.ai/docs/providers) for the full list.

### 3. Run CLI
```bash
python3 main.py
```

---

## Example Run

### Input
> "Explain Git and GitHub in simple terms"

### Output Screenshot
![Sample Run Screenshot](images/placeholder_sample_run.png)

---

## Learning Outcomes
- Managing API keys securely using `.env` files and `.gitignore`.
- Structuring LLM prompts to return consistent, formatted responses.
- Building model-agnostic applications using LiteLLM.
- Handling file I/O operations (appending text, creating directories) in Python.

---

## FastAPI Backend

This project includes a FastAPI backend API. The LLM response generation logic is shared with the CLI, but task input comes from an HTTP request body instead of `input()`.

### Environment Variables
Create a `.env` file using `.env.example` as a reference:

```env
GROQ_API_KEY=your_api_key_here
MODEL_NAME=groq/llama-3.3-70b-versatile
API_SECRET_TOKEN=your_api_secret_token
```

### Run API Server
```bash
source venv/bin/activate
python -m uvicorn api:app --reload
```

Swagger docs:

```text
http://127.0.0.1:8000/docs
```

### Endpoints
| Method | Endpoint | Purpose | Auth Required |
|---|---|---|---|
| GET | `/` | API health check | No |
| POST | `/generate` | Generate an AI productivity response | Yes |
| GET | `/outputs` | View saved responses | Yes |

### Bearer Token Authentication
Protected endpoints require this header:

```http
Authorization: Bearer your_api_secret_token
```

In Swagger, click `Authorize` and enter only the token value. Swagger adds `Bearer` automatically.

### Sample Request Body
```json
{
  "task": "Help me learn FastAPI as a beginner"
}
```

### API Screenshots

#### Swagger Docs
![Swagger Docs](images/api_ss_4.png)

#### Unauthorized Request
![Unauthorized 401 Request](images/api_ss_3.png)

#### Successful Generate Request
![Successful POST Generate Request](images/api_ss_2.png)

#### Updated Output File
![Updated Output File](images/api_ss_1.png)

### What Changed From CLI To API

The original app took task input from the terminal using `input()`. It now accepts task input through a FastAPI `POST /generate` endpoint using a JSON request body.

The LLM response generation logic remains the same, but the output is now returned as a JSON API response and saved to `outputs/response.txt`. Protected routes use static Bearer token authentication from `.env`.
