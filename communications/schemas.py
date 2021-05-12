from ninja import Schema
from datetime import datetime

class MessageOut(Schema):
    #sent_by_id :
    timestamp: datetime
    content: str
    message_type: str
    #property_id
    status: str

class MessageIn(Schema):
    #received_by_id : 
    content: str
    message_type: str
    #property_id
    #status: str

class NotificationIn(Schema):
    #sent_by_id :
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