from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from application.dll.db.db import Base
from application.dll.models.storage import Storage
from application.dll.models.employees import Employee


class Office(Base):
    __tablename__ = 'offices'

    idoffices = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(100), nullable=False)
    phone_number = Column(String(45), nullable=False)
    adress = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    zipcode = Column(Integer, nullable=False)
    Storage_idOffice_storage = Column(ForeignKey('Storage.idstorage'), nullable=False)

    storage = relationship("Storage", back_populates='office')
    employees = relationship("Employee", back_populates="office")

    def __repr__(self):
        return f'{self.city} {self.phone_number}, {self.adress}, {self.state}, {self.country}, {self.zipcode}'
