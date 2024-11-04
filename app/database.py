import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# configure to use a different database for testing
if os.getenv("TESTING"):
    SQLALCHEMY_DATABASE_URL = "postgresql://myuser:mypassword@db/location_data_test"
else:
    SQLALCHEMY_DATABASE_URL = "postgresql://myuser:mypassword@db/location_data"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
