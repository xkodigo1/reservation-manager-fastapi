from sqlalchemy import Column, Integer, ForeignKey, Date, Time, Enum, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum

class ReservationStatus(enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    canceled = "canceled"

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id", ondelete="CASCADE"), nullable=False)
    date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    status = Column(Enum(ReservationStatus), default=ReservationStatus.pending, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    # ORM Relationships
    user = relationship("User", backref="reservations")
    room = relationship("Room", backref="reservations")
