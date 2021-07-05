from ninja import Schema
from datetime import date
from users.schemas import UserOutPublic
from typing import List
from locations.schemas import CommuneOut

class PropertyOut(Schema):
    id: int
    title: str
    price: int
    commune: CommuneOut
    description: str
    status: str
    user: UserOutPublic
    water: bool
    electricity: bool
    sewer: bool
    area: float
    contact: str
    address: str
    photos_urls: List[str]
    coordinate1: List[float]
    coordinate2: List[float]
    coordinate3: List[float]
    coordinate4: List[float]

class PropertyRegister(Schema):
    title: str
    price: int
    description: str
    status: str
    commune: int
    area: float
    contact: str
    address: str
    water: bool
    electricity: bool
    sewer: bool
    photos_urls: List[str]
    coordinate1: List[float]
    coordinate2: List[float]
    coordinate3: List[float]
    coordinate4: List[float]