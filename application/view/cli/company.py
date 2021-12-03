from application.bll.company_controller import get_all_companies


def view_companys():
    companies = get_all_companies()
    print("***********")
    print("All Companys")
    print("***********")
    print()
    for company in companies:
        print(company)


def add_company():
    pass


def delete_company():
    pass
