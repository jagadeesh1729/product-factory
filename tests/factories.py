import factory
from factory.fuzzy import FuzzyChoice, FuzzyFloat
from models.product import Product  

class ProductFactory(factory.Factory):
    class Meta:
        model = Product  

    id = factory.Sequence(lambda n: n)  
    name = factory.Faker("word") 
    description = factory.Faker("sentence")  
    price = FuzzyFloat(10.0, 100.0)  
    stock = FuzzyChoice(choices=[True, False])  
    category = factory.Faker("word")  
    date_added = factory.Faker('date_this_decade')  
    rating = FuzzyFloat(1.0, 5.0) 
if __name__ == "__main__":
    # Create a single fake product
    fake_product = ProductFactory()

    # Print the generated fake product
    print(f"Product ID: {fake_product.id}")
    print(f"Product Name: {fake_product.name}")
    print(f"Description: {fake_product.description}")
    print(f"Price: ${fake_product.price}")
    print(f"In Stock: {fake_product.stock}")
    print(f"Category: {fake_product.category}")
    print(f"Date Added: {fake_product.date_added}")
    print(f"Rating: {fake_product.rating}")

    # Create multiple fake products
    fake_products = ProductFactory.build_batch(5)
    print("\nGenerated Products:")
    for product in fake_products:
        print(f"Product Name: {product.name}, Price: ${product.price}, In Stock: {product.stock}")
