from application.dll.db.db import session
from application.dll.models import AutoOrder


def delete_auto_order(auto_order):
    session.delete(auto_order)
    session.commit()


def get_auto_order():
    return session.query(AutoOrder).first()


if __name__ == '__main__':
    delete_auto_order(get_auto_order())
