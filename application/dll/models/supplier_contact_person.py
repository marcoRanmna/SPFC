from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from application.dll.db.db import Base


class SupplierContactPerson(Base):
    __tablename__ = 'Supplier_contactperson'

    idSupplier_contactperson = Column(Integer, primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)

    Suppliers_idSuppliers = Column(Integer, ForeignKey('Suppliers_idSuppliers'))
    suppliers = relationship('Suppliers', back_populates='supplier_contact_person')

    def __repr__(self):
        return f'{self.idSupplier_contactperson},{self.first_name}, {self.last_name}, {self.phone}, {self.email}'
