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

if __name__ == '__main__':
    #get_all_offices()
    find_offices('3M Company')