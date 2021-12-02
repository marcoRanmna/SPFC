from application.dll.repository import orderdetails_repository as orderdetail_r


def get_all_orderdetails():
    return orderdetail_r.get_all_orderdetails()


def create_orderdetails(orderdetail):
    orderdetail_r.create_orderdetails(orderdetail)
