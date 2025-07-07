from fastapi import FastAPI
from app.api.routers.summaries import router as summaries_router
from app.api.routers.health import router as health_router

app = FastAPI(title="Wikipedia Summarizer", version="0.1.0")


app.include_router(health_router)

app.include_router(summaries_router)
