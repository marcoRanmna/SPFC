from application.dll.repository import delivery_adress_repository as da_r


def get_all_delivery_adress():
    return da_r.get_all_delivery_adress()


def create_delivery_adress(delivery_adress):
    da_r.create_delivery_adress(delivery_adress)
