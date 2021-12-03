from application.bll.company_contact_employees_controller import get_all_company_contact_employees


def view_company_contact_employees():
    company_contact_employee = get_all_company_contact_employees()
    print("***********")
    print("All Company Contact Employees")
    print("***********")
    print()
    for cce in company_contact_employee:
        print(cce)


def add_company_contact_employee():
    pass


def delete_company_contact_employee():
    pass
