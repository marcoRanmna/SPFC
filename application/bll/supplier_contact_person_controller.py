from application.dll.repository import supplier_contact_person_repository as supplier_contact_person_r


def get_all_supplier_contact_person():
    return supplier_contact_person_r.get_all_supplier_contact_person()


def create_supplier_contact_person(supplier_contact_person):
    supplier_contact_person_r.create_supplier_contact_person(supplier_contact_person)
