from sqlalchemy import Column, Integer, String, ForeignKey

from db import Base


class Supplier(Base):
    __tablename__ = 'Suppliers'

    idSuppliers = Column(Integer, primary_key=True)
    company_name = Column(String(45), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(45), nullable=False)
    country = Column(String(45), nullable=False)
    zipcode = Column(String(45), nullable=False)
    city = Column(String(45), nullable=False)
    adress = Column(String(100), nullable=False)
    idProducts = Column(Integer, ForeignKey('idProducts'))

    def __repr__(self):
        return f'{self.idSuppliers},{self.company_name}, {self.email}, {self.phone}, {self.country} {self.zipcode}, {self.adress}'