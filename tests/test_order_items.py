"""
Tests for order_items endpoints
"""

from fastapi.testclient import TestClient

from app.main import app


def test_get_order_items():
    """Test getting all order_items"""
    with TestClient(app) as client:
        # Request to the endpoint
        response = client.get("order_items/")

        # Asserts that the response status code is 200
        assert response.status_code == 200


def test_get_order_item():
    """Test getting a specific order_item"""
    with TestClient(app) as client:
        # First, get the list to find a valid ID
        list_response = client.get("/order_items")
        items = list_response.json()

        if items:
            item_id = items[0]["id"]
            response = client.get(f"/order_items/{item_id}")
            assert response.status_code == 200
        else:
            print("No order items found to test individual GET")
