from datetime import datetime
from application.view.cli.producthandler import ProductsHandler
from application.bll.customer_controller import create_customer, get_specific_customers
from application.bll.carinfo_controller import create_carinfo, get_specific_carinfo
from application.bll.private_customer_controller import get_specific_private_customers
from application.bll.delivery_adress_controller import get_specific_delivery_adress

class Customer:
    def __init__(self, priv_or_corp, car_id, brand, model, year, customer_obj=None):
        self.priv_or_corp = int(priv_or_corp)
        self.carinfo = []
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.year = year
        self.packages = []
        self.customer_obj=customer_obj

    def add_carinfo(self):
        if [self.brand, self.model, self.year] not in self.carinfo:
            self.carinfo.append([self.car_id, self.brand, self.model, self.year])

    def completed(self, reg_number, color):
        self.created = datetime.today().strftime('%Y-%m-%d')
        self.reg_number = reg_number
        self.color = color

    def car_info_dict(self):
        d = {}
        for car in self.carinfo:
            d[car[0]]= car[1:]
        return d

    def customer_dict(self):
        return {'created': self.created, 'private_person_or_company': self.priv_or_corp }

    def commit(self, d_address, private=None, corp=None):
        customer_dict = self.customer_dict()
        if customer_dict['private_person_or_company'] == 1:

            priv = get_specific_private_customers(first_name=private.first_name, last_name=private.last_name, email=private.email)[0]
            customer_dict['private_person_idprivate_person'] = priv.idprivate_person

        delivery_id = get_specific_delivery_adress(adress=d_address.address, zipcode=d_address.zipcode, country=d_address.country)[0]
        customer_dict['delivery_adress_iddelivery_adress'] = delivery_id.iddelivery_adress
        create_customer(customer_dict)

        # -- car_info
        customer_id = self.car_info_commit(customer_dict)

        # -- Package
        self.packages_commit(customer_id)

    def car_info_commit(self, customer_dict):
        customer_obj = get_specific_customers(created=customer_dict['created'], private_person_or_company=customer_dict['private_person_or_company'], delivery_adress_iddelivery_adress=customer_dict['delivery_adress_iddelivery_adress'])[0]

        car_info_lists = self.car_info_dict()
        for car_key in car_info_lists:
            tmp = {}
            tmp['Customers_idCustomers'] = customer_obj.idCustomers
            tmp['manufacture_name'] = car_info_lists[car_key][0]
            tmp['model'] = car_info_lists[car_key][1]
            tmp['year_model'] = car_info_lists[car_key][2]
            tmp['reg_number'] = self.reg_number
            tmp['color'] = self.color
            print(tmp)
            create_carinfo(tmp)
            del tmp
        return customer_obj.idCustomers
    
    def packages_commit(self, customer_id):
        for package in self.packages:
            package.commit(customer_id)

    @classmethod
    def carintroduction(cls, priv_or_corp):
        print("To provid you with the best care dear customer.")
        print("\nPlease tell us about your car.")
        print("So Evil corp highly performative bullshit engine will")
        print("deliver all the necessary information right to your screen.")
        print("This is allow to give you directly what you wish for.")
        while True:
            print("\n")
            brand = input("Car Brand: ")
            model = input("Car model: ")
            year = input("Car year model: ")

            date_format = '%Y'
            valid_year = len(year) == 4 and year.isdigit() and datetime.now().year > datetime.strptime(year, date_format).year
            if len(brand) < 45 and len(model) < 45 and valid_year:
                if ProductsHandler.verified(brand, model):
                    car_id = ProductsHandler.get_component_id(brand, model)
                    break
                print("\nSorry we don't have any relevant products to that specific brand or model")
                print("Please try another car")
            print("Invalid input")
            priv_or_corp = int(priv_or_corp)
        return Customer(priv_or_corp, car_id, brand, model, year)

    @classmethod
    def previous_locate(cls, person, priv_or_corp):
        if priv_or_corp == "1":
            customer_obj = get_specific_customers(private_person_or_company=priv_or_corp, private_person_idprivate_person=person.idperson)[0]
        else:
            customer_obj = get_specific_customers(private_person_or_company=priv_or_corp, Company_idContactPersons=person.idperson)[0]
        cars = get_specific_carinfo(Customers_idCustomers=customer_obj.idCustomers)
        print("select which car you like to use")
        ids = {}
        for car in cars:
            print("+"+("-"*35)+"+")
            print("|", f"id:({car.idCarinfo}) {car.manufacture_name} {car.model}".ljust(33), "|")
            print("|", f"Year model {car.year_model}".ljust(33), "|")
            print("|", f"{car.reg_number} {car.color}".ljust(33), "|")
            print("+"+("-"*35)+"+")
            ids[car.idCarinfo] = [car.manufacture_name, car.model, car.year_model]
        while True:
            car_id = input("Enter id: ")
            if car_id.isdigit() and int(car_id) in ids:
                car_id = int(car_id)
                return Customer(priv_or_corp, car_id, ids[car_id][0], ids[car_id][1],ids[car_id][2], customer_obj=customer_obj)

