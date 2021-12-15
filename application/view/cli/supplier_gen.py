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
        'company_name': 'Postnorth',
        'email': 'postnorth@email.com',
        'phone': '0707040506',
        'country': 'Sweden',
        'zipcode': '42056',
        'city': 'Gothenburg',
        'adress': 'Postgatan 45',
        'Products_idProducts': 1
    }
    create_suppliers(supplier)

if __name__ == '__main__':
    add_supplier()
