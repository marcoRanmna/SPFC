from application.dll.repository import supplier_repository as supplier_r
from application.mongo_dll.repository import supplier_repository
from application.bll import mongo_or_mysql


def get_all_suppliers():
    if mongo_or_mysql == False:
        return supplier_r.get_all_suppliers()
    else:
        return supplier_repository.get_all_suppliers()


def get_specific_suppliers(idSuppliers=None, company_name=None, email=None, phone=None, country=None, state=None, zipcode=None, city=None, adress=None, Products_idProducts=None):
    if mongo_or_mysql == False:
        return supplier_r.get_specific_suppliers(idSuppliers, company_name, email, phone, country, state, zipcode, city, adress, Products_idProducts)
    else:
        return supplier_repository.find_suppliers(company_name)


def create_suppliers(supplier):
    if mongo_or_mysql == False:
        supplier_r.create_suppliers(supplier)
    else:
        supplier_repository.create_supplier(supplier)
