from ninja import Schema
from datetime import datetime
from properties.schemas import PropertyOut
from users.schemas import UserOutPublic

class MessageOut(Schema):
    id: int
    sent_by: UserOutPublic
    sent_to: UserOutPublic
    timestamp: datetime
    content: str
    property: PropertyOut
    message_type: str
    status: str

class MessageIn(Schema):
    sent_by_id: int
    sent_to_id: int
    content: str
    message_type: str
    property_id: int
    status: str

class NotificationIn(Schema):
    timestamp: datetime
    content: str
    notification_type: str
    #property_id

class NotificationOut(Schema):
    #received_by_id : 
    content: str
    notification_type: str
    #property_id
    #status: str