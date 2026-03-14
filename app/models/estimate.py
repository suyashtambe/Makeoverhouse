from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.database import Base
import datetime

class Estimate(Base):
    __tablename__ = "estimates"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=True)
    total_cost = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)