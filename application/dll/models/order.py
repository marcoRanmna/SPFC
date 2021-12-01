from sqlalchemy import Column, Integer, String

from application.dll.db.db import Base


class Order(Base):
    __tablename__ = 'orders'

    idOrders = Column(Integer, primary_key=True, autoincrement=True)
    Customers_idCustomers = Column(Integer, nullable=False)
    purchase_date = Column(String(50))
    requireddate = Column(String(50))
    status = Column()
    comments = Column()

    def __repr__(self):
        return f'{self.first_name} {self.last_name}, {self.email}'
