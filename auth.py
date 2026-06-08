import os
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from fastapi import Depends, HTTPException
# pyrefly: ignore [missing-import]
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

load_dotenv()

API_SECRET_TOKEN = os.getenv("API_SECRET_TOKEN")
security = HTTPBearer()

# This checks the bearer token
# It expects the header to look like Authorization: Bearer your_token_here
# This is used to verify the authenticity of the request

def verify_bearer_token(credentials: HTTPAuthorizationCredentials = Depends(security)):

    if not API_SECRET_TOKEN:
        raise HTTPException(
            status_code=500,
            detail="API_SECRET_TOKEN is missing on the server"
        )

    if credentials.credentials != API_SECRET_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Invalid bearer token"
        )
