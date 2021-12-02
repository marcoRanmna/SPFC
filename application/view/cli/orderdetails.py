from application.bll.orderdetails_controller import get_all_orderdetails, create_orderdetails

def view_orderdetails():
    orderdetails = get_all_orderdetails()
    print("***********")
    print("All Orderdetails")
    print("***********")
    print()
    for orderdetail in orderdetails:
        print(orderdetail)

def add_orderdetails():
    orderdetail = {
        'product_number': '',
        'quantityordered': '',
        'price': ''
    }
    create_orderdetails(orderdetail)
