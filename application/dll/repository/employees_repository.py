from application.dll.db.db import session
from application.dll.models.employees import Employees


def get_all_employees():
    return session.query(Employees).all()


def create_employees(employees):
    employees = Employees(**employees)
    session.add(employees)
    session.commit()
