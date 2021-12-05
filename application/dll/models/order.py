from sqlalchemy import Column, Integer, String, Date, DateTime, Text, ForeignKey

from application.dll.db.db import Base


class Order(Base):
    __tablename__ = 'Orders'

    idOrders = Column(Integer, primary_key=True)
    Customers_idCustomers = Column(Integer, primary_key=True, ForeignKey('Customers.idCustomers'), nullable=False)
    purchase_date = Column(DateTime, nullable=False)
    requireddate = Column(Date)
    shippeddate = Column(Date)
    status = Column(String(45), nullable=False)
    comments = Column(Text)

    def __repr__(self):
        return f'{self.purchase_date} {self.requireddate}, {self.shippeddate}, {self.status}, {self.comments}'
