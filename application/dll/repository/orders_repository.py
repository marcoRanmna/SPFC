from application.dll.db.db import session
from application.dll.models.order import Order


def get_all_orders():
    return session.query(Order).all()


def create_orders(orders):
    orders = Order(**orders)
    session.add(orders)
    session.commit()
