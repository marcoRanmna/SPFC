from sqlalchemy import Column, Integer, String, ForeignKey

from db import Base


class CompanyContactEmployee(Base):
    __tablename__ = 'company_contact_employees'

    idcompany_contact_employees = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)
    idContactPersons = Column(Integer, ForeignKey('idContactPersons'))

    def __repr__(self):
        return f'{self.idcompany_contact_employees}, {self.first_name}, {self.last_name}, {self.phone}, {self.email}'