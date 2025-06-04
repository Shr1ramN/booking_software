import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from scripts.models import Base
from scripts.models.models import FitnessClass

# Load environment variables from .env file
load_dotenv()

# Read database URL from environment, fallback to SQLite if missing
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Create database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """Initialize database schema and insert default fitness classes."""
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    if not session.query(FitnessClass).first():
        from datetime import datetime, timedelta

        now = datetime.now()
        session.add_all([
            FitnessClass(
                name="Yoga",
                datetime=now + timedelta(days=1, hours=9),
                instructor="Alice",
                available_slots=10
            ),
            FitnessClass(
                name="Zumba",
                datetime=now + timedelta(days=2, hours=18),
                instructor="Bob",
                available_slots=15
            ),
            FitnessClass(
                name="HIIT",
                datetime=now + timedelta(days=3, hours=7),
                instructor="Charlie",
                available_slots=5
            ),
        ])
        session.commit()
    session.close()
