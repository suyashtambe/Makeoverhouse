from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
import datetime

class Moodboard(Base):
    __tablename__ = "moodboards"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    module_item_id = Column(Integer, ForeignKey("module_items.id"))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User")
    module_item = relationship("ModuleItem")