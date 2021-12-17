from application.dll.db.db import session
from application.dll.models import CompanyContactEmployee


def get_all_company_contact_employees():
    return session.query(CompanyContactEmployee).all()


def get_specific_company_contact_employees(idcompany_contact_employees=None, Company_idContactPersons=None, first_name=None, last_name=None, phone=None, email=None):
    d = {idcompany_contact_employees:CompanyContactEmployee.idcompany_contact_employees, Company_idContactPersons:CompanyContactEmployee.Company_idContactPersons, first_name:CompanyContactEmployee.first_name, last_name:CompanyContactEmployee.last_name, phone:CompanyContactEmployee.phone, email:CompanyContactEmployee.email}
    keys = [d[key]==key for key in d if key != None]
    return session.query(CompanyContactEmployee).filter(*keys).all()


def create_company_contact_employees(company_contact_employees):
    #company_contact_employees = CompanyContactEmployee(Company_idContactPersons=company_contact_employees['Company_idContactPersons'],first_name=company_contact_employees['first_name'],last_name=company_contact_employees['last_name'],phone=company_contact_employees['phone'],email=company_contact_employees['email'])
    company_contact_employees = CompanyContactEmployee(**company_contact_employees)
    session.add(company_contact_employees)
    session.commit()
