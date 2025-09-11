from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from utils.dependencies import get_db

from core.config import settings

app = FastAPI()

@app.get("/")
def root():
    return {
        "app": settings.app_name,
        "environment": settings.app_env,
        "db_user": settings.db_user
        }

@app.get("/ping-db")
def ping_db(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "Database connection successful"}
    except Exception as e:
        return {"status": "Database connection failed", "error": str(e)}