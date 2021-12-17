from application.dll.repository import private_customer_repository as pc_r


def get_all_private_customers():
    return pc_r.get_all_private_customers()

def get_specific_private_customers(idprivate_person=None, first_name=None, last_name=None, phone=None, email=None):
    return pc_r.get_specific_private_customers(idprivate_person, first_name, last_name, phone, email)

def create_private_customers(private_customers):
    pc_r.create_private_customers(private_customers)

