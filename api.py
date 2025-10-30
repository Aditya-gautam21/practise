from fastapi import FastAPI, HTTPException
from fastapi.cors.middleware import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import Logging


try:
    from agents import automateTask
except ImportError:
    raise ImportError("Error in import automateTask, trya agian later")

Logging.basicConfig(level=Logging.INFO)
logger = Logging.getLogger(__name__)