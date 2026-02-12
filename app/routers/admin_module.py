from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.module import RoomModule
from app.schemas.module_schema import ModuleCreate, ModuleUpdate
from app.core.dependencies import get_current_admin

router = APIRouter(
    prefix="/api/admin/modules",
    tags=["Admin Room Modules"]
)

@router.post("/")
def create_module(
    data: ModuleCreate,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    existing = db.query(RoomModule).filter(RoomModule.name == data.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Module already exists")

    module = RoomModule(**data.dict())
    db.add(module)
    db.commit()
    db.refresh(module)

    return module


@router.get("/")
def get_modules(
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    return db.query(RoomModule).all()


@router.put("/{module_id}")
def update_module(
    module_id: int,
    data: ModuleUpdate,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    module = db.query(RoomModule).filter(RoomModule.id == module_id).first()

    if not module:
        raise HTTPException(status_code=404, detail="Module not found")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(module, key, value)

    db.commit()
    db.refresh(module)

    return module


@router.delete("/{module_id}")
def delete_module(
    module_id: int,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    module = db.query(RoomModule).filter(RoomModule.id == module_id).first()

    if not module:
        raise HTTPException(status_code=404, detail="Module not found")

    db.delete(module)
    db.commit()

    return {"message": "Module deleted successfully"}
