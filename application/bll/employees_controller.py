from application.dll.repository import employees_repository as employees_r


def get_all_employees():
    return employees_r.get_all_employees()


def create_employees(employees):
    employees_r.create_employees(employees)