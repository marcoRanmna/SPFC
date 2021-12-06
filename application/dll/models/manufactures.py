from sqlalchemy import Column, Integer, String

from application.dll.db.db import Base


class Manufacture(Base):
    __tablename__ = 'Manufactures'

    idManufacture = Column(Integer, primary_key=True)
    company_name = Column(String(45), nullable=False, unique=True)
    number_head_office = Column(Integer, nullable=True)

    def __repr__(self):
        return f'{self.idManufacture},{self.company_name}, {self.number_head_office}'
