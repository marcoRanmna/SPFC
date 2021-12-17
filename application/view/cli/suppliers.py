from application.bll.supplier_controller import get_specific_suppliers


class Supplier:
    def __init__(self, products):
        self.products = products
        for product in self.products:
            self.suppliers = get_specific_suppliers(Products_idProducts=product.idProducts)

    def present(self):
        #suppliers = []
        for supplier in self.suppliers:
            #suppliers.append(supplier.company_name)
            print(supplier)
