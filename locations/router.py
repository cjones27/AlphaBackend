from locations.models import Commune
from locations.schemas import CommuneOut
from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404

router = Router()

# GET Methods
@router.get("", response=List[CommuneOut])
def get_communes(request):
    return Commune.objects.all()

@router.get("/region/{region_id}", response=List[CommuneOut])
def get_communes_by_region(request, region_id:int):
    return Commune.objects.all().filter(region_id=region_id)