from django.db import models


class Services(models.Model):
    service_icon=models.CharField(max_length=50)
    service_tittle=models.CharField(max_length=50)
    service_des=models.FloatField()
 