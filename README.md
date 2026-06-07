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
![Sample Run Screenshot](placeholder_sample_run.png)

---

## Learning Outcomes
- Managing API keys securely using `.env` files and `.gitignore`.
- Structuring LLM prompts to return consistent, formatted responses.
- Handling file I/O operations (appending text, creating directories) in Python.
