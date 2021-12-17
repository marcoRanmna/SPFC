from application.dll.repository import product_repository as product_r


def get_all_products():
    return product_r.get_all_products()


def get_specific_products():
    return product_r.get_specific_products()


def create_products(product):
    product_r.create_products(product)
