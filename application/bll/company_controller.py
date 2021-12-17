from application.dll.repository import company_repository as company_r


def get_all_companies():
    return company_r.get_all_companies()

def get_specific_companies(idContactPersons=None, company_name=None, phone_number=None, email=None):
    return company_r.get_specific_companies(idContactPersons, company_name, phone_number, email)

def create_companies(companies):
    company_r.create_companies(companies)
