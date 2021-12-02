from application.dll.db.db import session
from application.dll.models.orderdetail import Orderdetail


def get_all_orders():
    return session.query(Orderdetail).all()
