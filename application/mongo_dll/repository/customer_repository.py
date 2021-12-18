from application.view.mongo.mongo_models import Customer


def get_all_customers():
    customers = Customer.all()
    for customer in customers:
        print(customer)
        return customer

def find_customers(created):
    customers = Customer.collection.find({'created': created})
    for customer in customers:
        print(customer)
        return customer


def create_customers(created=None, private_person_or_company=None, Company_idContactPersons=None, Employees_idEmployees=None, private_person_idprivate_person=None, delivery_adress_iddelivery_adress=None, private_persons=None, car_info=None, delivery_addresses=None):
    customer = Customer({'created': created, 'private_person_or_company': private_person_or_company, 'Company_idContactPersons': Company_idContactPersons, "Employees_idEmployees": Employees_idEmployees, 'private_person_idprivate_person': private_person_idprivate_person, 'delivery_adress_iddelivery_adress': delivery_adress_iddelivery_adress, 'private_persons': private_persons, 'car_info': car_info, 'delivery_addresses': delivery_addresses})
    customer.save()



if __name__ == '__main__':
    #get_all_customers()
    #find_customers('')
    private_persons =[{
        "first_name": "Kalle",
        "last_name": "Eriksson",
        "phone": "0707070707",
        "email": "erik@email.com"
    }]
    car_info = [{
        "reg_number": "asd123",
        "manufacture_name": "Porsche",
        "model": "Panamera 4S",
        "year_model": "2013",
        "color": "blue"
    }]
    delivery_addresses = [{
        "country": "Sweden",
        "city": "Gothenburg",
        "state": "Vastra Gotaland",
        "zipcode": "43540",
        "adress": "Furugatan 1"

    }]
    create_customers('2020-12-12', True, '', '', '', 1, private_persons, car_info, delivery_addresses)