from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
import datetime

class ModuleItem(Base):
    __tablename__ = "module_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    style = Column(String, nullable=True)
    price = Column(Integer, nullable=True)

    apartment_id = Column(Integer, ForeignKey("apartment_types.id"))
    module_id = Column(Integer, ForeignKey("room_modules.id"))

    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    apartment = relationship("ApartmentType")
    module = relationship("RoomModule")
