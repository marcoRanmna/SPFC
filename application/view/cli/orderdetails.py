from application.bll.orderdetails_controller import get_all_orderdetails

def view_orders():
    orderdetails = get_all_orderdetails()
    print("***********")
    print("All Orders")
    print("***********")
    print()
    for orderdetail in orderdetails:
        print(orderdetail)
