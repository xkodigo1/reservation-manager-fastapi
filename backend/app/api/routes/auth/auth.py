from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from app.core.jwt import create_access_token
from app.core.security import verify_password
from app.utils.dependencies import get_db
from app.models.users.userModel import User
from app.schemas.auth import Token
from app.core.config import settings
from app.schemas.users.userSchema import UserCreate, UserOut
from app.core.security import get_password_hash
from app.api.deps import get_current_user
from fastapi import Path
from app.models.users.userModel import UserRole

router = APIRouter(prefix="/auth", tags=["Auth"])

def require_admin(current_user=Depends(get_current_user)):
    if current_user.role != UserRole.admin:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return current_user

@router.post("/register", response_model=Token)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_in.email).first()
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(
        email=user_in.email,
        first_name=user_in.first_name,
        last_name=user_in.last_name,
        password_hash=get_password_hash(user_in.password),
        role=user_in.role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    access_token_expires = timedelta(seconds=settings.jwt_expiration_seconds)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(seconds=settings.jwt_expiration_seconds)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
