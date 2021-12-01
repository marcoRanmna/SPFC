import sqlalchemy
from CONFIG import *
from sqlalchemy.orm import declarative_base, sessionmaker

engine = sqlalchemy.create_engine(f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/SPFCdb")

Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

