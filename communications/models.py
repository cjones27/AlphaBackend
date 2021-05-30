from django.db import models
from users.models import User
from properties.models import Property

# Create your models here.
class Message(models.Model):
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="sent_by")
    sent_to = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="sent_to")
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    message_type = models.CharField(max_length=200)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=False)
    status = models.CharField(max_length=200, default="OK")

class Notification(models.Model):
    notification_type = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=False)