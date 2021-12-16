from application.dll.db.db import session
from application.dll.models import Office


def get_all_offices():
    return session.query(Office).all()


def get_specific_offices(idoffices=None, office_name=None, city=None, phone_number=None, adress=None, state=None, country=None, zipcode=None, Storage_idOffice_storage=None):
    d = {idoffices:Office.idoffices, office_name:Office.office_name, city:Office.city, phone_number:Office.phone_number, adress:Office.adress, state:Office.state, country:Office.country, zipcode:Office.zipcode, Storage_idOffice_storage:Office.Storage_idOffice_storage}
    keys = [d[key]==key for key in d if key != None]
    return session.query(Office).filter(*keys).all()


def create_offices(offices):
    offices = Office(**offices)
    session.add(offices)
    session.commit()
