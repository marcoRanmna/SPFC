from application.view.mongo.mongo_models import Company


def get_all_companys():
    companys = Company.all()
    for company in companys:
        print(company)
        return company


def find_companys(company_name):
    companys = Company.collection.find({'company_name': company_name})
    for company in companys:
        print(company)
        return company


if __name__ == '__main__':
    #get_all_companys()
    find_companys('Snabbastebilarna AB')