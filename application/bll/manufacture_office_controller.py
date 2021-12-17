from application.dll.repository import manufacture_office_repository as manufacture_office_r


def get_all_manufacture_office():
    return manufacture_office_r.get_all_manufacture_office()

def get_specific_manufacture_office(idManufacture_offices=None, phone=None, adress=None, country=None, zipcode=None, state=None, Manufactures_idManufactures=None):
    return manufacture_office_r.get_specific_manufacture_office(idManufacture_offices, phone, adress, country, zipcode, state, Manufactures_idManufactures)

def create_manufacture_office(manufacture_office):
    manufacture_office_r.create_manufacture_office(manufacture_office)
