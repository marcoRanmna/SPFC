from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from application.dll.db.db import Base


class CompanyContactEmployee(Base):
    __tablename__ = 'company_contact_employees'

    idcompany_contact_employees = Column(Integer, primary_key=True, autoincrement=True)
    Company_idContactPersons = Column(Integer, ForeignKey('Company.idContactPerson'), nullable=False)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)

    companies = relationship('Company', back_populates='company_contact_employees')

    def __repr__(self):
        return f'{self.first_name}, {self.last_name}, {self.phone}, {self.email}'
