from application.dll.db.db import session
from application.dll.models import Storage


def get_all_storage():
    return session.query(Storage).all()


def get_specific_storage(idstorage=None, adress=None, zipcode=None, city=None, state=None, country=None):
    d = {idstorage:Storage.idstorage, adress:Storage.adress, zipcode:Storage.zipcode, city:Storage.city, state:Storage.state, country:Storage.country}
    keys = [d[key]==key for key in d if key != None]
    return session.query(Storage).filter(*keys).all()


def create_storage(storage):
    #storage_facility = Storage(adress=storage['address'], zipcode=storage['zipcode'], city=storage['city'], state=storage['state'], country=storage['country'])
    storage_facility = Storage(**storage)
    session.add(storage_facility)
    session.commit()

