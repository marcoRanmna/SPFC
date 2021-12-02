from application.dll.db.db import session
from application.dll.models.orderdetail import Orderdetail


def get_all_orders():
    return session.query(Orderdetail).all()


def create_orderdetails(orderdetail):
    orderdetail = Orderdetail(**orderdetail)
    session.add(orderdetail)
    session.commit()
