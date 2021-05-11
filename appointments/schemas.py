from ninja import Schema
from datetime import date, datetime

class AppointmentRegister(Schema):
    datetime: datetime
    status: str