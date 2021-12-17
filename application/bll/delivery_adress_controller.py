from application.dll.repository import delivery_adress_repository as da_r


def get_all_delivery_adress():
    return da_r.get_all_delivery_adress()

def get_specific_delivery_adress(iddelivery_adress=None, country=None, city=None, state=None, zipcode=None, adress=None):
    return da_r.get_specific_delivery_adress(iddelivery_adress, country, city, state, zipcode, adress)

def create_delivery_adress(delivery_adress):
    da_r.create_delivery_adress(delivery_adress)
