# AI Productivity Assistant

A minimal CLI tool that queries the Groq API to generate structured productivity guides and study plans, saving the outputs to a local file.

---

## Features & Tech Stack
- **CLI Interface:** Standard user input prompt.
- **Structured Output:** Automatically generates plans containing a Goal, Key Steps, Timeline, Tools, and Recommendations.
- **History Logging:** Saves runs to `outputs/response.txt` with execution timestamps.
- **Tech Stack:** Python 3, `groq` API SDK, `python-dotenv`.

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
GROQ_API_KEY=your_actual_api_key_here
MODEL_NAME=llama-3.3-70b-versatile
```

### 3. Run
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
- Handling file I/O operations (appending text, creating directories) in Python.

---

## FastAPI Backend

This project was upgraded from a terminal based CLI app into a FastAPI backend API. The existing Groq response generation logic is reused, but task input now comes from an HTTP request body instead of `input()`.

### Environment Variables
Create a `.env` file using `.env.example` as a reference:

```env
GROQ_API_KEY=your_actual_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile
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
