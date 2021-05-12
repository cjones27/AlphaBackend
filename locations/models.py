from django.db import models

# Create your models here.
class Commune(models.Model):
    name = models.CharField(max_length=1000)
    # region_id = models.ForeignKey(
    #     owner, on_delete=models.DO_NOTHING, null=True
    # )

class Region(models.Model):
    name = models.CharField(max_length=1000)