from pydantic import BaseModel

class User_model(BaseModel):
    name: str
    password: str
    phone_number: int
    country: str
    email: str

class Output_data(BaseModel):
    message: str
    id: int
    username: str
    email: str
    phone: int
    password: str
    country: str
