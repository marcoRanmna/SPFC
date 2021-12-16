from application.dll.db.db import session
from application.dll.models import PrivatePerson


def get_all_private_customers():
    return session.query(PrivatePerson).all()


def get_specific_private_customers(idprivate_person=None, first_name=None, last_name=None, phone=None, email=None):
    d = {idprivate_person:PrivatePerson.idprivate_person, first_name:PrivatePerson.first_name, last_name:PrivatePerson.last_name, phone:PrivatePerson.phone, email:PrivatePerson.email}
    keys = [d[key]==key for key in d if key != None]
    return session.query(PrivatePerson).filter(*keys).all()


def create_private_customers(private_customers):
    private_customers = PrivatePerson(**private_customers)
    session.add(private_customers)
    session.commit()
