from application.dll.repository import orders_repository as order_r
from application.mongo_dll.repository import order_repository
from application.bll import mongo_or_mysql


def get_all_orders():
    if mongo_or_mysql == False:
        return order_r.get_all_orders()
    else:
        return order_repository


def get_specific_orders(idOrders=None, Customers_idCustomers=None, purchase_date=None, requireddate=None, shippeddate=None, status=None, comments=None, supplier_id=None):
    if mongo_or_mysql == False:
        return order_r.get_specific_orders(idOrders, Customers_idCustomers, purchase_date, requireddate, shippeddate, status, comments, supplier_id)
    else:
        return order_repository.find_orders(Customers_idCustomers)


def create_orders(orders):
    if mongo_or_mysql == False:
        order_r.create_orders(orders)
    else:
        order_repository.create_orders(orders)
