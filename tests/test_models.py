import logging
import unittest
from models import Product  # Assuming Product is in models.py
from factories import ProductFactory  # Assuming a factory is used

class TestProductModel(unittest.TestCase):
    
    def test_read_a_product(self):
        """Test case to READ a product"""
        product = ProductFactory()  
        logging.debug(product)
        self.assertIsNone(product.id)
        product.create()
        found_product = Product.find(product.id)

        self.assertIsNotNone(found_product)
        self.assertEqual(found_product.id, product.id)
        self.assertEqual(found_product.name, product.name)
        self.assertEqual(found_product.description, product.description)
        self.assertEqual(found_product.price, product.price)

    def test_update_a_product(self):
        """Test case to UPDATE a product"""
        product = ProductFactory()
        product.create()
        original_id = product.id

        # Modify product details
        product.description = "Updated Description"
        product.update()

        updated_product = Product.find(original_id)
        self.assertEqual(updated_product.id, original_id)
        self.assertEqual(updated_product.description, "Updated Description")

    def test_delete_a_product(self):
        """Test case to DELETE a product"""
        product = ProductFactory()
        product.create()
        product_id = product.id

        product.delete()
        deleted_product = Product.find(product_id)

        self.assertIsNone(deleted_product)

    def test_list_all_products(self):
        """Test case to LIST ALL products"""
        ProductFactory().create()
        ProductFactory().create()

        products = Product.all()
        self.assertGreaterEqual(len(products), 2)  # Ensure at least two exist

    def test_find_by_name(self):
        """Test case to FIND BY NAME"""
        product = ProductFactory(name="Test Product")
        product.create()

        found_products = Product.find_by_name("Test Product")
        self.assertTrue(any(p.name == "Test Product" for p in found_products))

    def test_find_by_category(self):
        """Test case to FIND BY CATEGORY"""
        product = ProductFactory(category="Electronics")
        product.create()

        found_products = Product.find_by_category("Electronics")
        self.assertTrue(any(p.category == "Electronics" for p in found_products))

    def test_find_by_availability(self):
        """Test case to FIND BY AVAILABILITY"""
        product = ProductFactory(available=True)
        product.create()

        found_products = Product.find_by_availability(True)
        self.assertTrue(any(p.available for p in found_products))

if __name__ == "__main__":
    unittest.main()
