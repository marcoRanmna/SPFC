from application.dll.db.db import session
from application.dll.models import DeliveryAdress


def get_all_delivery_adress():
    return session.query(DeliveryAdress).all()


def create_delivery_adress(delivery_adress):
    delivery_adress = DeliveryAdress(**delivery_adress)
    session.add(delivery_adress)
    session.commit()
