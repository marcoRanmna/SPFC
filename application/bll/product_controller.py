from application.dll.repository import product_repository as product_r


def get_all_products():
    return product_r.get_all_products()

def get_specific_products(idProducts=None, product_name=None, product_number=None, description=None, sell_price=None, product_stored_idproduct_stored=None, component_model_idcomponent_model=None):
    return product_r.get_specific_products(idProducts, product_name, product_number, description, sell_price, product_stored_idproduct_stored, component_model_idcomponent_model)


def create_products(product):
    product_r.create_products(product)
