from pydantic import BaseModel
from datetime import date, time, datetime

class ReservationStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    canceled = "canceled"

class ReservationBase(BaseModel):
    date: date
    start_time: time
    end_time: time
    status: ReservationStatus = ReservationStatus.pending

class ReservationCreate(ReservationBase):
    user_id: int
    room_id: int

class ReservationUpdate(BaseModel):
     status: ReservationStatus | None = None

class ReservationOut(ReservationBase):
    id: int
    user_id: int
    room_id: int
    created_at: datetime

    class Config:
        orm_mode = True  