from pydantic import BaseModel

class ImageCreate(BaseModel):
    image_url: str
    module_item_id: int

class ImageResponse(BaseModel):
    id: int
    image_url: str
    module_item_id: int

    class Config:
        orm_mode = True