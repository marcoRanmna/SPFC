from application.dll.repository import orderdetails_repository as orderdetail_r


def get_all_orderdetails():
    return orderdetail_r.get_all_orderdetails()

def get_specific_orderdetails(idOrderdetails=None, product_number=None, quantityprdered=None, price=None, Orders_idOrders=None):
    return orderdetail_r.get_specific_orderdetails(idOrderdetails, product_number, quantityprdered, price, Orders_idOrders)

def create_orderdetails(orderdetail):
    orderdetail_r.create_orderdetails(orderdetail)
