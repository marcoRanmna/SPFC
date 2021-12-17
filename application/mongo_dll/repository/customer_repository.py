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


if __name__ == '__main__':
    get_all_customers()
    find_customers('')