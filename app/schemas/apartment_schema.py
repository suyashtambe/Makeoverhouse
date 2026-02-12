from pydantic import BaseModel
from typing import Optional

class ApartmentCreate(BaseModel):
    name: str
    description: Optional[str] = None

class ApartmentUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

class ApartmentResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    is_active: bool

    class Config:
        orm_mode = True
