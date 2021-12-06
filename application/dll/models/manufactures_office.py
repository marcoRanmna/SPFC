from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from application.dll.db.db import Base


class ManufactureOffice(Base):
    __tablename__ = 'Manufactures_offices'

    idManufactures_offices = Column(Integer, primary_key=True)
    phone = Column(String(45), nullable=False, unique=True)
    adress = Column(String(45), nullable=False)
    country = Column(String(45), nullable=False)
    zipcode = Column(String(45), nullable=False)
    state = Column(String(45), nullable=False)
    Manufactures_idManufactures = Column(Integer, ForeignKey('Manufactures.idManufactures'))

    manufactures = relationship('Manufacture', back_populates='office')

    def __repr__(self):
        return f'{self.idManufactures_offices},{self.phone}, {self.adress}, {self.country}, {self.zipcode}, {self.state}'

