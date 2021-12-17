from application.dll.repository import manufacture_repository as manufacture_r


def get_all_manufactures():
    return manufacture_r.get_all_manufactures()

def get_specific_manufactures(idManufactures=None, company_name=None, number_head_office=None):
    return manufacture_r.get_specific_manufactures(idManufactures, company_name, number_head_office)

def create_manufactures(manufacture):
    manufacture_r.create_manufactures(manufacture)
