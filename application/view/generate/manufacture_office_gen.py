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
        'phone': '0808',
        'adress': 'As',
        'city': 'Di',
        'country': 'Po',
        'zipcode': 'Da',
        'state': 'Hej',
        'Manufactures_idManufactures': 1

    }
    create_manufacture_office(manufacture_office)


if __name__ == '__main__':
    add_manufacture_office()