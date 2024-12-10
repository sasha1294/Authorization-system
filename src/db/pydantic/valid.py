from pydantic import BaseModel
from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber

class User(BaseModel):
    name: str
    password: str
    phone_number: PhoneNumber
    country: str
    email: EmailStr


class OutputData(BaseModel):
    message: str
    id: int
    username: str
    email: EmailStr
    phone: PhoneNumber
    password: str
    country: str
