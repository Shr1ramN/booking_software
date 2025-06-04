from fastapi import APIRouter
from typing import List
from scripts.schemas.schemas import ClassOut
from scripts.services import class_service

router = APIRouter()

@router.get("/", response_model=List[ClassOut])
def get_classes():
    """
    Handles GET requests to retrieve a list of all classes.

    Returns:
        List[ClassOut]: A list of class objects as defined by the ClassOut schema.
    """
    return class_service.get_all_classes()
