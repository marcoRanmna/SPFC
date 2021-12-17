from application.view.mongo.mongo_models import Order


def get_all_orders():
    orders = Order.all()
    for order in orders:
        print(order)
        return order

def find_orders(Customers_idCustomers):
    orders = Order.collection.find({'Customers_idCustomers': Customers_idCustomers})
    for order in orders:
        print(order)
        return order


if __name__ == '__main__':
    #get_all_orders()
    find_orders(12)
