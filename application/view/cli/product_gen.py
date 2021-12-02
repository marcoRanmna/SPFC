from application.bll.product_controller import get_all_products, create_products


def view_product():
    products = get_all_products()
    print("***********")
    print("All Product")
    print("***********")
    print()
    for product in products:
        print(product)


def add_products():
    product = {
        'product_name': '',
        'product_number': '',
        'description': '',
        'sell_price': ''
    }
    create_products(product)
