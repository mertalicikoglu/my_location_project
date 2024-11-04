from sqlalchemy.orm import Session
from . import models, schemas

# Create location
def create_location(db: Session, location: schemas.LocationCreate):
    db_location = models.Location(**location.dict())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

# Get location
def get_location(db: Session, location_id: int):
    return db.query(models.Location).filter(models.Location.id == location_id).first()

# Get locations
def get_locations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Location).offset(skip).limit(limit).all()
