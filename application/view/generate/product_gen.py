import csv
from os import path
from application.bll.product_controller import get_all_products, create_products


def view_product():
    products = get_all_products()
    print("***********")
    print("All Product")
    print("***********")
    print()
    for product in products:
        print(product)


def add_products(product):
    #product = {
    #    'product_name': '',
    #    'product_number': '',
    #    'description': '',
    #    'sell_price': ''
    #}
    create_products(product)

def test_add_products():
    dir_path = "C:/Teknikhögskolan/SpareParts/PyCharm/application/dll/repository/data/"
    file_product = dir_path + "product.csv"
    print(file_product, path.exists(file_product))
    descriptions = "This is a product or something that is not nothing or is it".split()

    with open(file_product, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for i in range(1, 11):
            product_list = [c.strip() for c in next(csv_reader)]

            print(product_list)
            product = {
                'product_name': product_list[0],
                'product_number': product_list[1],
                'description': descriptions[i],
                'sell_price': float(product_list[-1]),
                'product_stored_idproduct_stored': 1,
                'component_model_idcomponent_model': i
            }
            print(product)
            add_products(product)

def my_sample_add():
    for i in range(1, 11):
        product = {
            'product_name': 'Air filter',
            'product_number': f'Gxx0J{i}',
            'description': 'A universal air filter',
            'sell_price': float("809"),
            'product_stored_idproduct_stored': 1,
            'component_model_idcomponent_model': i    
            }
        print(product)
        add_products(product)


if __name__ == '__main__':
    test_add_products()
    my_sample_add()
