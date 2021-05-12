from django.db import models
import uuid
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

# constants
name_length = 200
password_length = 128

# Users model
class User(models.Model):
    first_name = models.CharField(max_length=name_length)
    last_name = models.CharField(max_length=name_length)
    user_type = models.IntegerField(default=0)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=254, unique=True)
    password = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    api_key = models.UUIDField(default=uuid.uuid4, db_index=True)
    last_session = models.DateTimeField(default=now)

# class PollManager(models.Manager):
#     def create_user(self, **kwargs):
#         return 

# class UserManager_(models.Manager):
#     pass


# class ThreadManager(models.Manager):

#     obj = ThreadModel.objects

#     @staticmethod
#     def create_new_thread(subject, board_id):
#         curr_board = BoardModel.objects.get(board_id = board_id)
#         thread = ThreadManager.obj.create(board= curr_board, thread_name=subject)
#         thread.save()
#         return thread

#     @staticmethod
#     def get_all_messages_in_thread(thread):
#         messages = MessageModel.objects.filter(thread = thread)
#         return messages

# @router.post("/register", response=UserOutPrivate, auth=None)
# def create_user(request, user: UserIn):
#     user_model = User(**user.dict())
#     user_model.set_password(user.password)
#     user_model.save()

#     # return value includes api_key
#     return user_model