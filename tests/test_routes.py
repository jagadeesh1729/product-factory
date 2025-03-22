import logging
import unittest
from flask import Flask
from service.models import Product
from service.routes import app  # Assuming Flask app is in routes.py
from factories import ProductFactory

class TestProductRoutes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Initialize test client"""
        cls.app = app.test_client()
        cls.app.testing = True

    def setUp(self):
        """Runs before each test"""
        Product.remove_all()  

    def test_read_a_product(self):
        """Test case to READ a product via API"""
        product = ProductFactory()
        product.create()

        response = self.app.get(f"/products/{product.id}")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(data["id"], product.id)
        self.assertEqual(data["name"], product.name)

    def test_update_a_product(self):
        """Test case to UPDATE a product via API"""
        product = ProductFactory()
        product.create()
        original_id = product.id

        update_data = {"description": "Updated description"}
        response = self.app.put(f"/products/{product.id}", json=update_data)
        self.assertEqual(response.status_code, 200)

        updated_product = Product.find(original_id)
        self.assertEqual(updated_product.description, "Updated description")

    def test_delete_a_product(self):
        """Test case to DELETE a product via API"""
        product = ProductFactory()
        product.create()
        response = self.app.delete(f"/products/{product.id}")

        self.assertEqual(response.status_code, 204)  # No Content response
        deleted_product = Product.find(product.id)
        self.assertIsNone(deleted_product)

    def test_list_all_products(self):
        """Test case to LIST ALL products via API"""
        ProductFactory().create()
        ProductFactory().create()

        response = self.app.get("/products")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertGreaterEqual(len(data), 2)

    def test_list_by_name(self):
        """Test case to LIST BY NAME via API"""
        product = ProductFactory(name="Test Product")
        product.create()

        response = self.app.get("/products?name=Test Product")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(any(p["name"] == "Test Product" for p in data))

    def test_list_by_category(self):
        """Test case to LIST BY CATEGORY via API"""
        product = ProductFactory(category="Electronics")
        product.create()

        response = self.app.get("/products?category=Electronics")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(any(p["category"] == "Electronics" for p in data))

    def test_list_by_availability(self):
        """Test case to LIST BY AVAILABILITY via API"""
        product = ProductFactory(available=True)
        product.create()

        response = self.app.get("/products?available=true")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertTrue(any(p["available"] for p in data))

if __name__ == "__main__":
    unittest.main()
