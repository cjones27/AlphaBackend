from locations.schemas import CommuneOut
from ninja import Router
from typing import List
from users.schemas import UserOutPublic, UserRegister, UserOut, LogIn, Message
from users.models import User
from django.shortcuts import get_object_or_404
from alphabackend.security import AdminAuth
from locations.models import Commune

router = Router()

# GET Methods
@router.get("", response={200: List[UserOutPublic], 404: Message})
def get_users(request):
    user = request.auth
    if user.is_admin:
        return 200, User.objects.all()
    else:
        return 404 , {"message":"Unauthorized"}

@router.get("/{user_id}", response=UserOutPublic)
def get_user(request, user_id:int):
    return get_object_or_404(User, id=user_id)

# POST Methods
@router.post("/future/signup", response=UserOut, auth=None)
def create_user(request, user:UserRegister):
    new_user = User.objects.create(**user.dict())
    new_user.save()
    return new_user

# Admin
@router.post("/future/signup_admin", response={200: UserOut, 404: Message})
def create_admin(request, user:UserRegister):
    user_current = request.auth
    if user_current.is_admin:
        new_admin = User.objects.create(**user.dict(), is_admin = 1)
        new_admin.save()
        return 200, new_admin
    else:
        return 404, {"message":"Unauthorized"}

# DELETE Method
@router.delete("/delete/{user_id}")
def delete_user(request, user_id:int):
    user = request.auth
    deleted_user = get_object_or_404(User, id=user_id)
    if ((user_id == user.id) or user.is_admin):
        deleted_user.delete()
        return {"success":True}
    else:
        return {"detail":"Unauthorized"}

# PUT Method
@router.put("/update/{user_id}", response={200: UserRegister, 404: Message})
def put_user(request, user_id:int, user:UserRegister):
    user_current = request.auth
    edited_user = get_object_or_404(User, id=user_id)
    if ((user_current.id == user_id) or user_current.is_admin):
        for att , value in user.dict().items():
            setattr(edited_user, att, value)
        edited_user.save()
        return 200, edited_user
    else:
        return 404, {"message":"Unauthorized"}

@router.post("/future/login", response={200: UserOut, 404: Message}, auth=None)
def login_user(request, payload: LogIn):
    user = get_object_or_404(User, email=payload.email)
    if payload.password == user.password:
        return 200, user

    return 404, {"message": "Incorrect credentials"}

@router.get("/communes/all", response=List[CommuneOut], auth=None)
def get_communes(request):
    return Commune.objects.all()