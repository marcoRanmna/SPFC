from application.dll.repository import manufacture_repository as manufacture_r
from application.mongo_dll.repository import manufacture_repository
from application.bll import mongo_or_mysql


def get_all_manufactures():
    if mongo_or_mysql == False:
        return manufacture_r.get_all_manufactures()
    else:
        return manufacture_repository.get_all_manufactures()


def get_specific_manufactures(idManufactures=None, company_name=None, number_head_office=None):
    if mongo_or_mysql == False:
        return manufacture_r.get_specific_manufactures(idManufactures, company_name, number_head_office)
    else:
        return manufacture_repository.find_manufactures(company_name)


def create_manufactures(manufacture):
    if mongo_or_mysql == False:
        manufacture_r.create_manufactures(manufacture)
    else:
        manufacture_repository.create_manufacture(manufacture)
