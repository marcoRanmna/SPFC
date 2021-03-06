from application.bll.component_model_controller import get_specific_car_models
from application.bll.product_controller import get_specific_products, get_all_products
from application.bll.product_storage_controller import get_specific_product_storages
from application.bll.orders_controller import get_specific_orders
from application.bll.orderdetails_controller import get_specific_orderdetails

class Productquery:

    def __init__(self,car):
        self.car = car
        component = get_specific_car_models(car_brand=self.car.brand, car_model=self.car.model)[0]
        self.idcomponent = component.idcomponent_model

    @classmethod
    def verified(cls, brand, model):
        component = get_specific_car_models(car_brand=brand, car_model=model)[0]
        return False if component is None else True

    @classmethod
    def get_component_id(cls, brand, model):
        component = get_specific_car_models(car_brand=brand, car_model=model)[0]
        return component.idcomponent_model

    @staticmethod
    def fuzzy_breakdown(search):
        '''
            Breaks down the string to return list
        '''
        return [x for x in search.split("*") if len(x) > 0]

    def query_search(self, search):
        product_list = []
        result = get_all_products()
        for product in result:
            if all(s.lower() in product.product_name.lower() for s in search):
                stored = get_specific_product_storages(idproduct_stored=product.product_stored_idproduct_stored)[0]
                setattr(product, 'quantity', stored.product_stored)
                product_list.append(product)
        return product_list
    
    @classmethod
    def get_all_customers_orders(cls, idCustomers):
        return get_specific_orders(Customers_idCustomers=idCustomers)


class ProductsHandler(Productquery):
    def __init__(self, customer):
        super().__init__(customer)

    def refresh(self, search):
        self.search = super().fuzzy_breakdown(search)
        self.customer_products = self.query_search(self.search)

    def ls(self):
        for i, product in enumerate(self.customer_products):
            print("+"+("-"*35)+"+")
            print("|", f"{product.product_name}  Left: {product.quantity}".ljust(33), "|")
            print("|", f"Price {product.sell_price} sek".ljust(33), "|")
            print("|", f"{product.description}".ljust(33), "|")
            print("+"+("-"*35)+"+")

    def show_orders(self, customer_obj):
        for orders in super().get_all_customers_orders(customer_obj.idCustomers):
            print("+"+("-"*35)+"+")
            print("|", f"Purchased: {orders.purchase_date}".ljust(33), "|")
            print("|", f"Status: {orders.status}".ljust(33), "|")
            for orderdetail in get_specific_orderdetails(Orders_idOrders=orders.idOrders):
                products = get_specific_products(product_number=orderdetail.product_number)[0]
                print("|", f"Product: {products.product_name}".ljust(33), "|")
                print("|", f"Amount: {orderdetail.quantityordered}".ljust(33), "|")
                print("|", f"Price {orderdetail.price}".ljust(33), "|")
            print("+"+("-"*35)+"+")


