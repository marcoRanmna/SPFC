import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker


engine = sqlalchemy.create_engine(
    f"mysql+mysqlconnector://root:password@localhost:3307/SPFCdb"
)

Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
