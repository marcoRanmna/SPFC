from application.dll.models import Supplier
from application.dll.db.db import session


def get_all_suppliers():
    return session.query(Supplier).all()


def create_suppliers(supplier):
    supplier = Supplier(**supplier)
    #print(supplier['company_name'], supplier['email'], supplier['phone'], supplier['country'], supplier['zipcode'], supplier['city'], supplier['adress'])
    #supplier = Supplier(company_name=supplier['company_name'], email=supplier['email'], phone=supplier['phone'], country=supplier['country'], zipcode=supplier['zipcode'], city=supplier['city'], adress=supplier['adress'])
    session.add(supplier)
    session.commit()
