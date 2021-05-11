from ninja import Schema
from datetime import date

class PropertyOut(Schema):
    id: int
    price: int
    description: str

class PropertyRegister(Schema):
    price: int
    description: str
    status: str
    water: bool
    electricity: bool
    sewer: bool