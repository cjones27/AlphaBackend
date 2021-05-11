from ninja import Router
from typing import List
from appointments.schemas import AppointmentRegister
from appointments.models import Appointment
from django.shortcuts import get_object_or_404

router = Router()

# GET Methods
@router.get("", response=List[AppointmentRegister]) #remember to add auth
def get_appointments(request):
    return Appointment.objects.all()

# POST Methods
@router.post("/create", response=AppointmentRegister)
def create_appointment(request, appointment:AppointmentRegister):
    new_appointment = Appointment.objects.create(**appointment.dict())
    new_appointment.save()
    return new_appointment