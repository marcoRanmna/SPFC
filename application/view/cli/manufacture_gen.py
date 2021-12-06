from application.bll.manufacture_controller import get_all_manufactures, create_manufactures


def view_manufacture():
    manufactures = get_all_manufactures()
    print("***********")
    print("All Manufactures")
    print("***********")
    print()
    for manufacture in manufactures:
        print(manufacture)


def add_manufacture():
    manufacture = {
        'company_name': '',
        'number_head_office': '',
    }
    create_manufactures(manufacture)
