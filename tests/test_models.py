def test_read_a_product(self):
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
