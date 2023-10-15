from django.db import models


# Create your models here.
class ModelFirst(models.Model):
    name = models.CharField(max_length=30, null=False)
    number = models.IntegerField(null=False)
