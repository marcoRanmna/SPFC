from application.bll.company_contact_employees_controller import get_all_company_contact_employees, create_company_contact_employees


def view_company_contact_employees():
    company_contact_employee = get_all_company_contact_employees()
    print("***********")
    print("All Company Contact Employees")
    print("***********")
    print()
    for cce in company_contact_employee:
        print(cce)


def add_company_contact_employees():
    company_contact_employees = {
        'Company_idContactPersons': '',
        'first_name': '',
        'last_name': '',
        'phone': '',
        'email': ''
    }
    create_company_contact_employees(company_contact_employees)


def delete_company_contact_employee():
    pass

if __name__ == '__main__':
    add_company_contact_employees()
    #view_company_contact_employees()
