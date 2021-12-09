import csv
from os import path
from application.bll.storage_controller import get_all_storage, create_storage


def view_storage():
    storages = get_all_storage()
    print("*"*10,"\nAll Storage\n"+"*"*10,"\n")
    for facility in storages:
        print(facility)

def add_storage(storage):
    #storage = {
    #    'address': '',
    #    'zipcode': '',
    #    'city': '',
    #    'state': '',
    #    'country': ''
    #}
    create_storage(storage)

def test_add_storage():
    dir_path = "/home/victor/Documents/SPFC/application/dll/repository/dbvolume/"
    file_storage = dir_path + "adresses.csv"
    print(file_storage, path.exists(file_storage))

    with open(file_storage, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        storage_ls= next(csv_reader)
    storage_ls = [clean.strip() for clean in storage_ls]

    storage = {
        'address': storage_ls[0],
        'zipcode': storage_ls[1],
        'city': storage_ls[2],
        'state': storage_ls[3],
        'country': storage_ls[4]
    }
    add_storage(storage)

if __name__ == '__main__':
    #test_add_storage()
    view_storage()
