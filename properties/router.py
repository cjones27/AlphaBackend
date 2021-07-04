from locations.models import Commune
from users.schemas import Message
from ninja import Router
from typing import List
from properties.schemas import PropertyOut, PropertyRegister
from properties.models import Property
from django.shortcuts import get_object_or_404
from users.models import User
from alphabackend.security import AdminAuth

router = Router()

# GET Methods
@router.get("", response=List[PropertyOut])
def get_properties(request):
    return Property.objects.all()

@router.get("/{property_id}", response=PropertyOut)
def get_property(request, property_id:int):
    return get_object_or_404(Property, id=property_id)

@router.get("/commune/{commune_id}", response=List[PropertyOut])
def get_property_by_commune_id(request, commune_id:int):
    return Property.objects.all().filter(commune_id=commune_id)


# POST Methods
@router.post("/create/{user_id}", response={200:PropertyOut, 401:Message})
def create_property(request, property:PropertyRegister, user_id:int):
    user = request.auth
    if ((user.id == user_id) or user.is_admin):
        commune = get_object_or_404(Commune, id=property.dict()["commune"])
        owner = get_object_or_404(User, id=user_id)
        new_property_dict = property.dict().copy()
        new_property_dict["commune"] = commune
        new_property = Property.objects.create(**new_property_dict, user=owner)
        new_property.save()
        return 200, new_property

    return 401, {"message": "Unauthorized"}

# DELETE Method
@router.delete("/delete/{property_id}", response={200:Message, 401:Message})
def delete_property(request, property_id:int):
    user = request.auth
    property = get_object_or_404(Property, id=property_id)
    if ((user.id == property.user_id) or user.is_admin):
        property.delete()
        return 200, {"message":"Succesfully deleted"}

    return 401, {"message": "Unauthorized"}

# UPDATE Method
@router.put("/update/{property_id}", response={200:PropertyOut, 401:Message})
def update_property(request, property_id:int, property:PropertyRegister):
    user = request.auth
    edited_property = get_object_or_404(Property, id=property_id)
    if ((user.id == edited_property.user_id) or user.is_admin):
        for att , value in property.dict().items():
            setattr(edited_property, att, value)
        edited_property.save()
        return 200, edited_property

    return 401, {"message": "Unauthorized"}