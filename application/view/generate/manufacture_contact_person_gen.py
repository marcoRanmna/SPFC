import csv
from os import path

from application.bll.manufacture_contact_person_controller import get_all_manufacture_contact_person, create_manufacture_contact_person


def view_manufacture_contact_person():
    manufacture_contact_persons = get_all_manufacture_contact_person()
    print("***********")
    print("All Manufacture_contact_person")
    print("***********")
    print()
    for manufacture_contact_person in manufacture_contact_persons:
        print(manufacture_contact_person)


def add_manufacture_contact_person(manufacture_contact_person):
    # manufacture_contact_person = {
    #     'phone_number': '',
    #     'first_name': '',
    #     'last_name': '',
    #     'email': '',
    # }
    create_manufacture_contact_person(manufacture_contact_person)


def test_add_manufacture_contact_person():
    dir_path = 'C:/Python project/SPFC/application/dll/repository/dbvolume/'
    file_product = dir_path + 'person.csv'
    print(file_product, path.exists(file_product))

    with open(file_product, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        contact_person_list = next(csv_reader)
    print(contact_person_list)

    manufacture_contact_person = {
        'phone_number': '',
        'first_name': '',
        'last_name': '',
        'email': '',
    }
    # print(manufacture_contact_person)
    add_manufacture_contact_person(manufacture_contact_person)


if __name__ == '__main__':
    test_add_manufacture_contact_person()