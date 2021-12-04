from application.dll.models.carinfo import CarInfo
from application.dll.db.db import session


def get_all_carinfo():
    return session.query(CarInfo).all()


def create_carinfo(carinfo):
    carinfo = CarInfo(**carinfo)
    session.add(carinfo)
    session.commit()
