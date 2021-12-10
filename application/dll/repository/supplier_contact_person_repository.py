from application.dll.models import SupplierContactPerson
from application.dll.db.db import session


def get_all_supplier_contact_person():
    return session.query(SupplierContactPerson).all()


def create_supplier_contact_person(supplier_contact_person):
    print(supplier_contact_person['first_name'], supplier_contact_person['last_name'], supplier_contact_person['phone'], supplier_contact_person['email'])
    supplier_contact_person = SupplierContactPerson(first_name=supplier_contact_person['first_name'], last_name=supplier_contact_person['last_name'], phone=supplier_contact_person['phone'], email=supplier_contact_person['email'])
    session.add(supplier_contact_person)
    session.commit()
