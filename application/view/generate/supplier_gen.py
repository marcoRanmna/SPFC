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
        'company_name': 'Bilbengt',
        'email': 'bengt@email.com',
        'phone': '0707007006',
        'state': 'Holland',
        'country': 'sweden',
        'zipcode': '43540',
        'city': 'klaras',
        'adress': 'bokgatan 1',
        'Products_idProducts': 8
    }
    create_suppliers(supplier)

if __name__ == '__main__':
    add_supplier()
