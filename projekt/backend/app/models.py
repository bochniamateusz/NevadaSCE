from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, nullable=True)
    car_id = Column(String, nullable=False)
    zone = Column(String, nullable=True)
    zone_number = Column(String, nullable=True)
