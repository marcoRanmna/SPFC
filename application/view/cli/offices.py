from application.bll.offices_controller import get_all_offices, create_offices
import csv
from os import path

def view_offices():
    offices = get_all_offices()
    print("*"*10,"\nAll Offices\n"+"*"*10,"\n" )
    for office in offices:
        print(office)


def add_offices(offices):
    #offices = {
    #    'city': '',
    #    'phone_number': '',
    #    'adress': '',
    #    'state': '',
    #    'country': '',
    #    'zipcode': ''
    #}
    create_offices(offices)


def delete_record():
    pass

def test_add_offices():
    dir_path = "C:/Teknikhögskolan/SpareParts/PyCharm/application/dll/repository/data/"
    file_address = dir_path + "adresses.csv"
    file_phone = dir_path + "person.csv"
    print(file_address, path.exists(file_address))
    print(file_phone, path.exists(file_phone))

    with open(file_address, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        addresses_ls = next(csv_reader)
    addresses_ls = [clean.strip() for clean in addresses_ls]

    with open(file_address, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        phone_num = next(csv_reader)[-1].strip()

    addresses_ls[1] = int(addresses_ls[1].replace(" ", ""))

    offices = {
        'office_name': 'MegaSort',
        'city': addresses_ls[2],
        'phone_number': phone_num,
        'adress': addresses_ls[0],
        'state': addresses_ls[3],
        'country': addresses_ls[4],
        'zipcode': addresses_ls[1],
        'Storage_idOffice_storage': 1
    }

    print(offices)
    add_offices(offices)

if __name__ == '__main__':
    test_add_offices()
    #view_offices()
