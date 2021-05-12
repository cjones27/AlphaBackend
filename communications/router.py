from ninja import Router
from typing import List
from communications.schemas import MessageIn, MessageOut, NotificationIn, NotificationOut
from communications.models import Message, Notification
from django.shortcuts import get_object_or_404
from communications.schemas import MessageOut, MessageIn

router = Router()

# GET Methods
@router.get("/messages", response=List[MessageOut])
def get_messages(request):
    return Message.objects.all()

# POST Methods
@router.post("/messages/create", response=MessageOut)
def create_message(request, message:MessageIn):
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