from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.database import Base
import datetime

class RoomModule(Base):
    __tablename__ = "room_modules"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
