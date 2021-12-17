from application.dll.repository import company_repository as company_r
from application.mongo_dll.repository import company_repository
from application.bll import mongo_or_mysql


def get_all_companies():
    if mongo_or_mysql == False:
        return company_r.get_all_companies()
    else:
        return company_repository.get_all_companys()

def get_specific_companies(idContactPersons=None, company_name=None, phone_number=None, email=None):
    if mongo_or_mysql == False:
        return company_r.get_specific_companies(idContactPersons, company_name, phone_number, email)
    else:
        return company_repository.find_companys(company_name)

def create_companies(companies):
    if mongo_or_mysql == False:
        company_r.create_companies(companies)
    else:
        company_repository.create_company(companies)