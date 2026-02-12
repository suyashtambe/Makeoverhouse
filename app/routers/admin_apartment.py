from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.apartment import ApartmentType
from app.schemas.apartment_schema import ApartmentCreate, ApartmentUpdate
from app.core.dependencies import get_current_admin

router = APIRouter(
    prefix="/api/admin/apartment-types",
    tags=["Admin Apartment"]
)

@router.post("/")
def create_apartment(
    data: ApartmentCreate,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    existing = db.query(ApartmentType).filter(ApartmentType.name == data.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Apartment type already exists")

    apartment = ApartmentType(**data.dict())
    db.add(apartment)
    db.commit()
    db.refresh(apartment)

    return apartment


@router.get("/")
def get_apartments(
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    return db.query(ApartmentType).all()


@router.put("/{apartment_id}")
def update_apartment(
    apartment_id: int,
    data: ApartmentUpdate,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    apartment = db.query(ApartmentType).filter(ApartmentType.id == apartment_id).first()

    if not apartment:
        raise HTTPException(status_code=404, detail="Apartment type not found")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(apartment, key, value)

    db.commit()
    db.refresh(apartment)

    return apartment


@router.delete("/{apartment_id}")
def delete_apartment(
    apartment_id: int,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    apartment = db.query(ApartmentType).filter(ApartmentType.id == apartment_id).first()

    if not apartment:
        raise HTTPException(status_code=404, detail="Apartment type not found")

    db.delete(apartment)
    db.commit()

    return {"message": "Apartment type deleted successfully"}
