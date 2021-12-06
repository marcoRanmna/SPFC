from application.dll.repository import manufacture_office_repository as manufacture_office_r


def get_all_manufacture_office():
    return manufacture_office_r.get_all_manufacture_office()


def create_manufacture_office(manufacture_office):
    manufacture_office_r.create_manufacture_office(manufacture_office)
