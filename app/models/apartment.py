from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.database import Base
import datetime

class ApartmentType(Base):
    __tablename__ = "apartment_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
