from application.bll.product_controller import get_all_products


def view_product():
    products = get_all_products()
    print("***********")
    print("All Product")
    print("***********")
    print()
    for product in products:
        print(product)
        