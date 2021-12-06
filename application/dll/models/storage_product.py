from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from application.dll.db.db import Base


class Storage(Base):
    __tablename__ = "Storage"

    idstorage = Column(Integer, primary_key=True)
    address = Column(String(45))
    zipcode = Column(String(45))
    city = Column(String(45))
    state = Column(String(45))
    country = Column(String(45))
    storage = relationship("Product_Stored", back_populates="storage")

    def __repr__(self):
        return f"{self.country}, {self.state}, {self.city}, {self.zipcode}, {self.address}"


class ProductStored(Base):
    __tablename__ = "product_stored"

    idproduct_stored = Column(Integer, primary_key=True)
    product_stored = Column(Integer)
    product_min_limit = Column(Integer)
    product_max_limit = Column(Integer)
    storage_idstorage = Column(ForeignKey("Storage.idstorage"), nullable=False)

    storage = relationship("Storage", back_populates="storage")
    product = relationship("Product", back_populates="product_stored")

    def __repr__(self):
        return f"{self.product_stored}, limit {self.product_min_limit} {self.product_max_limit}"
