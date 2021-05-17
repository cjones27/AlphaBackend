from django.db import models
# from django.contrib.gis.db import models as geomodels
from users.models import User

status_length = 200

# Create your models here.
class Property(models.Model):
    # coordinates = geomodels.PointField()
    price = models.IntegerField(default=0)
    # commune_id = models.ForeignKey(
    #     communes, on_delete=models.DO_NOTHING, null=True
    # )
    description = models.TextField()
    status = models.CharField(max_length=status_length)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    # points = geomodels.MultiPointField()
    # photos_id = 
    water = models.BooleanField(default=0) 
    electricity = models.BooleanField(default=0)
    sewer = models.BooleanField(default=0)