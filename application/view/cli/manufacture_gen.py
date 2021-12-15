import csv
from os import path

from application.bll.manufacture_controller import get_all_manufactures, create_manufactures


def view_manufacture():
    manufactures = get_all_manufactures()
    print("***********")
    print("All Manufactures")
    print("***********")
    print()
    for manufacture in manufactures:
        print(manufacture)


def add_manufacture(manufacture):
    # manufacture = {
    #     'company_name': '',
    #     'number_head_office': '',
    # }
    create_manufactures(manufacture)


def test_add_manufacture():
    dir_path = 'C:/Teknikhögskolan/SpareParts/PyCharm/application/dll/repository/data/'
    file_product = dir_path + 'company.csv'
    print(file_product, path.exists(file_product))

    with open(file_product, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        manufacture_list = next(csv_reader)
    print(manufacture_list)

    dir_path2 = 'C:/Teknikhögskolan/SpareParts/PyCharm/application/dll/repository/data/'
    file_product2 = dir_path2 + 'person.csv'
    print(file_product2, path.exists(file_product2))

    with open(file_product2, 'r', encoding='utf-8') as csvfile2:
        csv_reader2 = csv.reader(csvfile2)
        next(csv_reader2)
        phone_num_list = next(csv_reader2)
    print(phone_num_list)

    manufacture = {
        'company_name': manufacture_list[0],
        'number_head_office': 1.0
    }
    # print(manufacture)
    add_manufacture(manufacture)


if __name__ == '__main__':
    test_add_manufacture()
