from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    speed = Column(Float)
    timestamp = Column(DateTime, nullable=False)
