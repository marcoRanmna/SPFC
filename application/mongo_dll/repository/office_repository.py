from application.view.mongo.mongo_models import Office


def get_all_offices():
    offices = Office.all()
    for office in offices:
        print(office)
        return office


def find_offices(office_name):
    offices = Office.collection.find({'office_name': office_name})
    for office in offices:
        print(office)
        return office

def create_office(office_name=None, city=None, phone_number=None, adress=None, state=None, country=None, zipcode=None, Storage_idOffice_storage=None, employees=None):
    office = Office({'office_name': office_name, 'city': city, 'phone_number': phone_number, 'adress': adress, 'state': state, 'country': country, 'zipcode': zipcode, 'Storage_idOffice_storage': Storage_idOffice_storage, 'employees': employees})
    office.save()

if __name__ == '__main__':
    #get_all_offices()
    find_offices('3M Company')
    create_office()