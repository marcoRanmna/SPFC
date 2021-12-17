from application.dll.db.db import session
from application.dll.models import Company


def get_all_companies():
    return session.query(Company).all()


def get_specific_companies(idContactPersons=None, company_name=None, phone_number=None, email=None):
    d = {idContactPersons:Company.idContactPersons, company_name:Company.company_name, phone_number:Company.phone_number, email:Company.email}
    keys = [d[key]==key for key in d if key != None]
    return session.query(Company).filter(*keys).all()


def create_companies(companies):
    #companies = Company(company_name=companies['company_name'], phone_number=companies['phone_number'], email=companies['email'])
    companies = Company(**companies)
    session.add(companies)
    session.commit()


