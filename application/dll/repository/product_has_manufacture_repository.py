from application.dll.models import ProductHasManufacture
from application.dll.db.db import session


def get_all_products_has_manufactures():
    return session.query(ProductHasManufacture).all()


def create_products_has_manufactures(products_has_manufacture):
    # supplier = Supplier(**supplier)
    print(products_has_manufacture['purchase_price'], products_has_manufacture['quality_rating'])
    products_has_manufacture = ProductHasManufacture(purchase_price=products_has_manufacture['purchase_price'], quality_rating=products_has_manufacture['quality_rating'])
    session.add(products_has_manufacture)
    session.commit()
