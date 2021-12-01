from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship

from application.dll.db.db import Base


class PrivatePerson(Base):
    __tablename__ = 'private_person'

    idprivate_person = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(VARCHAR(45), nullable=False)
    last_name = Column(VARCHAR(45), nullable=False)
    phone = Column(VARCHAR(45), nullable=False)
    email = Column(VARCHAR(45), nullable=False)
    costumer = relationship('Costumer', back_populates='private_persons')

    def __repr__(self):
        return f'{self.idprivate_person}, {self.first_name}, {self.last_name}, {self.phone}, {self.email}'
