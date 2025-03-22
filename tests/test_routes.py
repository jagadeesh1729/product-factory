def test_update_a_product(self):
    product = ProductFactory()  
    logging.debug(product)
    product.id = None
    product.create()
    logging.debug(product)

    self.assertIsNotNone(product.id)
    product.description = "testing"
    original_id = product.id
    product.update()

    updated_product = Product.find(original_id)

    self.assertIsNotNone(updated_product)
    self.assertEqual(updated_product.id, original_id)
    self.assertEqual(updated_product.description, "testing")

    products = Product.all()
    self.assertEqual(len(products), 1)
    self.assertEqual(products[0].id, original_id)
    self.assertEqual(products[0].description, "testing")
