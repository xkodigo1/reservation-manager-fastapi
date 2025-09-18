from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from datetime import date as date_type

from app.utils.dependencies import get_db
from app.api.deps import get_current_user
from app.models.reservations.reservationModel import Reservation, ReservationStatus
from app.schemas.reservations.reservSchema import ReservationBase, ReservationOut
from app.models.users.userModel import UserRole

router = APIRouter(prefix="/reservations", tags=["Reservations"])


@router.post("/", response_model=ReservationOut)
def create_reservation(reservation_in: ReservationBase, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    # Validación simple: el usuario actual debe coincidir con user_id
    if reservation_in.user_id != current_user.id and current_user.role != UserRole.admin:
        raise HTTPException(status_code=403, detail="Cannot create reservations for other users")
    # TODO: Aquí se puede validar cruce de horarios y bloques de 1 hora
    reservation = Reservation(
        user_id=reservation_in.user_id,
        room_id=reservation_in.room_id,
        date=reservation_in.date,
        start_time=reservation_in.start_time,
        end_time=reservation_in.end_time,
        status=reservation_in.status,
    )
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return reservation


@router.get("/me", response_model=list[ReservationOut])
def my_reservations(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(Reservation).filter(Reservation.user_id == current_user.id).all()


@router.get("/room/{room_id}", response_model=list[ReservationOut])
def reservations_by_room(room_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    return db.query(Reservation).filter(Reservation.room_id == room_id).all()


@router.get("/date/{reservation_date}", response_model=list[ReservationOut])
def reservations_by_date(reservation_date: date_type, db: Session = Depends(get_db)):
    return db.query(Reservation).filter(Reservation.date == reservation_date).all()


@router.delete("/{reservation_id}", status_code=204)
def cancel_reservation(reservation_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    # Solo el dueño o admin pueden cancelar
    if reservation.user_id != current_user.id and current_user.role != UserRole.admin:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    reservation.status = ReservationStatus.canceled
    db.commit()
    return None
