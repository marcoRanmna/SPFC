from application.bll.orders_controller import get_all_orders, create_orders


def view_orders():
    orders = get_all_orders()
    print("***********")
    print("All Orders")
    print("***********")
    print()
    for order in orders:
        print(order)


def add_orders():
    orders = {
        'purchase_date': '',
        'requireddate': '',
        'shippeddate': '',
        'status': '',
        'comments': ''
    }
    create_orders(orders)


def delete_record():
    pass
