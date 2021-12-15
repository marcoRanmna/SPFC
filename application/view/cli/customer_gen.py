from application.bll.customer_controller import get_all_customers, create_customer


def view_customers():
    customers = get_all_customers()
    print("*"*10,"\nAll Customers\n"+"*"*10,"\n")
    for customer in customers:
        print(customer)

def add_customers(customers):
    #customers = {
    #    'created': '',
    #    'private_person_or_company': ''
    #}
    create_customer(customers)

def test_add_customers():
    customers = {
        'created': '2020-12-12',
        'private_person_or_company': 1,
        'Company_idContactPersons': 1,
        'Employees_idEmployees': 1,
        'private_person_idprivate_person': 1,
        'delivery_adress_iddelivery_adress': 1
    }
    add_customers(customers)

if __name__ == '__main__':
    test_add_customers()
    #view_customers()
