from application.dll.repository import customer_repository as customer_r


def get_all_customers():
    return customer_r.get_all_customers()


def create_customer(customers):
    customer_r.create_customers(customers)
