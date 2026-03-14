from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base

class EstimateItem(Base):
    __tablename__ = "estimate_items"

    id = Column(Integer, primary_key=True, index=True)
    estimate_id = Column(Integer, ForeignKey("estimates.id"))
    module_item_id = Column(Integer, ForeignKey("module_items.id"))
    price = Column(Integer)