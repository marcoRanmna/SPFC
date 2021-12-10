from application.dll.db.db import session
from application.dll.models import PrivatePerson


def get_all_private_customers():
    return session.query(PrivatePerson).all()


def create_private_customers(private_customers):
    private_customers = PrivatePerson(**private_customers)
    session.add(private_customers)
    session.commit()
