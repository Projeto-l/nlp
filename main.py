from fastapi import FastAPI
from src.api.endpoints import router as interaction_router

app = FastAPI()

app.include_router(interaction_router, prefix="/api/v1")