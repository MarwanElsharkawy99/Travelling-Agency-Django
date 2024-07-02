from django.db import models
from django.contrib.auth.models import AbstractUser




class customUser(AbstractUser):
    first_name=models.CharField(max_length=256)
    last_name=models.CharField(max_length=256)
    date_birth=models.DateField(null=True)
    nationality=models.CharField(max_length=256)
    Address1=models.CharField(max_length=256)
    Address2=models.CharField(max_length=256)
    city=models.CharField(max_length=256)
    region=models.CharField(max_length=256)
    zipcode=models.CharField(max_length=256)
    country=models.CharField(max_length=256)
    mobile=models.IntegerField(null=True)

    def __str__(self):
        return self.first_name



