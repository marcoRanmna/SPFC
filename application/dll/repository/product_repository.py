from application.dll.models import Product
from application.dll.db.db import session


def get_all_products():
    return session.query(Product).all()


def get_specific_products(idProducts=None, product_name=None, product_number=None, description=None, sell_price=None, product_stored_idproduct_stored=None, component_model_idcomponent_model=None):
    d = {idProducts:Product.idProducts, product_name:Product.product_name, product_number:Product.product_number, description:Product.description, sell_price:Product.sell_price, product_stored_idproduct_stored:Product.product_stored_idproduct_stored, component_model_idcomponent_model:Product.component_model_idcomponent_model}
    keys = [d[key]==key for key in d if key != None]
    return session.query(Product).filter(*keys).all()


def create_products(product):
    #print(product['product_name'], product['product_number'], product['description'], product['sell_price'])
    #product = Product(product_name=product['product_name'], product_number=product['product_number'], description=product['description'], sell_price=product['sell_price'])
    product = Product(**product)
    session.add(product)
    session.commit()
