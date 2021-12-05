from application.dll.models.suppliers import Supplier
from db import session


def get_all_suppliers():
    return session.query(Supplier).all()


def create_suppliers(supplier):
    supplier = Supplier(**supplier)
    session.add(supplier)
    session.commit()
