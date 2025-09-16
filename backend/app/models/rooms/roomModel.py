from sqlalchemy import Column, Integer, String, Enum, JSON, TIMESTAMP
from sqlalchemy.sql import func
from app.db.base import Base
import enum

class Headquarter(enum.Enum):
    bogota = "Bogotá"
    medellin = "Medellín"

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    headquarter = Column(Enum(Headquarter), nullable=False)
    capacity = Column(Integer, nullable=False)
    resources = Column(JSON, nullable=True) # e.g., {"projector": true, "whiteboard": false}
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
