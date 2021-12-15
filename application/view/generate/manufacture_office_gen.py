from application.bll.manufacture_office_controller import get_all_manufacture_office, create_manufacture_office


def view_manufacture_office():
    manufactures_office = get_all_manufacture_office()
    print("***********")
    print("All Manufactures_office")
    print("***********")
    print()
    for manufacture_office in manufactures_office:
        print(manufacture_office)


def add_manufacture_office():
    manufacture_office = {
        'phone': '',
        'adress': '',
        'country': '',
        'zipcode': '',
        'state': '',

    }
    create_manufacture_office(manufacture_office)
