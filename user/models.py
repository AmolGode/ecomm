from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=10,blank=False,null=False)
    address = models.CharField(max_length=200)
    mobile_number_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'custom_user'