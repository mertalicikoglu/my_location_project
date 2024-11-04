from .celery import celery_app
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import models

@celery_app.task
def save_location_task(location_data):
    db: Session = SessionLocal()
    db_location = models.Location(**location_data)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    db.close()
    return {"status": "Location saved"}
