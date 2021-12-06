from application.dll.repository import product_has_manufacture_repository as product_has_manufacture_r


def get_all_product_has_manufacture():
    return product_has_manufacture_r.get_all_products_has_manufactures()


def create_product_has_manufacture(product_has_manufacture):
    product_has_manufacture_r.create_products_has_manufactures(product_has_manufacture)