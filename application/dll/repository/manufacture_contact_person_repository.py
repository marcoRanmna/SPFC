from application.dll.models import ManufactureContactPerson
from application.dll.db.db import session


def get_all_manufacture_contact_person():
    return session.query(ManufactureContactPerson).all()


def create_manufacture_contact_person(manufacture_contact_person):
    print(manufacture_contact_person['phone_number'], manufacture_contact_person['first_name'], manufacture_contact_person['last_name'], manufacture_contact_person['email'])
    manufacture_contact_person = ManufactureContactPerson(phone_number=manufacture_contact_person['phone_number'], first_name=manufacture_contact_person['first_name'], last_name=manufacture_contact_person['last_name'], email=manufacture_contact_person['email'])
    session.add(manufacture_contact_person)
    session.commit()