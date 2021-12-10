from application.dll.models import Manufacture
from application.dll.db.db import session


def get_all_manufactures():
    return session.query(Manufacture).all()


def create_manufactures(manufacture):
    print(manufacture['company_name'], manufacture['number_head_office'])
    manufacture = Manufacture(company_name=manufacture['company_name'], number_head_office=manufacture['number_head_office'])
    session.add(manufacture)
    session.commit()
