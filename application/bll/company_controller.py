from application.dll.repository import company_repository as company_r


def get_all_companies():
    return company_r.get_all_companies()


def create_companies(companies):
    company_r.create_companies(companies)
