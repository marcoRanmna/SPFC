from application.dll.db.db import session
from application.dll.models.company_contact_employees import CompanyContactEmployees


def get_all_company_contact_employees():
    return session.query(CompanyContactEmployees).all()


def create_company_contact_employees(company_contact_employees):
    company_contact_employees = CompanyContactEmployees(**company_contact_employees)
    session.add(company_contact_employees)
    session.commit()
