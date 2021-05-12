from django.db import models

# Create your models here.
class Message(models.Model):
    #sent_by_id = 
    #received_by_id = 
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    message_type = models.CharField(max_length=200)
    #property_id
    status = models.CharField(max_length=200, default="OK")

class Notification(models.Model):
    notification_type = models.CharField(max_length=200)
    content = models.TextField()
    # user_id = models.ForeignKey
    timestamp = models.DateTimeField(auto_now_add=True)
    # property_id = models.ForeignKey