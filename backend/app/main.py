from fastapi import FastAPI

from core.config import settings

app = FastAPI()

@app.get("/")
def root():
    return {
        "app": settings.app_name,
        "environment": settings.app_env,
        "db_user": settings.db_user
        }