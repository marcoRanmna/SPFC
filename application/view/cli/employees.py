from application.bll.employees_controller import get_all_employees, create_employees


def view_employees():
    employees = get_all_employees()
    print("***********")
    print("All Employees")
    print("***********")
    print()
    for employee in employees:
        print(employee)


def add_employees():
    employees = {
        'first_name': '',
        'last_name': '',
        'email': '',
        'phone': '',
        'Jobtitle': ''
    }
    create_employees(employees)


def delete_record():
    pass