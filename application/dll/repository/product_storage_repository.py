from application.dll.db.db import session
from application.dll.models import ProductStored


def get_all_product_storages():
    return session.query(ProductStored).all()


def create_product_storages(product_storages):
    product_storages = ProductStored(**product_storages)
    session.add(product_storages)
    session.commit()
