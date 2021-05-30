from ninja import Schema
from datetime import date
from uuid import UUID

class UserRegister(Schema):
    first_name: str 
    last_name: str
    user_type: int
    date_of_birth: date=None
    email: str
    password: str


class UserOut(Schema):
    id: int
    first_name: str
    last_name: str
    email: str
    user_type: int
    api_key: UUID

class UserOutPublic(Schema):
    id: int
    first_name: str
    last_name: str

class LogIn(Schema):
    email: str
    password: str

class Message(Schema):
    message: str