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


def create_orders(Customers_idCustomers=None, purchase_date=None, requireddate=None, shippeddate=None, status=None, comments=None, supplier_id=None, orderdetails=None):
    orders = Order({'Customers_idCustomers': Customers_idCustomers, 'purchase_date': purchase_date, 'requireddate': requireddate, 'shippeddate': shippeddate, 'status': status, 'comments': comments, 'supplier_id': supplier_id, 'orderdetails': orderdetails})
    orders.save()


if __name__ == '__main__':
    #get_all_orders()
    find_orders(12)
