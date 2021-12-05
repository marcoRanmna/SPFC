from application.dll.db.db import session
from application.dll.models.company import Company


def get_all_companies():
    return session.query(Company).all()


def create_companies(companies):
    companies = Company(**companies)
    session.add(companies)
    session.commit()