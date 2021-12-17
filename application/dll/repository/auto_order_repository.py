from application.dll.db.db import session
from application.dll.models import AutoOrder


def get_all_auto_order():
    return session.query(AutoOrder).all()


def delete_auto_order(auto_order):
    auto_order = AutoOrder(**auto_order)
    session.delete(auto_order)
    session.commit()
