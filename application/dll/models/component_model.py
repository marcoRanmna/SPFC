from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class CarModel(Base):
    __tablename__ = 'component_model'

    idcomponent_model = Column(Integer, primary_key=True)
    car_brand = Column(String(45), nullable=False)
    car_model = Column(String(45), nullable=False)
    car_model_year = Column(Year, nullable=True)
    product = relationship('Product', backpopulates='component_model')

    def __repr__(self):
        return f'{self.car_brand}, {self.car_model}, {self.car_model_year}'

