from application.dll.db.db import session
from application.dll.models import Employee


def get_all_employees():
    return session.query(Employee).all()


def get_specific_employees(idEmployees=None, first_name=None, last_name=None, email=None, phone=None, Jobtitle=None, offices_idoffices=None):
    d = {idEmployees:Employee.idEmployees, first_name:Employee.first_name, last_name:Employee.last_name, email:Employee.email, phone:Employee.phone, Jobtitle:Employee.Jobtitle, offices_idoffices:Employee.offices_idoffices}
    keys = [d[key]==key for key in d if key != None]
    return session.query(Employee).filter(*keys).all()


def create_employees(employees):
    employees = Employee(**employees)
    session.add(employees)
    session.commit()
