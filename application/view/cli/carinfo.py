from application.bll.carinfo_controller import get_all_carinfo, create_carinfo


def view_product():
    carinfo = get_all_carinfo()
    print("***********")
    print("All Carinfo")
    print("***********")
    print()
    for c_info in carinfo:
        print(c_info)


def add_carinfo():
    carinfo = {
        'reg_number': '',
        'manufacture_name': '',
        'model': '',
        'year_model': '',
        'color': ''
    }
    create_carinfo(carinfo)
