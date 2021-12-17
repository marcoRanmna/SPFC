from application.view.mongo.mongo_models import Manufacture


def get_all_manufactures():
    manufactures = Manufacture.all()
    for manufacture in manufactures:
        print(manufacture)
        return manufacture

def find_manufactures(company_name):
    manufactures = Manufacture.collection.find({'company_name': company_name})
    for manufacture in manufactures:
        print(manufacture)
        return manufacture


if __name__ == '__main__':
    #get_all_manufactures()
    find_manufactures('3Com Corp')