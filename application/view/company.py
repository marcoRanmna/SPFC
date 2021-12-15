from application.view.persons import Person
from application.bll.company_controller import create_companies
from application.bll.company_contact_employees_controller import create_company_contact_employees
from application.dll.db.db import session
from application.dll.models import Company as TableCompany

class Company:
    def __init__(self, corp_name, corp_email, corp_phone):
        self.corp_name = corp_name
        self.corp_email = corp_email
        self.corp_phone = corp_phone
        
        self.contact_persons = []

    def company_dict(self):
        return {'company_name': self.corp_name, 'phone_number': self.corp_phone,'email':self.corp_email}

    def commit(self):
        print(self.company_dict())
        create_companies(self.company_dict())
        corp = session.query(TableCompany).filter_by(company_name=self.corp_name, phone_number=self.corp_phone, email=self.corp_email).first()
        for person in self.contact_persons:
            pd = person.dict()
            pd['Company_idContactPersons'] = corp.idContactPersons
            create_company_contact_employees(pd)
            for address in person.address:
                address.commit()

    @classmethod
    def coperate_hello(cls):
        print("Hello,\nHere at Evil Corp we want you to be provid with the best of care.")
        corp_name = input("What would your company name be?: ")
        print("Thank you, now all we need its your company email, phone so we can begin a trusted transaction")
        company_email = input("Your coperations head email: ")
        company_phone = input("Your coperations head phone: ")
        return Company(corp_name, company_email, company_phone)
