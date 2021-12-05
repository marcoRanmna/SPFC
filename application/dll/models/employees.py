from sqlalchemy import Column, Integer, String, ForeignKey

from application.dll.db.db import Base


class Employees(Base):
    __tablename__ = 'Employees'

    idEmployees = Column(Integer, primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(45), nullable=False)
    Jobtitle = Column(String(45))
    offices_idoffices = Column(Integer, ForeignKey('offices.idoffices'), nullable=False)
    boss = Column(Integer, ForeignKey('Employees.idEmployees'))

    def __repr__(self):
        return f'{self.first_name} {self.last_name}, {self.email}, {self.phone}, {self.Jobtitle}'