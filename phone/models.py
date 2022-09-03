from django.db import models
from user.models import CustomUser
import uuid

# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    brand_description = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'brand'

class Phone(models.Model):
    model_name = models.CharField(max_length=50)
    phone_name = models.CharField(max_length=50)
    camera_features = models.CharField(max_length=500)
    display_features = models.CharField(max_length=500)
    operating_system = models.CharField(max_length=50)
    charging = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE, related_name='brand')
    custom_user = models.ManyToManyField(CustomUser,through='UserPhoneOrder', related_name='user_phone_order') # Many user can order many phones
    user_phone_reviews = models.ManyToManyField(CustomUser,through='UserPhoneReviews', related_name='user_phone_reviews') # Many user can give many reviews to many phones

    class Meta:
        db_table = 'phone'

class UserPhoneOrder(models.Model): ##many to many table
    order_id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    order_date = models.DateTimeField(auto_now=True)
    order_status = models.CharField(max_length=20)
    custom_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone,on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_phone_order'



class UserPhoneReviews(models.Model):
    review_text = models.CharField(max_length=300)
    review_date_time = models.DateTimeField(auto_now=True)
    phone = models.ForeignKey(Phone,on_delete=models.CASCADE)
    custom_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_phone_reviews'

