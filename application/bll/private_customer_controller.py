from application.dll.repository import private_customer_repository as pc_r


def get_all_private_customers():
    return pc_r.get_all_private_customers()


def create_private_customers(private_customers):
    pc_r.create_private_customers(private_customers)

