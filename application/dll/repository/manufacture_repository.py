from application.dll.models import Manufacture
from application.dll.db.db import session


def get_all_manufactures():
    return session.query(Manufacture).all()


def get_specific_manufactures(idManufactures=None, company_name=None, number_head_office=None):
    d = {idManufactures:Manufacture.idManufactures, company_name:Manufacture.company_name, number_head_office:Manufacture.number_head_office}
    keys = [d[key]==key for key in d if key != None]
    return session.query(Manufacture).filter(*keys).all()


def create_manufactures(manufacture):
    manufacture = Manufacture(**manufacture)
    session.add(manufacture)
    session.commit()
