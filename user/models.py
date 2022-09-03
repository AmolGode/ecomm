from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=200)

    class Meta:
        db_table = 'custom_user'