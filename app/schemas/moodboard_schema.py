from pydantic import BaseModel

class MoodboardCreate(BaseModel):
    module_item_id: int