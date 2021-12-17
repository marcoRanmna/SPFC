from application.dll.repository import company_contact_employee_repository as cce_r


def get_all_company_contact_employees():
    return cce_r.get_all_company_contact_employees()

def get_specific_company_contact_employees(idcompany_contact_employees=None, Company_idContactPersons=None, first_name=None, last_name=None, phone=None, email=None):
    return cce_r.get_specific_company_contact_employees(idcompany_contact_employees, Company_idContactPersons, first_name, last_name, phone, email)

def create_company_contact_employees(company_contact_employees):
    cce_r.create_company_contact_employees(company_contact_employees)
