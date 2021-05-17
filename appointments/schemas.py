from ninja import Schema
from datetime import datetime

class AppointmentIn(Schema):
    datetime: datetime
    status: str
    user_id: int
    property_id: int

class AppointmentOut(Schema):
    id: int
    datetime: datetime
    status: str
    user_id: int
    property_id: int
    