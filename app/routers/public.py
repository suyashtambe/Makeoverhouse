from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.apartment import ApartmentType
from app.models.module import RoomModule
from app.models.module_item import ModuleItem

router = APIRouter(prefix="/api", tags=["Public APIs"])

@router.get("/apartments")
def get_apartments(db: Session = Depends(get_db)):
    return db.query(ApartmentType).filter(ApartmentType.is_active == True).all()

@router.get("/modules")
def get_modules(db: Session = Depends(get_db)):
    return db.query(RoomModule).filter(RoomModule.is_active == True).all()

@router.get("/module-items")
def get_module_items(db: Session = Depends(get_db)):
    return db.query(ModuleItem).filter(ModuleItem.is_active == True).all()

@router.get("/designs")
def get_designs(
    apartment_id: int,
    module_id: int,
    db: Session = Depends(get_db)
):
    return db.query(ModuleItem).filter(
        ModuleItem.apartment_id == apartment_id,
        ModuleItem.module_id == module_id,
        ModuleItem.is_active == True
    ).all()


