from properties.models import Property
from alphabackend.security import AdminAuth
from ninja import Router
from typing import List
from appointments.schemas import AppointmentIn, AppointmentOut
from appointments.models import Appointment
from django.shortcuts import get_object_or_404
from users.schemas import Message
from users.models import User

router = Router()

# GET Methods
@router.get("", response=List[AppointmentOut], auth=AdminAuth()) #remember to add auth
def get_appointments(request):
    return Appointment.objects.all()

@router.get("/{appointment_id}", response={200:AppointmentOut, 401:Message})
def get_appointment(request, appointment_id:int):
    user = request.auth
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if user.id == appointment.user_id or user.is_admin:
        return 200, appointment

    return 401, {"message": "Not allowed"}

# POST Methods
@router.post("/future/create", response=AppointmentOut)
def create_appointment(request, appointment:AppointmentIn):
    user = get_object_or_404(User, id=appointment.user_id)
    property = get_object_or_404(Property, id=appointment.property_id)
    new_appointment = Appointment.objects.create(**appointment.dict())
    new_appointment.save()
    return new_appointment

# DELETE Method
@router.delete("/delete/{appointment_id}", response={200:Message, 401:Message})
def delete_appointment(request, appointment_id:int):
    user = request.auth
    appointment = get_object_or_404(Appointment, id=appointment_id)
    property = get_object_or_404(Property, id=appointment.property_id)
    owner = get_object_or_404(User, id=property.user_id)
    if user.id == appointment.user_id or user.id == owner.id or user.is_admin:
        appointment.delete()
        return 200, {"message":"Appoinment succesfully deleted"}

    return 401, {"message": "Not allowed"}