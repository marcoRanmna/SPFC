from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from application.dll.db.db import Base


class Product_Stored(Base):
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
