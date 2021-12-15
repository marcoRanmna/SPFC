from application.bll.private_customer_controller import create_private_customers
from application.bll.delivery_adress_controller import create_delivery_adress

class Person:
    def __init__(self,first_name, last_name, phone, email):
        self.first_name = first_name 
        self.last_name = last_name
        self.phone = phone
        self.email = email

        self.address = []

    def add_address(self,country, state, city, zipcode, address):
        self.address.append(Address(country, state, city, zipcode, address))

    def __repr__(self):
        return f"{self.name} {self.address} {self.phone} {self.email}"

    def dict(self):
        return {'first_name': self.first_name,'last_name': self.last_name,
                'phone': self.phone, 'email': self.email}

    def commit(self):
        create_private_customers(self.dict())
        for delivery_address in self.address:
            delivery_address.commit()

class Address:
    def __init__(self, country, state, city, zipcode, address):
        self.country = country
        self.state = state
        self.city = city
        self.zipcode = zipcode
        self.address = address

    def __repr__(self):
        return f"{self.country} {self.state} {self.zipcode} {self.address}"

    def dict(self):
        return {'country': self.country, 'city': self.city, 'state': self.state,
                'zipcode': self.zipcode, 'adress': self.address}

    def commit(self):
        create_delivery_adress(self.dict())

