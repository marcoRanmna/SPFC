from application.dll.repository import customer_repository as customer_r


def get_all_customers():
    return customer_r.get_all_customers()

def get_specific_customers(idCustomers=None, created=None, private_person_or_company=None, Company_idContactPersons=None, Employees_idEmployees=None, private_person_idprivate_person=None, delivery_adress_iddelivery_adress=None):
    return customer_r.get_specific_customers(idCustomers, created, private_person_or_company, Company_idContactPersons, Employees_idEmployees, private_person_idprivate_person, delivery_adress_iddelivery_adress)

def create_customer(customers):
    customer_r.create_customers(customers)
