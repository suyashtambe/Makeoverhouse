from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.design_image import DesignImage
from app.models.module_item import ModuleItem

router = APIRouter(prefix="/api/inspirations", tags=["Get Inspired"])

@router.get("/")
def get_inspirations(db: Session = Depends(get_db)):
    return db.query(ModuleItem).filter(ModuleItem.is_active == True).all()

@router.get("/filter")
def filter_inspirations(
    apartment_id: int = None,
    module_id: int = None,
    style: str = None,
    min_price: int = None,
    max_price: int = None,
    db: Session = Depends(get_db)
):
    query = db.query(ModuleItem)

    if apartment_id:
        query = query.filter(ModuleItem.apartment_id == apartment_id)

    if module_id:
        query = query.filter(ModuleItem.module_id == module_id)

    if style:
        query = query.filter(ModuleItem.style == style)

    if min_price:
        query = query.filter(ModuleItem.price >= min_price)

    if max_price:
        query = query.filter(ModuleItem.price <= max_price)

    return query.all()

@router.get("/{design_id}")
def get_design_detail(design_id: int, db: Session = Depends(get_db)):
    return db.query(ModuleItem).filter(
        ModuleItem.id == design_id
    ).first()
    
    from app.models.design_image import DesignImage

@router.get("/{design_id}/images")
def get_design_images(design_id: int, db: Session = Depends(get_db)):
    return db.query(DesignImage).filter(
        DesignImage.module_item_id == design_id
    ).all()