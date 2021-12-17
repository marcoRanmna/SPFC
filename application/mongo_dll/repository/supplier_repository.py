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

if __name__ == '__main__':
    get_all_suppliers()
