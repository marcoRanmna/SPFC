from application.view.mongo.mongo_models import Product


def get_all_products():
    products = Product.all()
    for product in products:
        print(product)
        return product

def find_products(product_name):
    products = Product.collection.find({'product_name': product_name})
    for product in products:
        print(product)
        return product

def create_products(product_name=None, product_number=None, description=None, sell_price=None, product_stored_idproduct_stored=None, component_model_idcomponent_model=None, product_stored=None, component_model=None, manufacture=None):
    products = Product({'product_name': product_name, 'product_number': product_number, 'description': description, "sell_price": sell_price, 'product_stored_idproduct_stored': product_stored_idproduct_stored, 'component_model_idcomponent_model': component_model_idcomponent_model, 'product_stored': product_stored, 'component_model': component_model, 'manufacture': manufacture})
    products.save()


if __name__ == '__main__':
    #get_all_products()
    #find_products('')
    product_stored = [{
        "product_stored": 1,
        "product_min_limit": 20,
        "product_max_limit": 100
    }]
    component_model = [{
        "car_brand": "Volvo",
        "car_model": "XC60",
        "car_model_year": '2020'
    }]
    manufacture = [{
        "purchase_price": 500,
        "quality_rating": 5
    }]
    create_products('Oil Filter', 'Gxba4612xa', 'filtering for oil', 1000, 1, '', product_stored, component_model, manufacture)