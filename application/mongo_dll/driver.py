from copy import copy

from application.dll.db.db import session
from application.dll.models import Company, Product, Customer, Manufacture, Order, Supplier, Storage
import application.view.mongo.mongo_models as mm


def convert_company():
    companys = session.query(Company).all()
    for company in companys:
        as_dict = copy(company.__dict__)
        del as_dict['_sa_instance_state']
        mongo_company = mm.Company(as_dict)
        mongo_company.save()


def convert_customer():
    customers = session.query(Customer).all()
    for customer in customers:
        as_dict = copy(customer.__dict__)
        del as_dict['_sa_instance_state']
        mongo_customer = mm.Customer(as_dict)
        mongo_customer.save()


def convert_manufacture():
    manufactures = session.query(Manufacture).all()
    for manufacture in manufactures:
        as_dict = copy(manufacture.__dict__)
        del as_dict['_sa_instance_state']
        mongo_manufacture = mm.Manufacture(as_dict)
        mongo_manufacture.save()


def convert_order():
    orders = session.query(Order).all()
    for order in orders:
        as_dict = copy(order.__dict__)
        del as_dict['_sa_instance_state']
        mongo_order = mm.Order(as_dict)
        mongo_order.save()


def convert_product():
    products = session.query(Product).all()
    for product in products:
        as_dict = copy(product.__dict__)
        del as_dict['_sa_instance_state']
        mongo_product = mm.Product(as_dict)
        mongo_product.save()


def convert_supplier():
    suppliers = session.query(Supplier).all()
    for supplier in suppliers:
        as_dict = copy(supplier.__dict__)
        del as_dict['_sa_instance_state']
        mongo_supplier = mm.Supplier(as_dict)
        mongo_supplier.save()


def convert_storage():
    storages = session.query(Storage).all()
    for storage in storages:
        as_dict = copy(storage.__dict__)
        del as_dict['_sa_instance_state']
        mongo_storage = mm.Storage(as_dict)
        mongo_storage.save()


if __name__ == '__main__':
    convert_company()
    convert_customer()
    convert_manufacture()
    convert_order()
    convert_product()
    convert_supplier()
    convert_storage()
