from pydantic import BaseModel, EmailStr, Field


class BookingRequest(BaseModel):
    class_id: int = Field(..., gt=0)
    client_name: str = Field(..., min_length=1)
    client_email: EmailStr


class BookingResponse(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr

    model_config = {"from_attributes": True}


class ClassOut(BaseModel):
    id: int
    name: str
    date: str      
    time: str        
    instructor: str
    available_slots: int

    model_config = {"from_attributes": True}
