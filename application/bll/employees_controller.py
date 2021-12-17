from application.dll.repository import employees_repository as employees_r


def get_all_employees():
    return employees_r.get_all_employees()

def get_specific_employees(idEmployees=None, first_name=None, last_name=None, email=None, phone=None, Jobtitle=None, offices_idoffices=None):
    return employees_r.get_specific_employees(idEmployees, first_name, last_name, email, phone, Jobtitle, offices_idoffices)

def create_employees(employees):
    employees_r.create_employees(employees)
