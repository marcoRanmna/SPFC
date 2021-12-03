from application.dll.repository import carinfo_repository as carinfo_r


def get_all_carinfo():
    return carinfo_r.get_all_carinfo


def create_carinfo(carinfo):
    carinfo_r.create_carinfo(carinfo)
