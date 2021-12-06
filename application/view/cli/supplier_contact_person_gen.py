from application.bll.supplier_contact_person_controller import get_all_supplier_contact_person, create_supplier_contact_person


def view_supplier_contact_person():
    supplier_contact_persons = get_all_supplier_contact_person()
    print("***********")
    print("All Supplier_contact_persons")
    print("***********")
    print()
    for supplier_contact_person in supplier_contact_persons:
        print(supplier_contact_person)


def add_supplier_contact_person():
    supplier_contact_person = {
        'first_name': '',
        'last_name': '',
        'phone': '',
        'email': '',
    }
    create_supplier_contact_person(supplier_contact_person)
