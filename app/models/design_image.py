from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class DesignImage(Base):
    __tablename__ = "design_images"

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, nullable=False)

    module_item_id = Column(Integer, ForeignKey("module_items.id"))

    module_item = relationship("ModuleItem")