from fastapi import FastAPI, HTTPException
import Logging
from fastapi.cors.middleware import CORSMiddleware
form pydantic import BaseModel

Logging.basicConfig(level=Logging.INFO)
logger = Logging.getLogger(__name__)

app = FastAPI(title="Practising building aps", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:5173","https://localhost:3000"],
    allow_credentials=True,
    allow_methods=[*],
    allow_headers=[*]
)