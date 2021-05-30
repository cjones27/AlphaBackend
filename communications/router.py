from ninja import Router
from typing import List
from communications.schemas import MessageIn, MessageOut, NotificationIn, NotificationOut
from communications.models import Message, Notification
from django.shortcuts import get_object_or_404
from communications.schemas import MessageOut, MessageIn
from alphabackend.security import AdminAuth
from properties.models import Property
from users.models import User

router = Router()

# GET Methods
@router.get("/messages", response=List[MessageOut], auth=AdminAuth)
def get_messages(request):
    return Message.objects.all()

@router.get("/user/messages", response=List[MessageOut])
def get_user_messages(request):
    user = request.auth
    messages = Message.objects.filter(sent_by_id=user.id) | Message.objects.filter(received_by_id=user.id)
    return messages

# POST Methods
@router.post("/messages/create", response=MessageOut)
def create_message(request, message:MessageIn):
    user = request.auth
    print("##########################")
    print(message.dict())
    property = get_object_or_404(Property, id=message.property_id)
    new_message = Message.objects.create(**message.dict())
    new_message.save()
    return new_message

@router.get("/notifications", response=List[NotificationOut])
def get_notifications(request):
    return Notification.objects.all()

# POST Methods
@router.post("/notifications/create", response=NotificationOut)
def create_notification(request, notification:NotificationIn):
    new_notification = Notification.objects.create(**notification.dict())
    new_notification.save()
    return new_notification