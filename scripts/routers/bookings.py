from fastapi import APIRouter
from typing import List
from scripts.schemas.schemas import BookingRequest, BookingResponse
from scripts.services import booking_service

router = APIRouter()

@router.post("/", response_model=BookingResponse)
def book_class(request: BookingRequest):
    """
    Endpoint to book a class.
    Accepts a BookingRequest and returns a BookingResponse.
    """
    return booking_service.book_class(request)

@router.get("/", response_model=List[BookingResponse])
def get_bookings(client_email: str):
    """
    Endpoint to retrieve all bookings for a given client email.
    Returns a list of BookingResponse objects.
    """
    return booking_service.get_bookings(client_email)
