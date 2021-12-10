from application.dll.db.db import session
from application.dll.models import Employee, Office


def get_all_employees():
    return session.query(Employee).all()


def create_employees(employees):
    office = session.query(Office).filter_by(office_name="MegaSort").one()
    employees = Employee(first_name=employees['first_name'], 
                            last_name=employees['last_name'], 
                            email=employees['email'], 
                            phone=employees['phone'], 
                            Jobtitle=employees['jobtitle'], 
                            offices_idoffices=office.idoffices)
    session.add(employees)
    session.commit()
