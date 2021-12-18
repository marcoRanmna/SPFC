from application.bll.offices_controller import get_specific_offices, get_all_offices
from application.bll.employees_controller import get_specific_employees
from application.bll.product_controller import get_specific_products
from application.bll.product_has_manufacture_controller import get_specific_products_has_manufactures
from application.bll.manufacture_controller import get_specific_manufactures
from application.bll.manufacture_office_controller import get_specific_manufacture_office


class Employee:
    def __init__(self, employee_obj):
        self.employee_obj = employee_obj
    
    def search_product(self, check_products):
        for product in check_products:
            junctions = get_specific_products_has_manufactures(Products_idProducts=product.idProducts)
            for junction in junctions:
                manufacures = get_specific_manufactures(idManufactures=junction.Manufactures_idManufactures)
                for manufacture in manufacures:
                    office = get_specific_manufacture_office(Manufactures_idManufactures=manufacture.idManufactures)[0]
                    contact_person = get_specific_manufacture_office(Manufactures_idManufactures=manufacture.idManufactures)[0]
                    print("+"+("-"*50)+"+")
                    print("|", f"{product.product_name}  Left: {product.quantity}".ljust(50), "|")
                    print("|", f"Manufactured by {manufacures.company_name}".ljust(50), "|")
                    print("|", f"Office Phone: {office.phone}".ljust(50), "|")
                    print("|", f"Contact Person: {contact_person.first_name} {contact_person.last_name}".ljust(50), "|")
                    print("|", f"Phone: {contact_person.phone_number}".ljust(50), "|")
                    print("+"+("-"*50)+"+")


    @classmethod
    def whoareyou(cls):
        while True:
            for office in get_all_offices():
                print(office.office_name)
            office_name = input("\nWhat office branch name are you from?\n> ").strip()
            office = get_specific_offices(office_name=office_name)
            if len(office) > 0:
                office = office[0]
                break
            print("Wrong office!")

        print("WHO ARE YOU?")
        while True:
            first_name = input("first_name: ").strip()
            last_name = input("last_name: ").strip()
            email = input("email: ").strip()
            phone = input("phone: ").strip()
            employee = get_specific_employees(first_name=first_name, last_name=last_name, email=email, phone=phone, offices_idoffices=office.idoffices)
            if len(employee) > 0:
                employee = employee[0]
                return Employee(employee)
            for emp in get_specific_employees(offices_idoffices=office.idoffices):
                print(emp)

