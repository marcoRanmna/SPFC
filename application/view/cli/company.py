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
        'company_name': 'Snabbabilar AB',
        'phone_number': '0707005476',
        'email': 'snabbabilar@email.com'
    }
    create_companies(companies)
    #view_companies()


def delete_company():
    pass


if __name__ == '__main__':
    add_companies()
