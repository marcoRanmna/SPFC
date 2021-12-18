from application.dll.repository import customer_repository as customer_r
from application.mongo_dll.repository import customer_repository
from application.bll import mongo_or_mysql


def get_all_customers():
    if mongo_or_mysql == False:
        return customer_r.get_all_customers()
    else:
        return customer_repository.get_all_customers()


def get_specific_customers(idCustomers=None, created=None, private_person_or_company=None, Company_idContactPersons=None, Employees_idEmployees=None, private_person_idprivate_person=None, delivery_adress_iddelivery_adress=None):
    if mongo_or_mysql == False:
        return customer_r.get_specific_customers(idCustomers, created, private_person_or_company, Company_idContactPersons, Employees_idEmployees, private_person_idprivate_person, delivery_adress_iddelivery_adress)
    else:
        return customer_repository.find_customers(created)


def create_customer(customers):
    if mongo_or_mysql == False:
        customer_r.create_customers(customers)
    else:
        customer_repository.create_customers(customers)
