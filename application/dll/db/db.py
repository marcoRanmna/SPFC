import sqlalchemy
from CONFIG import *
from sqlalchemy import text
from sqlalchemy.orm import declarative_base, sessionmaker

engine = sqlalchemy.create_engine(f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/SPFCdb", echo=True)

with engine.connect() as conn:
    print(conn.scalar(text("select 'hi'")))

Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

