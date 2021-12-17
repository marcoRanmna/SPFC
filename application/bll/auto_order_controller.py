from application.dll.repository import auto_order_repository as auto_order_r


def delete_auto_order(auto_order):
    auto_order_r.delete_auto_order(auto_order)


def get_auto_order():
    return auto_order_r.get_auto_order()
