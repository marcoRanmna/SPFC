from application.dll.repository import offices_repository as office_r


def get_all_offices():
    return office_r.get_all_offices()


def create_offices(offices):
    office_r.create_offices(offices)
