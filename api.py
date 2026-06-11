import os
# pyrefly: ignore [missing-import]
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from main import generate_response, save_response, MODEL_NAME
from auth import verify_bearer_token

app = FastAPI(title = "Productivity Assistant API") # This creates FastAPI app
OUTPUT_FILE = "outputs/response.txt"

class GenerateRequest(BaseModel):
    task: str # This defines expected JSON body structure

"""
API expects this:
{
  "task": "Help me plan my day"
}
"""

# Creates unprotected API health check route
# Used to check if API is running or not

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "Productivity Assistant API is running"
    }

# This creates the main protected API route:

"""
This route:

Checks the token.
Reads the task from JSON.
Rejects empty tasks with 400.
Calls your existing LLM function.
Saves the response.
Returns the AI response as JSON.
"""

@app.post("/generate")
def generate_task_response(
    request: GenerateRequest,
    _authenticated: None = Depends(verify_bearer_token)
):
    task = request.task.strip()

    if not task:
        raise HTTPException(
            status_code=400,
            detail="Task cannot be empty"
        )

    try:
        response = generate_response(task)
        save_response(task, response)

        return {
            "task": task,
            "model_used": MODEL_NAME,
            "response": response
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@app.get("/outputs")
def get_saved_outputs(_authenticated: None = Depends(verify_bearer_token)):
    try:
        if not os.path.exists(OUTPUT_FILE):
            return {
                "message": "No saved outputs found yet.",
                "outputs": ""
            }

        with open(OUTPUT_FILE, "r", encoding="utf-8") as file:
            outputs = file.read()

        return {
            "outputs": outputs
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )
