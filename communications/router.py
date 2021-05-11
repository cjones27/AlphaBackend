from ninja import Router
from typing import List
from communications.schemas import MessageOut, MessageIn
from communications.models import Message
from django.shortcuts import get_object_or_404

router = Router()

# GET Methods
@router.get("", response=List[MessageOut])
def get_messages(request):
    return Message.objects.all()

# POST Methods
@router.post("/message/create", response=MessageOut)
def create_message(request, message:MessageIn):
    new_message = Message.objects.create(**message.dict())
    new_message.save()
    return new_message