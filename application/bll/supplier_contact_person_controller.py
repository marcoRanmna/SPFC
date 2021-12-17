from application.dll.repository import supplier_contact_person_repository as supplier_contact_person_r


def get_all_supplier_contact_person():
    return supplier_contact_person_r.get_all_supplier_contact_person()

def get_specific_supplier_contact_person(idSupplier_contactperson=None, first_name=None, last_name=None, phone=None, email=None, Suppliers_idSuppliers=None):
    return supplier_contact_person_r.get_specific_supplier_contact_person(idSupplier_contactperson, first_name, last_name, phone, email, Suppliers_idSuppliers)

def create_supplier_contact_person(supplier_contact_person):
    supplier_contact_person_r.create_supplier_contact_person(supplier_contact_person)
