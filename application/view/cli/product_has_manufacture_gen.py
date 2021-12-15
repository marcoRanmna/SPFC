from application.bll.product_has_manufacture_controller import get_all_product_has_manufacture, create_product_has_manufacture


def view_product_has_manufacture():
    product_has_manufactures = get_all_product_has_manufacture()
    print("***********")
    print("All Product_has_manufacture")
    print("***********")
    print()
    for product_has_manufacture in product_has_manufactures:
        print(product_has_manufacture)


def add_product_has_manufacture():
    product_has_manufacture = {
        'Products_idProducts': 1,
        'Manufactures_idManufactures': 1,
        'purchase_price': 56,
        'quality_rating': 5
    }
    create_product_has_manufacture(product_has_manufacture)


if __name__ == '__main__':
    add_product_has_manufacture()
