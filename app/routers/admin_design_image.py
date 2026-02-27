from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.design_image import DesignImage
from app.models.module_item import ModuleItem
from app.schemas.design_image_schema import ImageCreate
from app.core.dependencies import get_current_admin

router = APIRouter(
    prefix="/api/admin/design-images",
    tags=["Admin Design Images"]
)

@router.post("/")
def add_image(
    data: ImageCreate,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    item = db.query(ModuleItem).filter(ModuleItem.id == data.module_item_id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Module item not found")

    image = DesignImage(**data.dict())
    db.add(image)
    db.commit()
    db.refresh(image)

    return image


@router.get("/{module_item_id}")
def get_images(module_item_id: int, db: Session = Depends(get_db)):
    return db.query(DesignImage).filter(
        DesignImage.module_item_id == module_item_id
    ).all()


@router.delete("/{image_id}")
def delete_image(
    image_id: int,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    image = db.query(DesignImage).filter(DesignImage.id == image_id).first()

    if not image:
        raise HTTPException(status_code=404, detail="Image not found")

    db.delete(image)
    db.commit()

    return {"message": "Image deleted"}