from application.dll.db.db import session
from application.dll.models import ProductStored


def get_all_product_storages():
    return session.query(ProductStored).all()


def get_specific_product_storages(idproduct_stored=None, product_stored=None, product_min_limit=None, products_max_limit=None, Storage_idstorage=None):
    d = {idproduct_stored:ProductStored.idproduct_stored, product_stored:ProductStored.product_stored, product_min_limit:ProductStored.product_min_limit, products_max_limit:ProductStored.products_max_limit, Storage_idstorage:ProductStored.Storage_idstorage}
    keys = [d[key]==key for key in d if key != None]
    return session.query(ProductStored).filter(*keys).all()


def create_product_storages(product_storages):
    product_storages = ProductStored(**product_storages)
    session.add(product_storages)
    session.commit()
