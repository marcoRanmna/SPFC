from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from application.dll.db.db import Base


class ProductHasManufacture(Base):
    __tablename__ = 'Products_has_Manufactures'

    Product_idProducts = Column(Integer, ForeignKey('Product.idProducts'), primary_key=True)
    Manufactures_idManufactures = Column(Integer, ForeignKey('Manufactures_idManufactures'), primary_key=True)
    purchase_price = Column(Float, nullable=False)
    quality_rating = Column(Integer, nullable=True)
    manufacture = relationship('Manufacture', back_populates='product_has_manufacture')
    product = relationship('Product', back_populates='product_has_product')
