from application.bll.supplier_controller import get_all_suppliers, create_suppliers


def view_supplier():
    suppliers = get_all_suppliers()
    print("***********")
    print("All Suppliers")
    print("***********")
    print()
    for supplier in suppliers:
        print(supplier)


def add_supplier():
    supplier = {
        'company_name': '',
        'email': '',
        'phone': '',
        'zipcode': '',
        'city': '',
        'adress': '',
    }
    create_suppliers(supplier)
