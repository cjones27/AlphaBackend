from properties.models import Property
from alphabackend.security import AdminAuth
from ninja import Router
from typing import List
from appointments.schemas import AppointmentIn, AppointmentOut, AppointmentOutPublic
from appointments.models import Appointment
from django.shortcuts import get_object_or_404
from users.schemas import Message
from users.models import User

router = Router()

# GET Methods
@router.get("", response=List[AppointmentOut])#, auth=AdminAuth())
def get_appointments(request):
    return Appointment.objects.all()

@router.get("/{appointment_id}", response={200:AppointmentOutPublic, 401:Message})
def get_appointment(request, appointment_id:int):
    # user = request.auth
    appointment = get_object_or_404(Appointment, id=appointment_id)
    # property = get_object_or_404(Property, id=appointment.property_id)
    # owner = get_object_or_404(User, id=property.user_id)
    # if user.id == appointment.user_id or user.is_admin or user.id == owner.id:
    return 200, appointment

    # return 401, {"message": "Not allowed"}

@router.get("/property/{property_id}", response={200:List[AppointmentOutPublic], 401:Message})
def get_property_appointments(request, property_id:int):
    property = get_object_or_404(Property, id=property_id)
    appointments = Appointment.objects.filter(property_id=property.id)
    return 200, appointments

@router.get("/property/owner/{property_id}", response={200:List[AppointmentOut], 401:Message})
def get_property_appointments_by_owner(request, property_id:int):
    user = request.auth
    property = get_object_or_404(Property, id=property_id)
    appointments = Appointment.objects.filter(property_id=property.id)
    owner = get_object_or_404(User, id=property.user_id)
    if user.is_admin or user.id == owner.id:
        return 200, appointments
    return 401, {"message": "Not allowed"}

@router.get("/user/{user_id}", response={200:List[AppointmentOut], 401:Message})
def get_user_appointments(request, user_id:int):
    user = request.auth
    appointments = Appointment.objects.filter(user_id=user.id)
    if user.id == user_id or user.is_admin:
        return 200, appointments
    return 401, {"message": "Not allowed"}

# POST Methods
@router.post("/future/create", response={200:AppointmentOut, 401:Message})
def create_appointment(request, appointment:AppointmentIn):
    user = request.auth
    property = get_object_or_404(Property, id=appointment.property_id)
    if user.id == appointment.user_id or user.is_admin:
        new_appointment = Appointment.objects.create(**appointment.dict())
        new_appointment.save()
        return 200, new_appointment
    return 401, {"message": "Not allowed"}

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