from application.dll.repository import component_model_repository as component_r


def get_all_car_models():
    return component_r.get_all_car_models()

def get_specific_car_models(idcomponent_model=None, car_brand=None, car_model=None, car_model_year=None):
    return component_r.get_specific_car_models(idcomponent_model, car_brand, car_model, car_model_year)

def create_car_models(car_models):
    component_r.create_car_model(car_models)

