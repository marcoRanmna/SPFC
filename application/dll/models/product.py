from sqlalchemy import Column, Integer, String, Text, CHAR, Float, ForeignKey
from sqlalchemy.orm import relationship
<<<<<<< HEAD
=======

>>>>>>> 8a25c606e910afd4dfc8c0066b1a6dabbf342d22
from application.dll.db.db import Base


class Product(Base):
    __tablename__ = 'Products'

    idProducts = Column(Integer, primary_key=True)
    product_name = Column(String(100), nullable=False)
    product_number = Column(CHAR(10), nullable=False, unique=True)
    description = Column(String(500), nullable=True)
    sell_price = Column(Float, nullable=False)

    product_stored_idproduct_stored = Column(Integer, ForeignKey('product_stored.idproduct_stored'))
    component_model_idcomponent_model = Column(Integer, ForeignKey('component_model.idcomponent_model'))

    product_stored = relationship('Product_Stored', back_populates='product')
    component_model = relationship('CarModel', back_populates='product')

    def __repr__(self):
        return f'{self.idProducts},{self.product_name}, {self.product_number}, {self.description}, {self.sell_price}'
