from application.dll.db.db import session
from application.dll.models import DeliveryAdress


def get_all_delivery_adress():
    return session.query(DeliveryAdress).all()


def get_specific_delivery_adress(iddelivery_adress=None, country=None, city=None, state=None, zipcode=None, adress=None):
    d = {iddelivery_adress:DeliveryAdress.iddelivery_adress, country:DeliveryAdress.country, city:DeliveryAdress.city, state:DeliveryAdress.state, zipcode:DeliveryAdress.zipcode, adress:DeliveryAdress.adress}
    keys = [d[key]==key for key in d if key != None]
    return session.query(DeliveryAdress).filter(*keys).all()


def create_delivery_adress(delivery_adress):
    delivery_adress = DeliveryAdress(**delivery_adress)
    session.add(delivery_adress)
    session.commit()
