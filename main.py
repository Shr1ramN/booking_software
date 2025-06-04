import logging
import uvicorn
from fastapi import FastAPI
from scripts.routers import bookings, classes

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

app = FastAPI()
app.include_router(bookings.router, prefix="/book", tags=["Bookings"])
app.include_router(classes.router, prefix="/classes", tags=["Classes"])


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
