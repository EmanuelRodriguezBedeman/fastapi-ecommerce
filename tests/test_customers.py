"""
Tests for customers endpoints
"""

from fastapi.testclient import TestClient

from app.main import app


def test_get_all_customers():
    """Test getting all customers"""

    with TestClient(app) as client:
        # Request to the endpoint
        response = client.get("/customers")

        # Asserts that the response status code is 200
        assert response.status_code == 200


def test_get_customer():
    """Test getting a specific customer by ID"""

    with TestClient(app) as client:
        # First, get the list to find a valid ID
        list_response = client.get("/customers")
        customers = list_response.json()

        if customers:
            customer_id = customers[0]["id"]
            response = client.get(f"/customers/{customer_id}")
            assert response.status_code == 200
        else:
            # If no customers, just skip or fail with a clear message
            print("No customers found to test individual GET")
