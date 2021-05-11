from ninja import Schema
from datetime import datetime

class AppointmentRegister(Schema):
    datetime: datetime
    status: str