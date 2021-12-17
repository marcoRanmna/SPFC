from application.bll.private_customer_controller import create_private_customers
from application.bll.delivery_adress_controller import create_delivery_adress, get_specific_delivery_adress
from application.bll.private_customer_controller import get_specific_private_customers
from application.bll.company_contact_employees_controller import get_specific_company_contact_employees


class Person:
    def __init__(self,first_name, last_name, phone, email, idperson=None):
        self.first_name = first_name 
        self.last_name = last_name
        self.phone = phone
        self.email = email
        
        self.idperson = idperson
        self.address = []

    def add_address(self,country, state, city, zipcode, address):
        self.address.append(Address(country, state, city, zipcode, address))

    def find_address(self, customer):
        customer_addresses = get_specific_delivery_adress(iddelivery_adress=customer.customer_obj.delivery_adress_iddelivery_adress)
        for customer_address in customer_addresses:
            self.add_address(customer_address.country, customer_address.state, customer_address.city, customer_address.zipcode, customer_address.adress)

    def __repr__(self):
        return f"{self.name} {self.address} {self.phone} {self.email}"

    def dict(self):
        return {'first_name': self.first_name,'last_name': self.last_name,
                'phone': self.phone, 'email': self.email}

    def commit(self):
        create_private_customers(self.dict())
        for delivery_address in self.address:
            delivery_address.commit()

    @classmethod
    def locate_person(cls, priv_or_corp, company_id=None):
        print("We would need you provide who are you information?")
        while True:
            first_name = input("Your first name: ").strip()
            last_name = input("Your last name: ").strip()
            phone = input("Your phone number: ").strip()
            email = input("Your email address: ").strip()
            if priv_or_corp == "1":
                whoami = get_specific_private_customers(first_name=first_name, last_name=last_name, phone=phone, email=email)
            else:
                whoami = get_specific_company_contact_employees(Company_idContactPersons=company_id, first_name=first_name, last_name=last_name, phone=phone, email=email)
            if len(whoami)>0:
                whoami = whoami[0]
                break
        if priv_or_corp == "1":
            return Person(whoami.first_name, whoami.last_name, whoami.phone, whoami.email, idperson=whoami.idprivate_person)
        else:
            return Person(whoami.first_name, whoami.last_name, whoami.phone, whoami.email, idperson=company_id)


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
