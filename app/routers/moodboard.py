from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.moodboard import Moodboard
from app.models.module_item import ModuleItem
from app.schemas.moodboard_schema import MoodboardCreate
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/api/moodboard", tags=["Moodboard"])

@router.post("/")
def save_design(
    data: MoodboardCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    item = db.query(ModuleItem).filter(ModuleItem.id == data.module_item_id).first()

    save = Moodboard(user_id=user.id, module_item_id=item.id)
    db.add(save)
    db.commit()

    return {"message": "Design saved"}

@router.get("/")
def get_saved_designs(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return db.query(Moodboard).filter(Moodboard.user_id == user.id).all()

@router.delete("/{id}")
def remove_design(
    id: int,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    item = db.query(Moodboard).filter(
        Moodboard.id == id,
        Moodboard.user_id == user.id
    ).first()

    db.delete(item)
    db.commit()

    return {"message": "Removed"}