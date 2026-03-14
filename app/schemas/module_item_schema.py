from pydantic import BaseModel
from typing import Optional

class ModuleItemCreate(BaseModel):
    title: str
    description: Optional[str] = None
    price: Optional[int] = None
    apartment_id: int
    module_id: int

class ModuleItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    is_active: Optional[bool] = None

class ModuleItemResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    price: Optional[int]
    apartment_id: int
    module_id: int
    is_active: bool

    class Config:
        orm_mode = True


class ModuleItemCreate(BaseModel):
    title: str
    description: Optional[str] = None
    price: Optional[int] = None
    style: Optional[str] = None
    apartment_id: int
    module_id: int