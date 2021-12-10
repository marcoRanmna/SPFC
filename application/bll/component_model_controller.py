from application.dll.repository import component_model_repository as component_r


def get_all_car_models():
    return component_r.get_all_car_models()


def create_car_models(car_models):
    component_r.create_car_model(car_models)
