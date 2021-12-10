from application.dll.models import Product
from application.dll.db.db import session


def get_all_products():
    return session.query(Product).all()


def create_products(product):
    print(product['product_name'], product['product_number'], product['description'], product['sell_price'])
    product = Product(product_name=product['product_name'], product_number=product['product_number'], description=product['description'], sell_price=product['sell_price'])
    session.add(product)
    session.commit()
