from app.db.session import SessionLocal

def get_db(): # Dependency to get DB session
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() # Ensure db session is closed after use