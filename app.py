from fastapi import FastAPI
from scripts.routers import classes, bookings
from scripts.handler.db import init_db

app = FastAPI(
    title="Fitness Studio Booking API",
    description="API for booking Yoga, Zumba, and HIIT classes.",
    version="1.0.0"
)

init_db() 

app.include_router(classes.router, prefix="/classes", tags=["Classes"])
app.include_router(bookings.router, prefix="/book", tags=["Bookings"])
