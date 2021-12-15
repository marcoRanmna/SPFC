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
        'country': 'Sweden',
        'city': 'Gothenburg',
        'state': 'Västra Götaland',
        'zipcode': '43560',
        'adress': 'Granvägen 7'
    }
    create_delivery_adress(delivery_adress)


def delete_record():
    pass

if __name__ == '__main__':
    add_delivery_adress()