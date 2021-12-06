from sqlalchemy import Column, Integer, DATE, ForeignKey
from sqlalchemy.orm import relationship

from application.dll.models.company import Company
from application.dll.models.private_customer import PrivatePerson
from application.dll.db.db import Base


class Customer(Base):
    __tablename__ = 'Customers'

    idCustomers = Column(Integer, primary_key=True)
    created = Column(DATE, nullable=False)
    private_person_or_company = Column(TINYINT=PrivatePerson and Company, nullable=False)
    Company_idContactPersons = Column(Integer, ForeignKey('Company.idContactPersons'))
    Employees_idEmployees = Column(Integer, ForeignKey('Employees.idEmployees'))
    private_person_idprivate_person = Column(Integer, ForeignKey('private_person.idprivate_person'))
    delivery_adress_iddelivery_adress = Column(Integer, ForeignKey('delivery_adress.iddelivery_adress'))

    delivery_addresses = relationship('Delivery_adress', back_populates='customers')
    companies = relationship('Company', back_populates='customers')
    orders = relationship('Order', back_populates='customers')
    private_persons = relationship('PrivatePerson', back_populates='customers')
    car_info = relationship('CarInfo', back_populates='customers')
    employees = relationship('Employee', back_populates='customers')

    def __repr__(self):
        return f'{self.customer_id}, {self.created}'
