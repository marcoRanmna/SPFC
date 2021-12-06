from application.dll.repository import manufacture_repository as manufacture_r


def get_all_manufactures():
    return manufacture_r.get_all_manufactures


def create_manufactures(manufacture):
    manufacture_r.create_manufactures(manufacture)
