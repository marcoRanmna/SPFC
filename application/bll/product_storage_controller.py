from application.dll.repository import product_storage_repository as ps_r


def get_all_product_storages():
    return ps_r.get_all_product_storages()

def get_specific_product_storages(idproduct_stored=None, product_stored=None, product_min_limit=None, products_max_limit=None, Storage_idstorage=None):
    return ps_r.get_specific_product_storages(idproduct_stored, product_stored, product_min_limit, products_max_limit, Storage_idstorage)

def create_product_storages(product_storages):
    ps_r.create_product_storages(product_storages)

def subtract_quantity(table_id, sub):
    ps_r.subtract_quantity(table_id, sub)
