import unittest
from rest_structure import app

class HelloWorldTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello_endpoint(self):
        response = self.client.get("/hello")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, World!"})

if __name__ == "__main__":
    unittest.main()
