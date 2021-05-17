from django.db import models
from users.models import User
from properties.models import Property

# Create your models here.
class Appointment(models.Model):
    datetime = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=False)
    status = models.CharField(max_length=200)