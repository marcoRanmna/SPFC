from application.dll.repository import storage_repository as storage_r


def get_all_storage():
    return storage_r.get_all_storage()

def get_specific_storage(idstorage=None, adress=None, zipcode=None, city=None, state=None, country=None):
    return storage_r.get_specific_storage(idstorage, adress, zipcode, city, state, country)

def create_storage(storage):
    storage_r.create_storage(storage)
