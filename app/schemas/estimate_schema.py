from pydantic import BaseModel
from typing import List

class EstimateCreate(BaseModel):
    module_item_ids: List[int]