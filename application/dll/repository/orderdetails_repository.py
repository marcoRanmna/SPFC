from application.dll.db.db import session
from application.dll.models import Orderdetail


def get_all_orderdetails():
    return session.query(Orderdetail).all()


def create_orderdetails(orderdetail):
    orderdetail = Orderdetail(**orderdetail)
    session.add(orderdetail)
    session.commit()
