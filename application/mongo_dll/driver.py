import csv
import datetime
from os import path

from application.dll.db.db import session
from application.dll.models import Company, Product, Customer, Manufacture, Order, Supplier, Storage
import application.dll.models as mm



def convert_company():
    companys = session.query(Company).all()
    for company in companys:
        as_dict = company.__dict__
        del as_dict['_sa_instance_state']
        mongo_company = mm.Company(as_dict)
        #print()
        mongo_company.save()


def test_convert_company():
    dir_path = 'C:/Python project/SPFC/application/dll/repository/data/'
    company_file = dir_path + 'company.csv'
    # print(company_file, path.exists(company_file))

    with open(company_file, 'r', encoding='utf-8') as file_csv:
        csv_reader = csv.reader(file_csv)
        next(csv_reader)
        company_list = next(csv_reader)
    # print(company_list)

    dir_path2 = 'C:/Python project/SPFC/application/dll/repository/data/'
    company_file2 = dir_path2 + 'person.csv'
    # print(company_file2, path.exists(company_file2))

    with open(company_file2, 'r', encoding='utf-8') as file_csv2:
        csv_reader2 = csv.reader(file_csv2)
        next(csv_reader2)
        phone_num_list = next(csv_reader2)
    # print(phone_num_list)

    company = {
        'company_name': company_list[0],
        'phone_number': phone_num_list[-1],
        'email': phone_num_list[2]
    }
    # convert_company()

def convert_customer():
    customers = session.query(Customer).all()
    for customer in customers:
        as_dict = customer.__dict__
        del as_dict['_sa_instance_state']
        mongo_customer = mm.Customer(as_dict)
        #print()
        mongo_customer.save()

def convert_manufacture():
    manufactures = session.query(Manufacture).all()
    for manufacture in manufactures:
        as_dict = manufacture.__dict__
        del as_dict['_sa_instance_state']
        mongo_manufacture = mm.Manufacture(as_dict)
        #print()
        mongo_manufacture.save()

def convert_order():
    orders = session.query(Order).all()
    for order in orders:
        as_dict = order.__dict__
        del as_dict['_sa_instance_state']
        mongo_order = mm.Order(as_dict)
        #print()
        mongo_order.save()

def convert_product():
    products = session.query(Product).all()
    for product in products:
        as_dict = product.__dict__
        del as_dict['_sa_instance_state']
        mongo_product = mm.Product(as_dict)
        # print()
        mongo_product.save()

def convert_supplier():
    suppliers = session.query(Supplier).all()
    for supplier in suppliers:
        as_dict = supplier.__dict__
        del as_dict['_sa_instance_state']
        mongo_supplier = mm.Supplier(as_dict)
        # print()
        mongo_supplier.save()

def convert_storage():
    storages = session.query(Storage).all()
    for storage in storages:
        as_dict = storage.__dict__
        del as_dict['_sa_instance_state']
        mongo_storage = mm.Storage(as_dict)
        # print()
        mongo_storage.save()

if __name__ == '__main__':
    # convert_company()
    convert_product()
