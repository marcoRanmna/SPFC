from application.dll.db.db import session
from application.dll.models.company_contact_employees import CompanyContactEmployees


def get_all_company_contact_employees():
    return session.query(CompanyContactEmployees).all()
