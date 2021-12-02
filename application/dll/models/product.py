from sqlalchemy import Column, Integer, String, CHAR, Float, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class Product(Base):
    __tablename__ = 'products'

    idProducts = Column(Integer, primary_key=True)
    product_name = Column(String(100), nullable=False)
    product_number = Column(CHAR(10), nullable=False, unique=True)
    description = Column(Mediumtext, nullable=True)
    sell_price = Column(Float, nullable=False)
    idcomponent_model = Column(Integer, ForeignKey('idcomponent_model'))
    component_model = relationship('CarModel', backpolulates='product')

    def __repr__(self):
        return f'{self.idProducts},{self.product_name}, {self.product_number}, {self.description}, {self.sell_price}'
