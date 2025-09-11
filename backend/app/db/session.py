from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

db_url = f"mysql+pymysql://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

engine = create_engine(db_url, pool_pre_ping=True) # Enable pool pre-ping to avoid stale connections

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

