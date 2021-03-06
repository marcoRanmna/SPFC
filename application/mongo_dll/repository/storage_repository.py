from application.view.mongo.mongo_models import Storage


def get_all_storages():
    storages = Storage.all()
    for storage in storages:
        print(storage)
        return storage

def find_storages(country):
    storages = Storage.collection.find({'country': country})
    for storage in storages:
        print(storage)
        return storage

def create_storage(adress=None, zipcode=None, city=None, state=None, country=None):
    storage = Storage({'adress': adress, 'zipcode': zipcode, 'city': city, "state": state, 'country': country})
    storage.save()


if __name__ == '__main__':
    #get_all_storages()
    find_storages('Sweden')
    create_storage()
