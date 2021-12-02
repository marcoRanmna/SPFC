from application.dll.models.product import Product
from db import session


def get_all_products():
    return session.query(Product).all()


def create_products(product):
    product = Product(**product)
    session.add(product)
    session.commit()
