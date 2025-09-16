from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.dependencies import get_db
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from app.api.routes import auth

from app.core.config import settings

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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

app.include_router(auth.router)

