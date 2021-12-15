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
        'country': '',
        'zipcode': '',
        'city': '',
        'adress': '',
        'Products_idProducts': ''
    }
    create_suppliers(supplier)

if __name__ == '__main__':
    add_supplier()
