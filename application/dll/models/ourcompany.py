from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from application.dll.db.db import Base


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
        return f"{self.country}, {self.state}, {self.city}, {self.zipcode}, {self.adress}"


class Office(Base):
    __tablename__ = 'offices'

    idoffices = Column(Integer, primary_key=True, autoincrement=True)
    office_name = Column(String(45), nullable=False, unique=True)
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
        return f'{self.office_name} {self.city} {self.phone_number}, {self.adress}, {self.state}, {self.country}, {self.zipcode}'


class Employee(Base):
    __tablename__ = 'Employees'

    idEmployees = Column(Integer, primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(45), nullable=False)
    Jobtitle = Column(String(45))
    offices_idoffices = Column(Integer, ForeignKey('offices.idoffices'), nullable=False)

    office = relationship("Office", back_populates="employees")
    #customers = relationship('Customer', back_populates='employees')

    def __repr__(self):
        return f'{self.first_name} {self.last_name}, {self.email}, {self.phone}, {self.Jobtitle}'

