from application.dll.db.db import session
from application.dll.models import Customer


def get_all_customers():
    return session.query(Customer).all()


def create_customers(customer):
    customers = Customer(**customer)
    session.add(customers)
    session.commit()


