from application.dll.models import ProductHasManufacture
from application.dll.db.db import session


def get_all_products_has_manufactures():
    return session.query(ProductHasManufacture).all()


def get_specific_products_has_manufactures(Products_idProducts=None, Manufactures_idManufactures=None, purchase_price=None, quality_rating=None):
    d = {Products_idProducts:ProductHasManufacture.Products_idProducts, Manufactures_idManufactures:ProductHasManufacture.Manufactures_idManufactures, purchase_price:ProductHasManufacture.purchase_price, quality_rating:ProductHasManufacture.quality_rating}
    keys = [d[key]==key for key in d if key != None]
    return session.query(ProductHasManufacture).filter(*keys).all()


def create_products_has_manufactures(products_has_manufacture):
    products_has_manufacture = ProductHasManufacture(**products_has_manufacture)
    session.add(products_has_manufacture)
    session.commit()
