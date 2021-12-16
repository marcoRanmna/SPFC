from application.dll.db.db import session
from application.dll.models import CarModel


def get_all_car_models():
    #return session.query(CarModel).all()
    specific = session.query(CarModel).all()
    #return session.query(CarModel).filter(CarModel.car_model_year.isnot(None))
    res = list(filter(None, specific))
    print(str(res))
    return res


def get_specific_car_models(idcomponent_model=None, car_brand=None, car_model=None, car_model_year=None):
    d = {idcomponent_model:CarModel.idcomponent_model, car_brand:CarModel.car_brand, car_model:CarModel.car_model, car_model_year:CarModel.car_model_year}
    keys = [d[key]==key for key in d if key != None]
    return session.query(CarModel).filter(*keys).all()


def create_car_model(car_model):
    car_models = CarModel(**car_model)
    session.add(car_models)
    session.commit()
