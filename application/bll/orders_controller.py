from application.dll.repository import orders_repository as order_r


def get_all_orders():
    return order_r.get_all_orders()

def get_specific_orders(idOrders=None, Customers_idCustomers=None, purchase_date=None, requireddate=None, shippeddate=None, status=None, comments=None, supplier_id=None):
    return order_r.get_specific_orders(idOrders, Customers_idCustomers, purchase_date, requireddate, shippeddate, status, comments, supplier_id)

def create_orders(orders):
    order_r.create_orders(orders)
