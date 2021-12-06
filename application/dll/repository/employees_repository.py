from application.dll.db.db import session
from application.dll.models.employees import Employee


def get_all_employees():
    return session.query(Employee).all()


def create_employees(employees):
    employees = Employee(**employees)
    session.add(employees)
    session.commit()
