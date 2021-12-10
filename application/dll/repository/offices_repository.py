from application.dll.db.db import session
from application.dll.models import Office, Storage


def get_all_offices():
    return session.query(Office).all()


def create_offices(offices):
    facillity = session.query(Storage).filter_by(adress="Anders Personsgatan 14").one()
    offices = Office(office_name=offices['name'],city=offices['city'], 
            phone_number=offices['phone_number'],
            adress=offices['adress'],
            state=offices['state'],
            country=offices['country'],
            zipcode=offices['zipcode'],
            Storage_idOffice_storage=facillity.idstorage)
    session.add(offices)
    session.commit()
