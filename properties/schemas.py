from django.contrib.postgres.fields import array
from ninja import Schema
from datetime import date
from users.schemas import UserOutPublic
from typing import List

class PropertyOut(Schema):
    id: int
    title: str
    price: int
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
    coordinates: List[List[float]]

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
    photos_urls: List[str]
    coordinates: List[List[float]]