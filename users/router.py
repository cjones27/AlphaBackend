from ninja import Router
from typing import List
from users.schemas import UserRegister, UserOut, LogIn, Message
from users.models import User
from django.shortcuts import get_object_or_404
from alphabackend.security import AdminAuth

router = Router()

# GET Methods
@router.get("", response=List[UserRegister], auth=AdminAuth())
def get_users(request):
    return User.objects.all()

@router.get("/{user_id}", response=UserRegister)
def get_user(request, user_id:int):
    return get_object_or_404(User, id=user_id)

# POST Methods
@router.post("/future/signup", response=UserOut, auth=None)
def create_user(request, user:UserRegister):
    new_user = User.objects.create(**user.dict())
    new_user.save()
    return new_user

# Admin
@router.post("/future/signup_admin", response=UserOut, auth=AdminAuth())
def create_admin(request, user:UserRegister):
    new_admin = User.objects.create(**user.dict(), is_admin = 1)
    new_admin.save()
    return new_admin

# DELETE Method
@router.delete("/delete/{user_id}")
def delete_user(request, user_id:int):
    deleted_user = get_object_or_404(User, id=user_id)
    deleted_user.delete()
    return {"success":True}

# PUT Method
@router.put("/update/{user_id}", response=UserRegister)
def put_user(request, user_id:int, user:UserRegister):
    edited_user = get_object_or_404(User, id=user_id)
    for att , value in user.dict().items():
        setattr(edited_user, att, value)
    edited_user.save()
    return edited_user

@router.post("/future/login", response={200: UserOut, 404: Message}, auth=None)
def login_user(request, payload: LogIn):
    user = get_object_or_404(User, email=payload.email)
    if payload.password == user.password: #recordar check_password de encriptación
        return 200, user

    return 404, {"message": "Incorrect credentials"}