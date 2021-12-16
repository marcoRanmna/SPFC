from application.dll.repository import supplier_repository as supplier_r


def get_all_suppliers():
    return supplier_r.get_all_suppliers()


def create_suppliers(supplier):
    supplier_r.create_suppliers(supplier)
