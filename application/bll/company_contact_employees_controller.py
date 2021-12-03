from application.dll.repository import company_contact_employee_repository as cce_r


def get_all_company_contact_employees():
    return cce_r.get_all_company_contact_employees()
