from ninja import Router
from typing import List
from users.schemas import UserRegister
from users.models import User

router = Router()

@router.get("", response=UserRegister)
def get_users(request):
    return User.objects.all()
