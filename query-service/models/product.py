from sqlalchemy import Column, String, Float, Integer
from db.base import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Integer)
