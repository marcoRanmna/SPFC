from application.dll.models import CarInfo
from application.dll.db.db import session


def get_all_carinfo():
    return session.query(CarInfo).all()

def get_all_not_none_values():
    values = session.query(CarInfo).first()
    for value in values:
        if value != None:
            values.append(value)

def create_carinfo(carinfo):
    carinfo = CarInfo(**carinfo)
    session.add(carinfo)
    session.commit()
