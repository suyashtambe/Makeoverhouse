from pydantic import BaseModel
from typing import Optional

class ModuleCreate(BaseModel):
    name: str
    description: Optional[str] = None

class ModuleUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

class ModuleResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    is_active: bool

    class Config:
        orm_mode = True
