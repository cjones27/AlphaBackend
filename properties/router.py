from ninja import Router
from typing import List
from properties.schemas import PropertyOut, PropertyRegister
from properties.models import Property
from django.shortcuts import get_object_or_404

router = Router()

# GET Methods
@router.get("", response=List[PropertyOut])
def get_properties(request):
    return Property.objects.all()


# POST Methods
@router.post("/create", response=PropertyOut)
def create_property(request, property:PropertyRegister):
    new_property = Property.objects.create(**property.dict())
    new_property.save()
    return new_property