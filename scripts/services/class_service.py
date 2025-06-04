from scripts.models.models import FitnessClass
from scripts.handler.db import SessionLocal
from fastapi import HTTPException
import pytz
from datetime import datetime
import logging

logger = logging.getLogger("class_service")

def get_all_classes():
    """
    Fetch all fitness classes from the database, convert their datetime to Asia/Kolkata timezone,
    and return a list of class details with formatted date and time.
    """
    db = SessionLocal()
    try:
        # Query all FitnessClass records from the database
        classes = db.query(FitnessClass).all()

        ist = pytz.timezone("Asia/Kolkata")
        output = []

        for cls in classes:
            # Convert class datetime to IST timezone
            ist_dt = cls.datetime.astimezone(ist)
            # Append class details to output list
            output.append({
                "id": cls.id,
                "name": cls.name,
                "date": ist_dt.strftime("%Y-%m-%d"),
                "time": ist_dt.strftime("%I:%M %p"),
                "instructor": cls.instructor,
                "available_slots": cls.available_slots,
            })

        return output

    except Exception as e:
        # Log any errors and raise HTTP 500 error
        logger.error(f"Fetch class error: {e}")
        raise HTTPException(status_code=500, detail="Could not fetch classes")
    finally:
        # Ensure the database session is closed
        db.close()
