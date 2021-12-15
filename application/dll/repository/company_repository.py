from application.dll.db.db import session
from application.dll.models import Company


def get_all_companies():
    return session.query(Company).all()

def get_one_companies(company_name=None, phone_number=None):
    pass 

def create_companies(companies):
    companies = Company(company_name=companies['company_name'], phone_number=companies['phone_number'], email=companies['email'])
    session.add(companies)
    session.commit()


