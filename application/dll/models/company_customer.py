from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class CompanyCustomer(Base):
    __tablename__ = 'Company'

    idContactPersons = Column(Integer, primary_key=True, unique=True)
    company_name = Column(String(45), nullable=False, unique=True)
    phone_number = Column(String(45), nullable=False, unique=True)
    email = Column(String(45), nullable=True)

    def __repr__(self):
        return f'{self.idContactPersons}, {self.company_name}, {self.phone_number}, {self.email}'


