from datetime import datetime
from application.bll.orders_controller import create_orders, get_specific_orders
from application.bll.orderdetails_controller import create_orderdetails
from application.bll.product_storage_controller import subtract_quantity

class Package:
    def __init__(self, products_ordered, requireddate=None, comments=""):
        self.purchase_date = datetime.now().strftime('%Y-%m-%d %H:%M')
        self.requireddate = requireddate
        self.status = "In progress" 
        self.comments = comments
        self.orders = {}
        for product in products_ordered:
            if product.product_number in self.orders:
                self.orders[product.product_number]['quantity'] += 1
                self.orders[product.product_number]['price'] += product.sell_price
                self.orders[product.product_number]['product_stored_id'] = product.product_stored_idproduct_stored
            else:
                self.orders[product.product_number] = {'quantity': 1, 'price': product.sell_price, 'product_stored_id': product.product_stored_idproduct_stored}

    def dict_orderdetail(self):
        return self.orders 

    def dict_orders(self):
        return {'purchase_date':self.purchase_date, 'requireddate': self.requireddate, 'status': self.status, 'comments': self.comments}

    def commit(self, customer_id):
        order = self.dict_orders()
        order['Customers_idCustomers'] = customer_id
        create_orders(order)

        orders = get_specific_orders(Customers_idCustomers=order['Customers_idCustomers'], purchase_date=order['purchase_date'])[0]

        orderdetail = (orders.idOrders, customer_id)
        orderdetail_dict = self.dict_orderdetail()
        print(orderdetail_dict)
        for product_number in orderdetail_dict:
            tmp = {}
            tmp['product_number'] = product_number
            tmp['quantityordered'] = orderdetail_dict[product_number]['quantity']
            tmp['price'] = orderdetail_dict[product_number]['price']
            tmp['Orders_idOrders'] = orders.idOrders 
            create_orderdetails(tmp)
            subtract_quantity(orderdetail_dict[product_number]['product_stored_id'], tmp['quantityordered'])
            del tmp
