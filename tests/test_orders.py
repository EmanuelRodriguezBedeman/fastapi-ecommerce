"""
Tests for order endpoints
"""

from fastapi.testclient import TestClient

from app.main import app


def test_get_orders():
    """Test getting all orders"""

    with TestClient(app) as client:
        # Request to the endpoint
        response = client.get("orders/")

        # Asserts that the response status code is 200
        assert response.status_code == 200


def test_get_order():
    """Test getting a specific order"""

    with TestClient(app) as client:
        # First, get the list to find a valid ID
        list_response = client.get("/orders")
        orders = list_response.json()

        if orders:
            order_id = orders[0]["id"]
            response = client.get(f"/orders/{order_id}")
            assert response.status_code == 200
        else:
            print("No orders found to test individual GET")
