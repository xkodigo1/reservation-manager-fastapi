from pydantic import BaseModel
from enum import Enum
from typing import List
from datetime import datetime

class Headquarter(str, Enum):
    bogota = "Bogotá"
    medellin = "Medellín"

class RoomBase(BaseModel):
    name: str
    headquarter: Headquarter
    capacity: int
    resources: List[str]

class RoomCreate(BaseModel):
    pass

class RoomUpdate(RoomBase):
    name: str | None = None
    headquarter: Headquarter | None = None
    capacity: int | None = None
    resources: List[str] | None = None

class RoomOut(RoomBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True 