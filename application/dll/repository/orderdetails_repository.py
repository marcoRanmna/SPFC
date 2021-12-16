from application.dll.db.db import session
from application.dll.models import Orderdetail


def get_all_orderdetails():
    return session.query(Orderdetail).all()


def get_specific_orderdetails(idOrderdetails=None, product_number=None, quantityprdered=None, price=None, Orders_idOrders=None, Orders_Customers_idCustomers=None):
    d = {idOrderdetails:Orderdetail.idOrderdetails, product_number:Orderdetail.product_number, quantityprdered:Orderdetail.quantityordered, price:Orderdetail.price, Orders_idOrders:Orderdetail.Orders_idOrders, Orders_Customers_idCustomers:Orderdetail.Orders_Customers_idCustomers}
    keys = [d[key]==key for key in d if key != None]
    return session.query(Orderdetail).filter(*keys).all()


def create_orderdetails(orderdetail):
    orderdetail = Orderdetail(**orderdetail)
    session.add(orderdetail)
    session.commit()
