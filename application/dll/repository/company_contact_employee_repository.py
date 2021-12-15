from application.dll.db.db import session
from application.dll.models import CompanyContactEmployee


def get_all_company_contact_employees():
    return session.query(CompanyContactEmployee).all()


def create_company_contact_employees(company_contact_employees):
    company_contact_employees = CompanyContactEmployee(Company_idContactPersons=company_contact_employees['Company_idContactPersons'],first_name=company_contact_employees['first_name'],last_name=company_contact_employees['last_name'],phone=company_contact_employees['phone'],email=company_contact_employees['email'])
    session.add(company_contact_employees)
    session.commit()
