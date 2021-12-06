from application.dll.repository import storage_repository as storage_r


def get_all_storage():
    return storage_r.get_all_storage

def create_storage(storage):
    storage_r.create_storage(storage)
