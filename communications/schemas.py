from ninja import Schema
from datetime import datetime

class MessageOut(Schema):
    # Lo que entra a la request
    #sent_by_id :
    timestamp: datetime
    content: str
    message_type: str
    #property_id
    status: str

class MessageIn(Schema):
    # Lo que entra a la request
    #received_by_id : 
    content: str
    message_type: str
    #property_id
    #status: str