from sqlalchemy import Column, Integer, DATE, ForeignKey
from sqlalchemy.orm import relationship

from application.dll.models.company_customer import CompanyCustomer
from application.dll.models.private_customer import PrivatePerson
from application.dll.db.db import Base


class Costumer(Base):
    __tablename__ = 'Customers'

    idCustomers = Column(Integer, primary_key=True)
    created = Column(DATE, nullable=False)
    private_person_or_company = Column(TINYINT=PrivatePerson and CompanyCustomer, nullable=False)
    Company_idContactPersons = Column(Integer, ForeignKey('Company.idContactPersons'))
    Employees_idEmployees = Column(Integer, ForeignKey('Employees.idEmployees'))
    private_person_idprivate_person = Column(Integer, ForeignKey('private_person.idprivate_person'))
    delivery_adress_iddelivery_adress = Column(Integer, ForeignKey('delivery_adress.iddelivery_adress'))

    delivery_addresses = relationship('Delivery_adress', back_populates='customers')

    def __repr__(self):
        return f'{self.customer_id}, {self.created}'
