import csv
from os import path
from datetime import datetime
from random import choice, randint
from application.bll.storage_controller import get_all_storage
from application.bll.product_storage_controller import get_all_product_storages
from application.bll.component_model_controller import get_all_car_models
from application.bll.offices_controller import get_all_offices
from application.bll.product_controller import get_all_products
from application.bll.supplier_controller import get_all_suppliers
from application.bll.manufacture_controller import get_all_manufactures
from application.bll.manufacture_office_controller import get_all_manufacture_office


class GenerateSQL:
    def __init__(self):
        working_path = path.dirname(path.realpath(__file__))
        working_path = working_path.split('SPFC')
        self.data_path = working_path[0] + "SPFC/application/dll/repository/data/"
        self.phone_numbers = set()

    def filecomplete(self, filecsv): 
        filecsv = self.data_path + filecsv
        if not path.exists(filecsv):
            print(filecsv)
            print("File not found")
            return False
        return filecsv

    def csvFileReader(self, filecsv):
        with open(filecsv, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for line in csv_reader:
                line = [c.strip() for c in line]
                yield line
        return 0

    def phone_num(self, lenght):
        while True:
            phone = "".join([str(randint(0,9)) for _ in range(lenght)])
            if phone not in self.phone_numbers:
                self.phone_numbers.add(phone)
                break
        return phone

    def component_model(self, sample_file, sample_size):
        sample_file = self.filecomplete(sample_file)
        if not sample_file:
            return "abortting..."

        from application.bll.component_model_controller import create_car_models
        for index, car_list in enumerate(self.csvFileReader(sample_file)):
            if car_list == 0 or index == sample_size:
                break
            # --- data arrangement ---
            car_list[3] = datetime.strptime(car_list[3], '%Y').year
            car_models = {
                'car_brand': car_list[1],
                'car_model': car_list[2],
                'car_model_year': car_list[3]
            }
            create_car_models(car_models)

    def storage(self, sample_file, sample_size):
        sample_file = self.filecomplete(sample_file)
        if not sample_file:
            return "abortting..."

        from application.bll.storage_controller import create_storage
        for index, storage_list in enumerate(self.csvFileReader(sample_file)):
            if storage_list == 0 or index == sample_size:
                break
            # --- data arrangement ---
            storage = {
                'adress': storage_list[0],
                'zipcode': storage_list[1],
                'city': storage_list[2],
                'state': storage_list[3],
                'country': storage_list[4]
            }
            create_storage(storage)

    def deliveryadress(self, sample_file, sample_size):
        sample_file = self.filecomplete(sample_file)
        if not sample_file:
            return "abortting..."
        from application.bll.delivery_adress_controller import create_delivery_adress
        for index, delivery_list in enumerate(self.csvFileReader(sample_file)):
            if delivery_list == 0 or index == sample_size:
                break
            delivery_adress = {
                'country': delivery_list[4],
                'city': delivery_list[2],
                'state': delivery_list[3],
                'zipcode': delivery_list[1],
                'adress': delivery_list[0],
            }
            create_delivery_adress(delivery_adress)

    def productstored(self, sample_size):
        # Imports
        from application.bll.product_storage_controller import create_product_storages

        facility_storage = get_all_storage()
        facility_storage_id = [facility.idstorage for facility in facility_storage]

        for _ in range(sample_size):
            # --- data arrangement ---
            min_limit = randint(2, 5)
            max_limit = randint(6, 20)
            product_storages = {
                'product_stored': randint(min_limit+1, max_limit),
                'product_min_limit': min_limit,
                'products_max_limit': max_limit,
                'Storage_idstorage': choice(facility_storage_id)
            }
            create_product_storages(product_storages)

    def product(self, sample_file, sample_size):
        sample_file = self.filecomplete(sample_file)
        if not sample_file:
            return "abortting..."

        from application.bll.product_controller import create_products

        product_stored = get_all_product_storages()
        car_models = get_all_car_models()

        product_stored_id = [stored.idproduct_stored for stored in product_stored]
        car_models_id = [car.idcomponent_model for car in car_models]

        for index, product_list in enumerate(self.csvFileReader(sample_file)):
            if product_list == 0 or index == sample_size:
                break

            product = {
                'product_name': product_list[0],
                'product_number': product_list[1],
                'description': "This is a product :)",
                'sell_price': float(product_list[-1]),
                'product_stored_idproduct_stored': choice(product_stored_id),
                'component_model_idcomponent_model': choice(car_models_id)
            }
            create_products(product)

    def offices(self, sample_file_1, sample_file_2, sample_size):
        sample_file_1 = self.filecomplete(sample_file_1)
        sample_file_2 = self.filecomplete(sample_file_2)
        if not(sample_file_1 and sample_file_2):
            return "abortting..." 
        
        from application.bll.offices_controller import create_offices

        facility_storage = get_all_storage()
        facility_storage_id = [facility.idstorage for facility in facility_storage]
        company_name = [company for company in self.csvFileReader(sample_file_2)]
        
        for index, office_list in enumerate(self.csvFileReader(sample_file_1)):
            if office_list == 0 or index == len(company_name) or index == sample_size:
                break
            company_line = company_name[index]
            offices = {
                'office_name': company_line[0],
                'city': office_list[2],
                'phone_number': self.phone_num(10),
                'adress': office_list[0],
                'state': office_list[3],
                'country': office_list[4],
                'zipcode': office_list[1],
                'Storage_idOffice_storage': choice(facility_storage_id)
            }
            create_offices(offices)

    def employees(self, sample_file, sample_size):
        sample_file = self.filecomplete(sample_file)
        if not sample_file:
            return "abortting..."
        
        from application.bll.employees_controller import create_employees

        offices = get_all_offices()
        offices_id = [building.idoffices for building in offices]
        
        for index, employee_list in enumerate(self.csvFileReader(sample_file)):
            if employee_list == 0 or index == sample_size:
                break

            employees = {
                'first_name': employee_list[0],
                'last_name': employee_list[1],
                'email': employee_list[2],
                'phone': employee_list[3],
                'Jobtitle': 'Seller',
                'offices_idoffices': choice(offices_id)
            }
            create_employees(employees)

    def suppliers(self, sample_file_1, sample_file_2, sample_file_3,  sample_size):
        sample_file_1 = self.filecomplete(sample_file_1)
        sample_file_2 = self.filecomplete(sample_file_2)
        sample_file_3 = self.filecomplete(sample_file_3)
        if not(sample_file_1 and sample_file_2 and sample_file_3):
            return "abortting..."
        
        from application.bll.supplier_controller import create_suppliers
        
        products = get_all_products()
        products_id = [product.idProducts for product in products]
        company_name = [company for company in self.csvFileReader(sample_file_2)]
        person_list = [person for person in self.csvFileReader(sample_file_3)]
 
        for index, supplier_list in enumerate(self.csvFileReader(sample_file_1)):
            if supplier_list == 0 or index == len(company_name) or index == sample_size:
                break

            company_line = company_name[index]
            person_line = person_list[index]
            supplier = {
                'company_name': company_line[0],
                'email': person_line[2],
                'phone': person_line[3],
                'country': supplier_list[4],
                'state': supplier_list[3],
                'zipcode': supplier_list[1],
                'city': supplier_list[2],
                'adress': supplier_list[0],
                'Products_idProducts': choice(products_id)
            }
            create_suppliers(supplier)

    def suppliers_contactpersons(self, sample_file, sample_size):
        sample_file = self.filecomplete(sample_file)
        if not sample_file:
            return "abortting..."
        
        from application.bll.supplier_contact_person_controller import create_supplier_contact_person

        suppliers = get_all_suppliers()
        suppliers_id = [supp.idSuppliers for supp in suppliers]
        
        for index, contact_person in enumerate(self.csvFileReader(sample_file)):
            if contact_person == 0 or index == sample_size:
                break

            supplier_contact_person = {
                'first_name': contact_person[0],
                'last_name': contact_person[1],
                'phone': contact_person[3],
                'email': contact_person[2],
                'Suppliers_idSuppliers': choice(suppliers_id)
            }
            create_supplier_contact_person(supplier_contact_person)

    def manufactures_extd(self, sample_file, sample_file_extd1, sample_file_extd2, sample_size):
        sample_file = self.filecomplete(sample_file)
        sample_file_extd1 = self.filecomplete(sample_file_extd1)
        sample_file_extd2 = self.filecomplete(sample_file_extd2)
        if not(sample_file and sample_file_extd1 and sample_file_extd2):
            return "abortting..."

        from application.bll.manufacture_controller import create_manufactures
        offices = []

        for index, manufactures_list in enumerate(self.csvFileReader(sample_file)):
            if manufactures_list == 0 or index == sample_size:
                break

            offices.append((manufactures_list[0], randint(1,6)))

            manufacture = {
                'company_name': offices[-1][0],
                'number_head_office': offices[-1][1]
            }
            create_manufactures(manufacture)

        manufactures_ids = []
        manufactures = get_all_manufactures()
        # -- Create manufactures_offices
        for office in offices:
            manufactures_id = [manufacture.idManufactures for manufacture in manufactures if manufacture.company_name == office[0]]
            self.manufactures_offices(sample_file_extd1, 4, manufactures_id)
            manufactures_ids.append(manufactures_id)

        # -- Create manufactures_contact_person
        for mid in manufactures_ids:
            self.manufactures_contact_person(sample_file_extd2, 4, mid[0])

    def manufactures_offices(self, sample_file, sample_size, manufactures_id):
        from application.bll.manufacture_office_controller import create_manufacture_office
        for index, manufactures_office_list in enumerate(self.csvFileReader(sample_file)):
            if manufactures_office_list == 0 or index == sample_size:
                break
            manufacture_office = {
                'phone': self.phone_num(10),
                'adress': manufactures_office_list[0],
                'country': manufactures_office_list[4],
                'zipcode': manufactures_office_list[1],
                'state': manufactures_office_list[3],
                'Manufactures_idManufactures': choice(manufactures_id)
            }
            create_manufacture_office(manufacture_office)

    def manufactures_contact_person(self, sample_file, sample_size, manufacture_id):
        from application.bll.manufacture_contact_person_controller import create_manufacture_contact_person
        offices = get_all_manufacture_office()
        offices_id = [office.idManufactures_offices for office in offices if office.Manufactures_idManufactures == manufacture_id]

        for index, contact_person in enumerate(self.csvFileReader(sample_file)):
            if contact_person == 0 or index == sample_size:
                break

            manufacture_contact_person = {
                'phone_number': self.phone_num(10),
                'first_name': contact_person[0],
                'last_name': contact_person[1],
                'email': contact_person[2],
                'Manufactures_idManufactures': manufacture_id,
                'Manufactures_offices_idManufactures_offices': choice(offices_id)
            }
            create_manufacture_contact_person(manufacture_contact_person)

    def product_has_manufactures(self, sample_size):
        from application.bll.product_has_manufacture_controller import create_product_has_manufacture

        manufactures = get_all_manufactures()
        products = get_all_products()

        manufactures_id = [manufacture.idManufactures for manufacture in manufactures]
        products_id = [product.idProducts for product in products]

        for _ in range(sample_size):
            product_has_manufacture = {
                'Products_idProducts': choice(products_id),
                'Manufactures_idManufactures': choice(manufactures_id),
                'purchase_price': float(randint(10, 10000)),
                'quality_rating': randint(1, 10)
            }
            create_product_has_manufacture(product_has_manufacture)

    def generate_all(self):
        warning = input("Are you sure?[Warning y/n]: ").strip()
        if warning == 'y':
            populate.storage('adresses.csv', 2) 
            populate.component_model('car.csv', 2) 
            populate.productstored(5) 
            populate.product('product.csv', 8) 
            populate.offices('adresses.csv', 'company.csv', 4) 
            populate.employees('person.csv', 8) 
            populate.suppliers('adresses.csv', 'company.csv', 'person.csv', 5) 
            populate.suppliers_contactpersons('person.csv', 8) 
            populate.manufactures_extd('company.csv', 'adresses.csv', 'person.csv', 5) 
            populate.product_has_manufactures(2) 
            #populate.deliveryadress('adresses.csv', 2) 

if __name__ == '__main__':
    populate = GenerateSQL()
    populate.generate_all()

