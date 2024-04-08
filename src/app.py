from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import v1_router

app = FastAPI(
    title="event-service",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router)
