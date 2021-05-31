from ninja import Schema
from datetime import datetime
from users.schemas import UserOutPublic

class AppointmentIn(Schema):
    datetime: datetime
    status: str
    user_id: int
    property_id: int

class AppointmentOut(Schema):
    id: int
    datetime: datetime
    status: str
    user: UserOutPublic
    property_id: int

class AppointmentOutPublic(Schema):
    id: int
    datetime: datetime
    status: str
    property_id: int
    