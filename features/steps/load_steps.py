from behave import given
from service.models import db, Product

@given('the database is initialized with the following products')
def step_impl(context):
    db.session.query(Product).delete()  

    for row in context.table:
        product = Product(
            name=row['name'],
            category=row['category'],
            description=row['description'],
            price=float(row['price']),
            available=row['available'].lower() == 'true'
        )
        db.session.add(product)
    
    db.session.commit()
