from ninja import Router
from typing import List
from users.schemas import UserRegister, UserOut
from users.models import User
from django.shortcuts import get_object_or_404
from alphabackend.security import AnyUserApiKey

login_required = AnyUserApiKey()

router = Router()

# GET Methods
@router.get("", response=List[UserRegister], auth=login_required)
def get_users(request):
    return User.objects.all()

@router.get("/{user_id}", response=UserRegister)
def get_user(request, user_id:int):
    return get_object_or_404(User, id=user_id)

# POST Methods
@router.post("/register", response=UserOut)
def create_user(request, user:UserRegister):
    new_user = User.objects.create(**user.dict())
    new_user.save()
    return new_user

# DELETE Method
@router.delete("/{user_id}")
def delete_user(request, user_id:int):
    deleted_user = get_object_or_404(User, id=user_id)
    deleted_user.delete()
    return {"success":True}

# PUT Method
@router.put("/{user_id}", response=UserRegister)
def put_user(request, user_id:int, user:UserRegister):
    edited_user = get_object_or_404(User, id=user_id)
    for att , value in user.dict().items():
        setattr(edited_user, att, value)
    edited_user.save()
    return edited_user