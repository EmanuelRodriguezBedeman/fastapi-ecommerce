"""
Tests for product endpoints
"""

from fastapi.testclient import TestClient

from app.main import app


def test_get_products():
    """Test getting all products"""

    with TestClient(app) as client:
        # Request to the endpoint
        response = client.get("products/")

        # Asserts that the response status code is 200
        assert response.status_code == 200


def test_get_product():
    """Test getting a specific product"""

    with TestClient(app) as client:
        # First, get the list to find a valid ID
        list_response = client.get("/products")
        products = list_response.json()

        if products:
            product_id = products[0]["id"]
            response = client.get(f"/products/{product_id}")
            assert response.status_code == 200
        else:
            print("No products found to test individual GET")
