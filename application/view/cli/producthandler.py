from application.bll.component_model_controller import get_specific_car_models
from application.bll.product_controller import get_specific_products, get_all_products
from application.bll.product_storage_controller import get_specific_product_storages

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

