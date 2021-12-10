from application.dll.db.db import session
from application.dll.models.ourcompany import Storage


def get_all_storage():
    return session.query(Storage).all()


def create_storage(storage):
    storage_facility = Storage(adress=storage['address'], zipcode=storage['zipcode'], city=storage['city'], state=storage['state'], country=storage['country'])
    session.add(storage_facility)
    session.commit()

