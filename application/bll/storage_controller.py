from application.dll.repository import storage_repository as storage_r
from application.mongo_dll.repository import storage_repository
from application.bll import mongo_or_mysql


def get_all_storage():
    if mongo_or_mysql == False:
        return storage_r.get_all_storage()
    else:
        return storage_repository.get_all_storages()


def get_specific_storage(idstorage=None, adress=None, zipcode=None, city=None, state=None, country=None):
    if mongo_or_mysql == False:
        return storage_r.get_specific_storage(idstorage, adress, zipcode, city, state, country)
    else:
        return storage_repository.find_storages(country)


def create_storage(storage):
    if mongo_or_mysql == False:
        storage_r.create_storage(storage)
    else:
        storage_repository.create_storage(storage)
