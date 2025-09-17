from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.dependencies import get_db
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from app.api.routes import auth
from app.api.routes.users import userRoute
from app.api.routes.rooms import roomRoute

from app.core.config import settings

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

app.include_router(auth.router)
app.include_router(userRoute.router)
app.include_router(roomRoute.router)

