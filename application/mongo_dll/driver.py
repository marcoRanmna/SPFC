from copy import copy

from application.dll.db.db import session
from application.dll.models import Company, Product, Customer, Manufacture, Order, Supplier, Storage, Office
import application.view.mongo.mongo_models as mm


def convert_company():
    companys = session.query(Company).all()
    for company in companys:
        as_dict = copy(company.__dict__)
        del as_dict['_sa_instance_state']

        company_contact_employees = []
        for companycontactemployee in company.company_contact_employees:
            company_contact_employees.append({
                'first_name': companycontactemployee.first_name,
                'last_name': companycontactemployee.last_name,
                'phone': companycontactemployee.phone,
                'email': companycontactemployee.email
            })
        as_dict['company_contact_employees'] = company_contact_employees
        mongo_company = mm.Company(as_dict)
        mongo_company.save()


def convert_customer():
    customers = session.query(Customer).all()
    for customer in customers:
        as_dict = copy(customer.__dict__)
        del as_dict['_sa_instance_state']

        private_persons = []
        for privateperson in customer.private_persons:
            private_persons.append({
                'first_name': privateperson.first_name,
                'last_name': privateperson.last_name,
                'phone': privateperson.phone,
                'email': privateperson.email
            })
        if len(private_persons) > 0:
            as_dict['private_person'] = private_persons
        print()

        car_info = []
        for carinfo in customer.car_info:
            carinfo.append({
                'reg_number': carinfo.reg_number,
                'manufacture_name': carinfo.manufacture_name,
                'model': carinfo.model,
                'year_model': carinfo.year_model,
                'color': carinfo.color
            })
        as_dict['car_info'] = car_info

        delivery_addresses = []
        for deliveryadress in customer.delivery_addresses:
            delivery_addresses.append({
                'country': deliveryadress.country,
                'city': deliveryadress.city,
                'state': deliveryadress.state,
                'zipcode': deliveryadress.zipcode,
                'adress': deliveryadress.adress
            })
        as_dict['delivery_address'] = delivery_addresses
        mongo_customer = mm.Customer(as_dict)
        mongo_customer.save()


def convert_manufacture():
    manufactures = session.query(Manufacture).all()
    for manufacture in manufactures:
        as_dict = copy(manufacture.__dict__)
        del as_dict['_sa_instance_state']

        contact_person = []
        for manufacturecontactperson in manufacture.contact_person:
            contact_person.append({
                'phone_number': manufacturecontactperson.phone_number,
                'first_name': manufacturecontactperson.first_name,
                'last_name': manufacturecontactperson.last_name,
                'email': manufacturecontactperson.email
            })
        as_dict['contact_person'] = contact_person

        manufacture_offices = []
        for manufactureoffice in manufacture.manufacture_offices:
            manufacture_offices.append({
                'phone': manufactureoffice.phone,
                'adress': manufactureoffice.adress,
                'country': manufactureoffice.country,
                'zipcode': manufactureoffice.zipcode,
                'state': manufactureoffice.state
            })
        as_dict['manufacture_office'] = manufacture_offices
        mongo_manufacture = mm.Manufacture(as_dict)
        mongo_manufacture.save()


def convert_order():
    orders = session.query(Order).all()
    for order in orders:
        as_dict = copy(order.__dict__)
        del as_dict['_sa_instance_state']

        orderdetails = []
        for orderdetail in order.orderdetails:
            orderdetails.append({
                'product_number': orderdetail.product_number,
                'quantityordered': orderdetail.quantityordered,
                'price': orderdetail.price
            })
        mongo_order = mm.Order(as_dict)
        mongo_order.save()


def convert_product():
    products = session.query(Product).all()
    for product in products:
        as_dict = copy(product.__dict__)
        del as_dict['_sa_instance_state']

        product_stored = []
        for productstored in product.product_stored:
            product_stored.append({
                'product_stored': productstored.product_stored,
                'product_min_limit': productstored.product_min_limit,
                'product_max_limit': productstored.product_min_limit
            })
        as_dict['product_storage'] = product_stored

        component_model = []
        for carmodel in product.component_model:
            component_model.append({
                'car_brand': carmodel.car_brand,
                'car_model': carmodel.car_model,
                'car_model_year': carmodel.car_model_year
            })
        as_dict['car_model'] = component_model

        manufacture = []
        for producthasmanufacture in product.manufacture:
            manufacture.append({
                'purchase_price': producthasmanufacture.purchase_price,
                'quality_rating': producthasmanufacture.quality_rating
            })
        as_dict['manufacture_info'] = manufacture
        mongo_product = mm.Product(as_dict)
        mongo_product.save()


def convert_supplier():
    suppliers = session.query(Supplier).all()
    for supplier in suppliers:
        as_dict = copy(supplier.__dict__)
        del as_dict['_sa_instance_state']

        supplier_contact_person = []
        for suppliercontactperson in supplier.supplier_contact_person:
            supplier_contact_person.append({
                'first_name': suppliercontactperson.first_name,
                'last_name': suppliercontactperson.last_name,
                'phone': suppliercontactperson.phone,
                'email': suppliercontactperson.email
            })
        as_dict['supplier_contact_person'] = supplier_contact_person
        mongo_supplier = mm.Supplier(as_dict)
        mongo_supplier.save()


def convert_storage():
    storages = session.query(Storage).all()
    for storage in storages:
        as_dict = copy(storage.__dict__)
        del as_dict['_sa_instance_state']
        mongo_storage = mm.Storage(as_dict)
        mongo_storage.save()


def convert_office():
    offices = session.query(Office).all()
    for office in offices:
        as_dict = copy(office.__dict__)
        del as_dict['_sa_instance_state']

        employees = []
        for employee in office.employees:
            employees.append({
                'first_name': employee.first_name,
                'last_name': employee.last_name,
                'email': employee.email,
                'phone': employee.phone,
                'Jobtitle': employee.Jobtitle
            })
        as_dict['employees'] = employees
        mongo_office = mm.Office(as_dict)
        mongo_office.save()


if __name__ == '__main__':
    convert_company()
    convert_customer()
    convert_manufacture()
    convert_order()
    convert_product()
    convert_supplier()
    convert_storage()
