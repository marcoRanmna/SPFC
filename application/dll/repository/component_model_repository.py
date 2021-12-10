from application.dll.db.db import session
from application.dll.models import CarModel


def get_all_car_models():
    return session.query(CarModel).all()


def create_car_model(car_model):
    car_models = CarModel(**car_model)
    session.add(car_models)
    session.commit()
