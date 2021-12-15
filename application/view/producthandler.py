from application.dll.db.db import session
from application.dll.models import CarModel as Component
from application.dll.models import Product, ProductStored

class Productquery:

    def __init__(self,car):
        self.car = car
        component = session.query(Component).filter_by(car_brand=self.car.brand, car_model=self.car.model).first()
        self.idcomponent = component.idcomponent_model

    @classmethod
    def verified(cls, brand, model):
        component = session.query(Component).filter_by(car_brand=brand, car_model=model).first()
        return False if component is None else True

    @classmethod
    def get_component_id(cls, brand, model):
        component = session.query(Component).filter_by(car_brand=brand, car_model=model).first()
        return component.idcomponent_model

    @staticmethod
    def fuzzy_breakdown(search):
        '''
            Breaks down the string to return list
        '''
        return [x for x in search.split("*") if len(x) > 0]

    def query_search(self, search):
        product_list = []
        result = session.query(Product).filter_by(component_model_idcomponent_model=self.idcomponent).all()
        for product in result:
            if all(s.lower() in product.product_name.lower() for s in search):
                stored = session.query(ProductStored).filter_by(idproduct_stored=product.product_stored_idproduct_stored).first()
                setattr(product, 'quantity', stored.product_stored)
                product_list.append(product)
        return product_list

class ProductsHandler(Productquery):
    def __init__(self, customer):
        super().__init__(customer)

    def refresh(self, search):
        self.search = super().fuzzy_breakdown(search)
        self.customer_products = self.query_search(self.search)

    def ls(self):
        for i, product in enumerate(self.customer_products):
            print("+"+("-"*25)+"+")
            print("|", f"{product.product_name}     Left: {product.quantity}".ljust(23), "|")
            print("|", f"Price {product.sell_price} sek".ljust(23), "|")
            print("|", f"{product.description}".ljust(23), "|")
            print("+"+("-"*25)+"+")

