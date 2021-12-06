from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from application.dll.db.db import Base


class Manufacture(Base):
    __tablename__ = 'Manufactures'

    idManufactures = Column(Integer, primary_key=True)
    company_name = Column(String(45), nullable=False, unique=True)
    number_head_office = Column(Integer, nullable=True)

    product_has_manufacture = relationship('ProductHasManufacture', back_populates='manufacture')

    office = relationship('ManufactureOffice', backpopulates='manufactures')

    def __repr__(self):
        return f'{self.idManufactures},{self.company_name}, {self.number_head_office}'
