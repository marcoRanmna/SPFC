from application.view.mongo.mongo_models import Supplier


def get_all_suppliers():
    suppliers = Supplier.all()
    for supplier in suppliers:
        print(supplier)
        return supplier

def find_suppliers(company_name):
    suppliers = Supplier.collection.find({'company_name': company_name})
    for supplier in suppliers:
        print(supplier)
        return supplier

def create_supplier(company_name=None, email=None, phone=None, country=None, state=None, zipcode=None, city=None, adress=None, Products_idProduct=None, supplier_contact_person=None):
    supplier = Supplier({'company_name': company_name, 'email': email, 'phone': phone, "country": country, 'state': state, 'zipcode': zipcode, 'city': city, 'adress': adress, 'Products_idProduct': Products_idProduct, 'supplier_contact_person': supplier_contact_person})
    supplier.save()

if __name__ == '__main__':
    get_all_suppliers()
    #find_suppliers()
    create_supplier()
