from application.dll.db.db import session
from application.dll.models import Customer


def get_all_customers():
    return session.query(Customer).all()


def get_specific_customers(idCustomers=None, created=None, private_person_or_company=None, Company_idContactPersons=None, Employees_idEmployees=None, private_person_idprivate_person=None, delivery_adress_iddelivery_adress=None):
    d = {idCustomers:Customer.idCustomers, created:Customer.created, private_person_or_company:Customer.private_person_or_company, Company_idContactPersons:Customer.Company_idContactPersons, Employees_idEmployees:Customer.Employees_idEmployees, private_person_idprivate_person:Customer.private_person_idprivate_person, delivery_adress_iddelivery_adress:Customer.delivery_adress_iddelivery_adress}
    keys = [d[key]==key for key in d if key != None]
    return session.query(Customer).filter(*keys).all()


def create_customers(customer):
    customers = Customer(**customer)
    session.add(customers)
    session.commit()


