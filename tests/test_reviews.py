"""
Tests for reviews endpoints
"""

from fastapi.testclient import TestClient

from app.main import app


def test_get_reviews():
    """Test getting all reviews"""
    with TestClient(app) as client:
        # Request to the endpoint
        response = client.get("reviews/")

        # Asserts that the response status code is 200
        assert response.status_code == 200


def test_get_review():
    """Test getting a specific review"""
    with TestClient(app) as client:
        # First, get the list to find a valid ID
        list_response = client.get("/reviews")
        reviews = list_response.json()

        if reviews:
            review_id = reviews[0]["id"]
            response = client.get(f"/reviews/{review_id}")
            assert response.status_code == 200
        else:
            print("No reviews found to test individual GET")
