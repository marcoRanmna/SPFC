from application.bll.offices_controller import get_all_offices, create_offices


def view_offices():
    offices = get_all_offices()
    print("***********")
    print("All Offices")
    print("***********")
    print()
    for office in offices:
        print(office)


def add_offices():
    offices = {
        'city': '',
        'phone_number': '',
        'adress': '',
        'state': '',
        'country': '',
        'zipcode': ''
    }
    create_offices(offices)


def delete_record():
    pass