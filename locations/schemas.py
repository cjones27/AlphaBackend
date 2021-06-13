from ninja import Schema
from datetime import date
# from locations.schemas import RegionOut

class RegionOut(Schema):
    id: int
    name: str

class CommuneOut(Schema):
    id: int
    name: str
    region: RegionOut