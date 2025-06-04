from sqlalchemy import Column, Integer, String, DateTime
from scripts.models import Base

class FitnessClass(Base):
    __tablename__ = "fitness_classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    datetime = Column(DateTime)
    instructor = Column(String)
    available_slots = Column(Integer)


class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    class_id = Column(Integer)
    client_name = Column(String)
    client_email = Column(String)
