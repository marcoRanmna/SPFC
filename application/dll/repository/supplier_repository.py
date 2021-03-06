from application.dll.models import Supplier
from application.dll.db.db import session


def get_all_suppliers():
    return session.query(Supplier).all()


def get_specific_suppliers(idSuppliers=None, company_name=None, email=None, phone=None, country=None, state=None, zipcode=None, city=None, adress=None, Products_idProducts=None):
    d = {idSuppliers:Supplier.idSuppliers, company_name:Supplier.company_name, email:Supplier.email, phone:Supplier.phone, country:Supplier.country, state:Supplier.state, zipcode:Supplier.zipcode, city:Supplier.city, adress:Supplier.adress, Products_idProducts:Supplier.Products_idProducts}
    keys = [d[key]==key for key in d if key != None]
    return session.query(Supplier).filter(*keys).all()


def create_suppliers(supplier):
    supplier = Supplier(**supplier)
    session.add(supplier)
    session.commit()
