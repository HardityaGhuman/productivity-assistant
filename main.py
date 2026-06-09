import os
from datetime import datetime
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing. Please add it to your .env file.")

# Above block is made for better error handling and visibility

client = Groq(api_key=GROQ_API_KEY)

def get_user_input():
    task = input("Enter your productivity task: ")
    return task

"""

Some pointers while setting up prompts:

1. P - Persona; Establishes how you want the LLM to behave
2. T - Task; Explains what you want the LLM to do exactly
3. C - Context; Provides background or current information
4. F - Format; Specifies the structure of the output (usually JSON format in key - value pairs, makes it easier to extract information on the frontend level)
5. Constraints - Specifies rules, limitations, or boundaries the LLM must follow (Specifying what the LLM is not allowed to do)

* Also need to set up guardrails for cases where the task is unclear, incomplete, or inappropriate *

"""

def generate_response(task):
    prompt = f"""
### 1. Persona (P)
You are an expert AI Productivity Assistant specializing in time management, goal setting, and workflow optimization. Your tone is professional, encouraging, and highly structured.

### 2. Context (C)
The user has submitted the following task:
"{task}"

### 3. Task (T)
Analyze the user's task. If the task is valid, actionable, and appropriate, break it down into a practical, beginner-friendly step-by-step plan. If the task is unclear, incomplete, or inappropriate, trigger the guardrails.

### 4. Constraints
- You MUST respond ONLY with a raw JSON object.
- Do NOT wrap the JSON in markdown code blocks (e.g., do not use ```json ... ```).
- Do NOT include any introductory or concluding text outside of the JSON.
- All recommendations must be realistic, actionable, and beginner-friendly.

### 5. Guardrails
Evaluate the user task first. If the task is:
- Gibberish, single characters, or meaningless text.
- Completely unclear or lacking context to create a plan.
- Inappropriate, offensive, or harmful.
Then:
- Set "status" to "error".
- Set "is_valid_task" to false.
- Populate "guardrail_message" with a polite, helpful explanation of why the task could not be processed and guidance on how the user can clarify it.
- Set all other fields to null.

### 6. Format (F)
Your output must strictly adhere to this JSON structure:
{{
  "status": "success" or "error",
  "is_valid_task": true or false,
  "guardrail_message": "string" or null,
  "goal": "string" or null,
  "key_steps": ["string", "string", ...] or null,
  "suggested_timeline": "string" or null,
  "tools_or_resources": ["string", "string", ...] or null,
  "final_recommendation": "string" or null
}}
"""

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an AI Productivity Assistant. You must output all responses in valid JSON format."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        model=MODEL_NAME,
        temperature=0.4,
        response_format={"type": "json_object"}
    )

    return chat_completion.choices[0].message.content

def save_response(task, response):
    os.makedirs("outputs", exist_ok=True)

    file_path = "outputs/response.txt"

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"Date: {datetime.now()}\n")
        file.write(f"Task: {task}\n")
        file.write("AI Response:\n")
        file.write(response)
        file.write("\n")
        file.write("-" * 60)
        file.write("\n\n")

    print(f"\nResponse saved to {file_path}")

def main():
    print("AI Productivity Assistant using Groq")
    print("-" * 40)

    task = get_user_input()
    response = generate_response(task)

    print("\nAI Response:\n")
    print(response)

    save_response(task, response)

if __name__ == "__main__":
    main()

