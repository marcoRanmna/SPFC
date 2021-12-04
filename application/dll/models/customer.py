from sqlalchemy import Column, Integer, DATE, ForeignKey
from sqlalchemy.orm import relationship

from application.dll.models.company_customer import CompanyCustomer
from application.dll.models.private_customer import PrivatePerson
from application.dll.db.db import Base


class Costumer(Base):
    __tablename__ = 'Customers'

    customer_id = Column(Integer, primary_key=True)
    created = Column(DATE, nullable=False)
    private_person_or_company = Column(TINYINT=PrivatePerson and CompanyCustomer, nullable=False)

    idprivate_person = Column(Integer, ForeignKey('private_person_idprivate_person'))

    idContactPersons = Column(Integer, ForeignKey('idContactPersons'))

    def __repr__(self):
        return f'{self.customer_id}, {self.created}'
