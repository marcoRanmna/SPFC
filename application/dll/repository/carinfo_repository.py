from application.dll.models import CarInfo
from application.dll.db.db import session


def get_all_carinfo():
    return session.query(CarInfo).all()


def get_specific_carinfo(idCarinfo=None, reg_number=None, manufacture_name=None, model=None, year_model=None, color=None, Customers_idCustomers=None):
    d = {idCarinfo:CarInfo.idCarinfo, reg_number:CarInfo.reg_number, manufacture_name:CarInfo.manufacture_name, model:CarInfo.model, year_model:CarInfo.model, color:CarInfo.color, Customers_idCustomers:CarInfo.Customers_idCustomers}
    keys = [d[key]==key for key in d if key != None]
    return session.query(CarInfo).filter(*keys).all()


def create_carinfo(carinfo):
    carinfo = CarInfo(**carinfo)
    session.add(carinfo)
    session.commit()
