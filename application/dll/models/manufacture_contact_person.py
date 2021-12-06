from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from application.dll.db.db import Base


class ManufactureContactPerson(Base):
    __tablename__ = 'Manufactures_contact_person'

    idManufactures_contact_person = Column(Integer, primary_key=True)
    phone_number = Column(String(45), nullable=False, unique=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    email = Column(String(100), nullable=False, unique=True)

    Manufactures_idManufactures = Column(Integer, ForeignKey('Manufactures_idManufactures'))
    manufactures = relationship('Manufacture', back_populates='contact_person')

    def __repr__(self):
        return f'{self.idManufactures_contact_person},{self.phone_number}, {self.first_name}, {self.last_name}, {self.email}'
