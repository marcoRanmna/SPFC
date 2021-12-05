from application.bll.delivery_adress_controller import get_all_delivery_adress, create_delivery_adress


def view_delivery_adress():
    delivery_adress = get_all_delivery_adress()
    print("***********")
    print("All Delivery Addresses")
    print("***********")
    print()
    for da in delivery_adress:
        print(da)


def add_delivery_adress():
    delivery_adress = {
        'country': '',
        'city': '',
        'state': '',
        'zipcode': '',
        'adress': ''
    }
    create_delivery_adress(delivery_adress)


def delete_record():
    pass
