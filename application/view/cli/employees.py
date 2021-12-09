import csv
from os import path
from application.bll.employees_controller import get_all_employees, create_employees


def view_employees():
    employees = get_all_employees()
    print("*"*10,"\nAll Offices\n"+"*"*10,"\n" )
    for employee in employees:
        print(employee)


def add_employees(employees):
    #employees = {
    #    'first_name': '',
    #    'last_name': '',
    #    'email': '',
    #    'phone': '',
    #    'Jobtitle': ''
    #}
    create_employees(employees)


def delete_record():
    pass


def test_add_employees():
    dir_path = "/home/victor/Documents/SPFC/application/dll/repository/dbvolume/"
    file_person = dir_path + "person.csv"
    print(file_person, path.exists(file_person))

    with open(file_person, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        person_ls = next(csv_reader)
    person_ls = [clean.strip() for clean in person_ls]

    employees = {
        'first_name': person_ls[0],
        'last_name': person_ls[1],
        'email': person_ls[2],
        'phone': person_ls[3],
        'jobtitle': 'Seller'
    }

    print(employees)
    add_employees(employees)

if __name__ == '__main__':
    #test_add_employees()
    view_employees()
