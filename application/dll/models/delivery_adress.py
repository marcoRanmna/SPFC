from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from application.dll.db.db import Base


class Delivery_adress(Base):
    __tablename__ = 'delivery_adress'

    iddelivery_adress = Column(Integer, primary_key=True)
    country = Column(String(45), nullable=False)
    city = Column(String(45), nullable=False)
    state = Column(String(45), nullable=False)
    zipcode = Column(String(45), nullable=False)
    adress = Column(String(45), nullable=False)

    customers = relationship('Customer', back_populates='delivery_addresses')

    def __repr__(self):
        return f'{self.country} {self.city}, {self.state}, {self.zipcode}, {self.adress}'