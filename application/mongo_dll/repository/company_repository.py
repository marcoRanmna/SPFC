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

def create_company(company_name=None, phone_number=None, email=None, employees=None):
    company = Company({'company_name': company_name, 'phone_number': phone_number, 'email': email, "company_contact_employees": employees})
    company.save()



if __name__ == '__main__':
    #get_all_companys()
    #find_companys('Snabbastebilarna AB')
    employees = [{
        "first_name": "Kalle",
        "last_name": "Eriksson",
        "phone": "0707070707",
        "email": "erik@email.com"
    }]
    create_company('Snabbbil', '', 'snabbbil@email.com', employees)
