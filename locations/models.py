from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=1000)

class Commune(models.Model):
    name = models.CharField(max_length=1000)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=False)