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


if __name__ == '__main__':
    get_all_products()
    find_products('')