from application.dll.repository import product_storage_repository as ps_r


def get_all_product_storages():
    return ps_r.get_all_product_storages()


def create_product_storages(product_storages):
    ps_r.create_product_storages(product_storages)
