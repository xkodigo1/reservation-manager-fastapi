from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Settings(BaseSettings):

    # Application settings
    app_name: str = "Reservation Manager"
    app_env: str = "development"
    app_port: int = 8000
    
    # Database settings
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str
    jwt_secret_key: str

    # JWT settings
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    jwt_expiration_seconds: int = 3600  # 1 hour

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()