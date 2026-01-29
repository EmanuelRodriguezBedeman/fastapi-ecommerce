"""
Customer table tests
"""

from fastapi.testclient import TestClient
from app.main import app


def test_get_all_customers():
    """Test the customers endpoint returns 200 OK and correct status"""

    with TestClient(app) as client:
        # Request to the endpoint
        response = client.get("/customers")
        
        # Asserts that the response status code is 200
        assert response.status_code == 200


def test_get_customer():
    """Test customers by ID endpoint returns 200 OK and correct status"""

    with TestClient(app) as client:
        # Request to the endpoint
        response = client.get("/customers/500")
        
        # Asserts that the response status code is 200
        assert response.status_code == 200