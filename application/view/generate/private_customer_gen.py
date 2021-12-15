from application.bll.private_customer_controller import get_all_private_customers, create_private_customers


def view_private_customers():
    private_customers = get_all_private_customers()
    print("*"*10,"\nAll Private Customers\n"+"*"*10,"\n")
    for customer in private_customers:
        print(customer)


def add_private_customers(private_customers):
    #private_customers = {
     #   'first_name': '',
      #  'last_name': '',
       # 'phone': '',
        #'email': ''
    #}
    create_private_customers(private_customers)


def test_add_customers():
    private_customers = {
        'first_name': 'Kalle',
        'last_name': 'Svensson',
        'phone': '0704050504',
        'email': 'kalle@email.com'
    }
    add_private_customers(private_customers)


if __name__ == '__main__':
    test_add_customers()
    #view_private_customers()
