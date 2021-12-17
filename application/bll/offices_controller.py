from application.dll.repository import offices_repository as office_r


def get_all_offices():
    return office_r.get_all_offices()

def get_specific_offices(idoffices=None, office_name=None, city=None, phone_number=None, adress=None, state=None, country=None, zipcode=None, Storage_idOffice_storage=None):
    return office_r.get_specific_offices(idoffices, office_name, city, phone_number, adress, state, country, zipcode, Storage_idOffice_storage)

def create_offices(offices):
    office_r.create_offices(offices)
