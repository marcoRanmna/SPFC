from application.dll.models.product import Product
from db import session


def get_all_products():
    return session.query(Product).all()
