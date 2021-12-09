from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from application.dll.db.db import Base
from application.dll.models.offices import Office

class Storage(Base):
    __tablename__ = "Storage"

    idstorage = Column(Integer, primary_key=True, autoincrement=True)
    adress = Column(String(45), nullable=False, unique=True)
    zipcode = Column(String(45), nullable=False)
    city = Column(String(45), nullable=False)
    state = Column(String(45), nullable=False)
    country = Column(String(45), nullable=False)

    office = relationship("Office", back_populates="storage")

    def __repr__(self):
        return f"{self.country}, {self.state}, {self.city}, {self.zipcode}, {self.address}"
