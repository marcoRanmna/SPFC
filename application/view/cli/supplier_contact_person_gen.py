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
        'first_name': 'Magnus',
        'last_name': 'Svensson',
        'phone': '0707133701',
        'email': 'magnus@email.com',
        'Suppliers_idSuppliers': 1
    }
    create_supplier_contact_person(supplier_contact_person)


if __name__ == '__main__':
    add_supplier_contact_person()
