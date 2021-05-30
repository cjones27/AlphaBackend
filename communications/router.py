from ninja import Router
from typing import List
from communications.schemas import MessageIn, MessageOut, NotificationIn, NotificationOut
from communications.models import Message, Notification
from django.shortcuts import get_object_or_404
from communications.schemas import MessageOut, MessageIn
from alphabackend.security import AdminAuth
from properties.models import Property
from users.models import User
from users.schemas import Message as Msg

router = Router()

# GET Methods
@router.get("/messages", response=List[MessageOut], auth=AdminAuth())
def get_messages(request):
    return Message.objects.all()

@router.get("/user/messages", response=List[MessageOut])
def get_user_messages(request):
    user = request.auth
    messages = (Message.objects.filter(sent_by_id=user.id) | Message.objects.filter(sent_to_id=user.id)).distinct("property_id")
    return messages

@router.get("/user/messages/{property_id}", response={200:List[MessageOut], 401:Msg})
def get_user_messages_by_property(request, property_id:int):
    user = request.auth
    property = get_object_or_404(Property, id=property_id)
    if user.id == property.user_id:
        messages = Message.objects.filter(property_id=property_id)
        return 200, messages
    return 401, {"message": "Not allowed"}

# POST Methods
@router.post("/messages/create", response={200:MessageOut, 401:Msg})
def create_message(request, message:MessageIn):
    user = request.auth
    property = get_object_or_404(Property, id=message.property_id)
    if user.id == message.sent_by_id:
        new_message = Message.objects.create(**message.dict())
        new_message.save()
        return 200, new_message
    return 401, {"message": "Not allowed"}

# DELETE Methods
@router.delete("/user/messages/delete/{message_id}", response={200:Msg, 401:Msg})
def delete_user_messages(request, message_id:int):
    user = request.auth
    message = get_object_or_404(Message, id=message_id)
    if message.sent_by_id == user.id:
        message.delete()
        return 200, {"message": "Succesfully deleted"}
    return 401, {"message": "Not allowed"}

@router.get("/notifications", response=List[NotificationOut])
def get_notifications(request):
    return Notification.objects.all()

# POST Methods
@router.post("/notifications/create", response=NotificationOut)
def create_notification(request, notification:NotificationIn):
    new_notification = Notification.objects.create(**notification.dict())
    new_notification.save()
    return new_notification

