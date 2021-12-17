from application.dll.db.db import session
from application.dll.models import Order


def get_all_orders():
    return session.query(Order).all()


def get_specific_orders(idOrders=None, Customers_idCustomers=None, purchase_date=None, requireddate=None, shippeddate=None, status=None, comments=None, supplier_id=None):
    d = {idOrders:Order.idOrders, Customers_idCustomers:Order.Customers_idCustomers, purchase_date:Order.purchase_date, requireddate:Order.requireddate, shippeddate:Order.shippeddate, status:Order.status, comments:Order.comments, supplier_id:Order.supplier_id}
    keys = [d[key]==key for key in d if key != None]
    return session.query(Order).filter(*keys).all()


def create_orders(orders):
    orders = Order(**orders)
    session.add(orders)
    session.commit()
