from application.dll.models import SupplierContactPerson
from application.dll.db.db import session


def get_all_supplier_contact_person():
    return session.query(SupplierContactPerson).all()


def get_specific_supplier_contact_person(idSupplier_contactperson=None, first_name=None, last_name=None, phone=None, email=None, Suppliers_idSuppliers=None):
    d = {idSupplier_contactperson:SupplierContactPerson.idSupplier_contactperson, first_name:SupplierContactPerson.first_name, last_name:SupplierContactPerson.last_name, phone:SupplierContactPerson.phone, email:SupplierContactPerson.email, Suppliers_idSuppliers:SupplierContactPerson.Suppliers_idSuppliers}
    keys = [d[key]==key for key in d if key != None]
    return session.query(SupplierContactPerson).filter(*keys).all()


def create_supplier_contact_person(supplier_contact_person):
    #print(supplier_contact_person['first_name'], supplier_contact_person['last_name'], supplier_contact_person['phone'], supplier_contact_person['email'])
    #supplier_contact_person = SupplierContactPerson(first_name=supplier_contact_person['first_name'], last_name=supplier_contact_person['last_name'], phone=supplier_contact_person['phone'], email=supplier_contact_person['email'])
    supplier_contact_person = SupplierContactPerson(**supplier_contact_person)
    session.add(supplier_contact_person)
    session.commit()
