from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from application.dll.db.db import Base

class Storage(Base):
    __tablename__ = "Storage"

    idstorage = Column(Integer, primary_key=True)
    adress = Column(String(45))
    zipcode = Column(String(45))
    city = Column(String(45))
    state = Column(String(45))
    country = Column(String(45))

    def __repr__(self):
        return f"{self.country}, {self.state}, {self.city}, {self.zipcode}, {self.address}"
