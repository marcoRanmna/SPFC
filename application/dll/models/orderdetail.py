from sqlalchemy import Column, Integer, String, ForeignKey, Float

from application.dll.db.db import Base


class Orderdetail(Base):
    __tablename__ = 'Orderdetails'

    idOrderdetails = Column(Integer, primary_key=True)
    product_number = Column(String(45), nullable=False)
    quantityordered = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    Orders_idOrders = Column(Integer, ForeignKey('Orders.idOrders'), nullable=False)
    Orders_Customers_idCustomers = Column(Integer, ForeignKey('Orders.Customers.idCustomers'), nullable=False)

    def __repr__(self):
        return f'{self.product_number} {self.quantityordered}, {self.price}'
