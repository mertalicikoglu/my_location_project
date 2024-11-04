from pydantic import BaseModel
from datetime import datetime

class LocationBase(BaseModel):
    device_id: str
    latitude: float
    longitude: float
    speed: float
    timestamp: datetime

class LocationCreate(LocationBase):
    pass

class Location(LocationBase):
    id: int

    class Config:
        orm_mode = True
