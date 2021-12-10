from application.dll.db.db import session
from application.dll.models import Company


def get_all_companies():
    return session.query(Company).all()


def create_companies(companies):
    #companies = Company(**companies)
    print(companies['company_name'], companies['phone_number'], companies['email'])
    companies = Company(company_name=companies['company_name'], phone_number=companies['phone_number'], email=companies['email'])
    session.add(companies)
    session.commit()
