from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session

from app.utils.dependencies import get_db
from app.api.deps import get_current_user
from app.models.rooms.roomModel import Room
from app.schemas.rooms.roomSchema import RoomBase, RoomUpdate, RoomOut
from app.models.users.userModel import UserRole

router = APIRouter(prefix="/rooms", tags=["Rooms"])


def require_admin(current_user=Depends(get_current_user)):
    if current_user.role != UserRole.admin:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return current_user


@router.get("/", response_model=list[RoomOut])
def list_rooms(db: Session = Depends(get_db)):
    return db.query(Room).all()


@router.get("/{room_id}", response_model=RoomOut)
def get_room(room_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room


@router.post("/", response_model=RoomOut, dependencies=[Depends(require_admin)])
def create_room(room_in: RoomBase, db: Session = Depends(get_db)):
    room = Room(
        name=room_in.name,
        Headquarter=room_in.headquarter,
        capacity=room_in.capacity,
        resources=room_in.resources,
    )
    db.add(room)
    db.commit()
    db.refresh(room)
    return room


@router.put("/{room_id}", response_model=RoomOut, dependencies=[Depends(require_admin)])
def update_room(room_id: int, room_in: RoomUpdate, db: Session = Depends(get_db)):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    if room_in.name is not None:
        room.name = room_in.name
    if room_in.headquarter is not None:
        room.Headquarter = room_in.headquarter
    if room_in.capacity is not None:
        room.capacity = room_in.capacity
    if room_in.resources is not None:
        room.resources = room_in.resources

    db.commit()
    db.refresh(room)
    return room


@router.delete("/{room_id}", status_code=204, dependencies=[Depends(require_admin)])
def delete_room(room_id: int, db: Session = Depends(get_db)):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    db.delete(room)
    db.commit()
    return None
