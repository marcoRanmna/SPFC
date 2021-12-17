from application.dll.repository import carinfo_repository as carinfo_r


def get_all_carinfo():
    return carinfo_r.get_all_carinfo()

def get_specific_carinfo(idCarinfo=None, reg_number=None, manufacture_name=None, model=None, year_model=None, color=None, Customers_idCustomers=None):
    return carinfo_r.get_specific_carinfo(idCarinfo, reg_number, manufacture_name, model, year_model, color, Customers_idCustomers)

def create_carinfo(carinfo):
    carinfo_r.create_carinfo(carinfo)
