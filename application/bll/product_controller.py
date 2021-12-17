from application.dll.repository import product_repository as product_r
from application.mongo_dll.repository import product_repository
from application.bll import mongo_or_mysql


def get_all_products():
    if mongo_or_mysql == False:
        return product_r.get_all_products()
    else:
        return product_repository.get_all_products()


def get_specific_products(idProducts=None, product_name=None, product_number=None, description=None, sell_price=None, product_stored_idproduct_stored=None, component_model_idcomponent_model=None):
    if mongo_or_mysql == False:
        return product_r.get_specific_products(idProducts, product_name, product_number, description, sell_price, product_stored_idproduct_stored, component_model_idcomponent_model)
    else:
        return product_repository.find_products(product_name)

def create_products(product):
    if mongo_or_mysql == False:
        product_r.create_products(product)
    else:
        product_repository.create_products(product)
