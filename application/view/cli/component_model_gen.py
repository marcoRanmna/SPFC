from application.bll.component_model_controller import get_all_car_models, create_car_models


def view_car_models():
    car_model = get_all_car_models()
    print("*"*10,"\nAll Component Models\n"+"*"*10,"\n")
    for models in car_model:
        print(models)


def add_car_models(car_models):
    #car_models = {
    #    'car_brand': '',
    #    'car_model': '',
    #    'car_model_year': ''
    #}
    create_car_models(car_models)


def test_add_car_model():
    car_models = {
        'car_brand': 'Volvo',
        'car_model': 'XC60',
        'car_model_year': '2020'
    }
    add_car_models(car_models)


if __name__ == '__main__':
    test_add_car_model()
    #view_car_models()
