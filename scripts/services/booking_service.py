from fastapi import HTTPException
from scripts.models.models import Booking, FitnessClass
from scripts.handler.db import SessionLocal
from scripts.schemas.schemas import BookingRequest
import logging

logger = logging.getLogger("booking_service")

def book_class(request: BookingRequest):
    db = SessionLocal()
    try:
        # Fetch the fitness class by ID
        fitness_class = db.query(FitnessClass).filter(FitnessClass.id == request.class_id).first()
        if not fitness_class:
            logger.warning(f"Class not found: {request.class_id}")
            # Raise 404 if class does not exist
            raise HTTPException(status_code=404, detail="Class not found")

        # Check if there are available slots
        if fitness_class.available_slots <= 0:
            logger.warning(f"Overbooking attempt: {request.class_id}")
            # Raise 400 if no slots are available
            raise HTTPException(status_code=400, detail="No available slots")

        # Decrement available slots
        fitness_class.available_slots -= 1
        # Create a new booking
        booking = Booking(**request.model_dump())
        db.add(booking)
        db.commit()
        db.refresh(booking)
        logger.info(f"Booked class {request.class_id} for {request.client_email}")
        return booking

    except Exception as e:
        db.rollback()
        logger.error(f"Booking error: {e}")
        # Raise 500 on unexpected errors
        raise HTTPException(status_code=500, detail="Booking failed")

    finally:
        db.close()

def get_bookings(client_email: str):
    db = SessionLocal()
    try:
        # Fetch all bookings for the given client email
        return db.query(Booking).filter(Booking.client_email == client_email).all()
    except Exception as e:
        logger.error(f"Fetch booking error: {e}")
        # Raise 500 on unexpected errors
        raise HTTPException(status_code=500, detail="Could not fetch bookings")
    finally:
        db.close()
