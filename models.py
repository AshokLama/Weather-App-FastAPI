from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    temperature = Column(Float)
    description = Column(String)