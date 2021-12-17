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
        'company_name': 'Snabbastebilarna AB',
        'phone_number': '0707133769',
        'email': 'snabbastebilarna@email.com'
    }
    create_companies(companies)
    #view_companies()


def delete_company():
    pass


if __name__ == '__main__':
    add_companies()
    #view_companies()
