from sqlalchemy import Column, Integer, String, Date, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from application.dll.db.db import Base


class Order(Base):
    __tablename__ = 'Orders'

    idOrders = Column(Integer, primary_key=True)
    Customers_idCustomers = Column(Integer, ForeignKey('Customers.idCustomers'), primary_key=True)
    purchase_date = Column(DateTime, nullable=False)
    requireddate = Column(Date)
    shippeddate = Column(Date)
    status = Column(String(45), nullable=False)
    comments = Column(Text)

    customers = relationship('Customer', back_populates='orders')
    orderdetails = relationship('Orderdetail', back_populates='orders')

    def __repr__(self):
        return f'{self.purchase_date} {self.requireddate}, {self.shippeddate}, {self.status}, {self.comments}'
