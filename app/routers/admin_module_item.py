from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.module_item import ModuleItem
from app.models.apartment import ApartmentType
from app.models.module import RoomModule
from app.schemas.module_item_schema import ModuleItemCreate, ModuleItemUpdate
from app.core.dependencies import get_current_admin

router = APIRouter(
    prefix="/api/admin/module-items",
    tags=["Admin Module Items"]
)

@router.post("/")
def create_module_item(
    data: ModuleItemCreate,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    apartment = db.query(ApartmentType).filter(ApartmentType.id == data.apartment_id).first()
    module = db.query(RoomModule).filter(RoomModule.id == data.module_id).first()

    if not apartment:
        raise HTTPException(status_code=404, detail="Apartment type not found")

    if not module:
        raise HTTPException(status_code=404, detail="Module not found")

    item = ModuleItem(**data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)

    return item


@router.get("/")
def get_module_items(
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    return db.query(ModuleItem).all()


@router.put("/{item_id}")
def update_module_item(
    item_id: int,
    data: ModuleItemUpdate,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    item = db.query(ModuleItem).filter(ModuleItem.id == item_id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)

    return item


@router.delete("/{item_id}")
def delete_module_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    item = db.query(ModuleItem).filter(ModuleItem.id == item_id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()

    return {"message": "Module item deleted successfully"}
