from django.db import models
from django.contrib.postgres.fields import ArrayField
from users.models import User
from locations.models import Commune

status_length = 200

# Create your models here.
class Property(models.Model):
    coordinates = ArrayField(ArrayField(models.FloatField(), size=2))
    title = models.CharField(max_length=status_length)
    price = models.IntegerField(default=0)
    commune = models.ForeignKey(Commune, on_delete=models.DO_NOTHING, null=False)
    description = models.TextField()
    address = models.TextField()
    area = models.FloatField()
    contact = models.CharField(max_length=status_length)
    status = models.CharField(max_length=status_length)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    photos_urls = ArrayField(models.TextField())
    water = models.BooleanField(default=0) 
    electricity = models.BooleanField(default=0)
    sewer = models.BooleanField(default=0)