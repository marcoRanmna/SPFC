from application.dll.repository import supplier_repository as supplier_r


def get_all_suppliers():
    return supplier_r.get_all_suppliers()

def get_specific_suppliers(idSuppliers=None, company_name=None, email=None, phone=None, country=None, zipcode=None, city=None, adress=None, Products_idProducts=None):
    return supplier_r.get_specific_suppliers(idSuppliers, company_name, email, phone, country, zipcode, city, adress, Products_idProducts)

def create_suppliers(supplier):
    supplier_r.create_suppliers(supplier)
