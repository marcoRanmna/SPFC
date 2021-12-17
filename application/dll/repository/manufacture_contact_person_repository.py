from application.dll.models import ManufactureContactPerson
from application.dll.db.db import session


def get_all_manufacture_contact_person():
    return session.query(ManufactureContactPerson).all()


def get_specific_manufacture_contact_person(idManufactures_contact_person=None, phone_number=None, first_name=None, last_name=None, email=None, Manufactures_idManufactures=None, Manufactures_offices_idManufactures_offices=None):
    d = {idManufactures_contact_person:ManufactureContactPerson.idManufactures_contact_person, phone_number:ManufactureContactPerson.phone_number, first_name:ManufactureContactPerson.first_name, last_name:ManufactureContactPerson.last_name, email:ManufactureContactPerson.email, Manufactures_idManufactures:ManufactureContactPerson.Manufactures_idManufactures, Manufactures_offices_idManufactures_offices:ManufactureContactPerson.Manufactures_offices_idManufactures_offices}
    keys = [d[key]==key for key in d if key != None]
    return session.query(ManufactureContactPerson).filter(*keys).all()


def create_manufacture_contact_person(manufacture_contact_person):
    manufacture_contact_person = ManufactureContactPerson(**manufacture_contact_person)
    session.add(manufacture_contact_person)
    session.commit()
