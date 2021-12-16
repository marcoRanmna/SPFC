from application.dll.models import ManufactureOffice
from application.dll.db.db import session


def get_all_manufacture_office():
    return session.query(ManufactureOffice).all()


def get_specific_manufacture_office(idManufacture_offices=None, phone=None, adress=None, country=None, zipcode=None, state=None, Manufactures_idManufactures=None):
    d = {idManufacture_offices:ManufactureOffice.idManufactures_offices, phone:ManufactureOffice.phone, adress:ManufactureOffice.adress, country:ManufactureOffice.country, zipcode:ManufactureOffice.zipcode, state:ManufactureOffice.state, Manufactures_idManufactures:ManufactureOffice.Manufactures_idManufactures}
    keys = [d[key]==key for key in d if key != None]
    return session.query(ManufactureOffice).filter(*keys).all()


def create_manufacture_office(manufacture_office):
    #print(manufacture_office['phone'], manufacture_office['adress'], manufacture_office['country'], manufacture_office['zipcode'], manufacture_office['state'])
    #manufacture_office = ManufactureOffice(phone=manufacture_office['phone'], adress=manufacture_office['adress'], country=manufacture_office['country'], zipcode=manufacture_office['zipcode'], state=manufacture_office['state'])
    manufacture_office = ManufactureOffice(**manufacture_office)
    session.add(manufacture_office)
    session.commit()
