from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from application.dll.db.db import Base


class CarInfo(Base):
    __tablename__ = 'Carinfo'

    idCarinfo = Column(Integer, primary_key=True)
    reg_number = Column(String(15), nullable=False)
    manufacture_name = Column(String(45), nullable=False)
    model = Column(String(45), nullable=False)
    year_model = Column(DateTime, nullable=False)
    color = Column(String(45), nullable=False)
    Customers_idCustomers = Column(Integer, ForeignKey('Customers.idCustomers'))

    def __repr__(self):
        return f'{self.reg_number}, {self.manufacture_name}, {self.model}, {self.year_model}, {self.color}'
