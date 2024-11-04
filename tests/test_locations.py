import os
import pytest
from fastapi.testclient import TestClient
from app.main import app

os.environ["TESTING"] = "True"

# set up the test client for FastAPI
client = TestClient(app)

# Test to get all locations from the database
def test_get_locations():
    response = client.get("/locations/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
