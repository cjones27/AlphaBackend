from ninja import Schema
from datetime import date
from uuid import UUID

class UserRegister(Schema):
    # Lo que entra a la request
    first_name: str 
    last_name: str
    user_type: int
    date_of_birth: date=None
    email: str
    password: str


class UserOut(Schema):
    # Lo que se entrega en la request
    id: int
    first_name: str
    last_name: str
    email: str
    user_type: int
    api_key: UUID

class LogIn(Schema):
    email: str
    password: str

class Message(Schema):
    message: str