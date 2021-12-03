from application.bll.orders_controller import get_all_orders


def view_orders():
    orders = get_all_orders()
    print("***********")
    print("All Orders")
    print("***********")
    print()
    for order in orders:
        print(order)


def add_order():
    pass


def delete_record():
    pass
