from ninja import Schema
from datetime import date
from users.schemas import UserOut

class PropertyOut(Schema):
    id: int
    title: str
    price: int
    description: str
    status: str
    user: UserOut
    water: bool
    electricity: bool
    sewer: bool
    area: float
    contact: str
    address: str

class PropertyRegister(Schema):
    title: str
    price: int
    description: str
    status: str
    area: float
    contact: str
    address: str
    water: bool
    electricity: bool
    sewer: bool