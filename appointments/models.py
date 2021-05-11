from django.db import models

# Create your models here.
class Appointment(models.Model):
    datetime = models.DateTimeField()
    # user_id = 
    # property_id =
    status = models.CharField(max_length=200)