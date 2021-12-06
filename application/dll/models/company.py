from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from application.dll.db.db import Base


class Company(Base):
    __tablename__ = 'Company'

    idContactPersons = Column(Integer, primary_key=True)
    company_name = Column(String(45), nullable=False)
    phone_number = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)

    company_contact_employees = relationship('CompanyContactEmployee', back_populates='companies')
    customers = relationship('Customer', back_populates='companies')

    def __repr__(self):
        return f'{self.company_name}, {self.phone_number}, {self.email}'
