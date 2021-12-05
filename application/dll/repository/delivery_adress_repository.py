from application.dll.db.db import session
from application.dll.models.delivery_adress import Delivery_adress


def get_all_delivery_adress():
    return session.query(Delivery_adress).all()


def create_delivery_adress(delivery_adress):
    delivery_adress = Delivery_adress(**delivery_adress)
    session.add(delivery_adress)
    session.commit()
