import csv
from os import path
from datetime import datetime
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
    dir_path = "C:/Teknikhögskolan/SpareParts/PyCharm/application/dll/repository/data/"
    file_car = dir_path + "car.csv"
    print(file_car, path.exists(file_car))

    with open(file_car, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for _ in range(20):
            car_list = [c.strip() for c in next(csv_reader)]
            car_list[3] = datetime.strptime(car_list[3], '%Y').year

            car_models = {
                'car_brand': car_list[1],
                'car_model': car_list[2],
                'car_model_year': car_list[3]
            }
            print(car_models)
            add_car_models(car_models)


if __name__ == '__main__':
    #test_add_car_model()
    view_car_models()
