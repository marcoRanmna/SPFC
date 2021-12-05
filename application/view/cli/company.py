from application.bll.company_controller import get_all_companies, create_companies


def view_companies():
    companies = get_all_companies()
    print("***********")
    print("All Companies")
    print("***********")
    print()
    for company in companies:
        print(company)


def add_companies():
    companies = {
        'company_name': '',
        'phone_number': '',
        'email': ''
    }
    create_companies(companies)


def delete_company():
    pass
