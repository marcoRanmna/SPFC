from application.bll.supplier_controller import get_specific_suppliers


class Supplier:
    def __init__(self, products):
        self.products = products
        for product in self.products:
            self.suppliers = get_specific_suppliers(Products_idProducts=product.idProducts)

    def present(self):
        suppliers_ls = []
        print('***Suppliers***\n================')
        for supplier in self.suppliers:
            print(f'***{supplier.company_name}***')
            suppliers_ls.append(supplier.company_name)
        while True:
            choice = input('Which supplier would you like to use? ')
            if choice in suppliers_ls:
                print(f'{choice} will now be the supplier')
                supplier_obj = get_specific_suppliers(company_name=choice)[0]
                return supplier_obj.idSuppliers
            else:
                print(f'{choice} is not a supplier for this product')


