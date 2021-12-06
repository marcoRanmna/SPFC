from application.bll.manufacture_contact_person_controller import get_all_manufacture_contact_person, create_manufacture_contact_person


def view_manufacture_contact_person():
    manufacture_contact_persons = get_all_manufacture_contact_person()
    print("***********")
    print("All Manufacture_contact_person")
    print("***********")
    print()
    for manufacture_contact_person in manufacture_contact_persons:
        print(manufacture_contact_person)


def add_manufacture_contact_person():
    manufacture_contact_person = {
        'phone_number': '',
        'first_name': '',
        'last_name': '',
        'email': '',
    }
    create_manufacture_contact_person(manufacture_contact_person)
