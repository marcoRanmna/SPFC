from application.dll.db.db import session
from application.dll.models.storage import Storage


def get_all_storage():
    return session.query(Storage).all()


def create_storage(storage):
    print(1,storage['address'], storage['zipcode'], storage['city'], storage['state'], storage['country'])
    stroage_facility = Storage(idstorage=1, adress=storage['address'], zipcode=storage['zipcode'], city=storage['city'], state=storage['state'], country=storage['country'])
    session.add(stroage_facility)
    session.commit()

