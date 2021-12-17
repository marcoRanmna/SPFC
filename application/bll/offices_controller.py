from application.dll.repository import offices_repository as office_r
from application.mongo_dll.repository import office_repository
from application.bll import mongo_or_mysql


def get_all_offices():
    if mongo_or_mysql == False:
        return office_r.get_all_offices()
    else:
        return office_repository.get_all_offices()


def get_specific_offices(idoffices=None, office_name=None, city=None, phone_number=None, adress=None, state=None, country=None, zipcode=None, Storage_idOffice_storage=None):
    if mongo_or_mysql == False:
        return office_r.get_specific_offices(idoffices, office_name, city, phone_number, adress, state, country, zipcode, Storage_idOffice_storage)
    else:
        return office_repository.find_offices(office_name)


def create_offices(offices):
    if mongo_or_mysql == False:
        office_r.create_offices(offices)
    else:
        office_repository.create_office(offices)
