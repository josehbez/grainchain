from fastapi.testclient import TestClient
import unittest
from app import app

class TestApp(unittest.TestCase):

  def setUp(self):
    self.client = TestClient(app)
  
  def test_index(self):
    request = self.client.get("/")
    assert request.status_code == 200, "Invalid HTTP status code"
    assert request.json()["Hello"] == "World", "Expected 'Hello': 'World'"

    # Post testing user
    user = {
        "name":     "Test User",
        "username": "test",
        "location": "Main Office"
    }
    request = self.client.post("http://localhost:8022/user", json=user)
    assert request.status_code == 200, "Invalid HTTP status code"
    user = request.json()
    assert user["name"]             == "Test User",   "Invalid name"
    assert user["username"]         == "test",        "Invalid username"
    assert user["location"]         == "Main Office", "Invalid location"
    print("Test passed!")

if __name__ == "__main__":
    unittest.main()


