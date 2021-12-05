from application.dll.db.db import session
from application.dll.models.offices import Office


def get_all_offices():
    return session.query(Office).all()


def create_offices(offices):
    offices = Office(**offices)
    session.add(offices)
    session.commit()
