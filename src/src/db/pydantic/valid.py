from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    phone: str
    country: str
    email: str


class OutputData(BaseModel):
    message: str
    id: int
    username: str
    email:  str
    phone: str
    password: str
    country: str
