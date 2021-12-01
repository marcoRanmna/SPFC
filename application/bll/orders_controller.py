from application.dll.repository import orders_repository as order_r


def get_all_orders():
    return order_r.get_all_orders()
