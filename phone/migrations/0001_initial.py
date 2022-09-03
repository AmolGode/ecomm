# Generated by Django 4.1 on 2022-09-03 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_customuser_mobile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50)),
                ('brand_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('phone_name', models.CharField(max_length=50)),
                ('camera_features', models.CharField(max_length=500)),
                ('display_features', models.CharField(max_length=500)),
                ('operating_system', models.CharField(max_length=50)),
                ('charging', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='phone.brand')),
            ],
        ),
        migrations.CreateModel(
            name='UserPhoneReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.CharField(max_length=300)),
                ('review_date_time', models.DateTimeField(auto_now=True)),
                ('custom_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phone.phone')),
            ],
        ),
        migrations.CreateModel(
            name='UserPhoneOrder',
            fields=[
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('order_status', models.CharField(max_length=20)),
                ('custom_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phone.phone')),
            ],
        ),
        migrations.AddField(
            model_name='phone',
            name='custom_user',
            field=models.ManyToManyField(related_name='user_phone_order', through='phone.UserPhoneOrder', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='phone',
            name='user_phone_reviews',
            field=models.ManyToManyField(related_name='user_phone_reviews', through='phone.UserPhoneReviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
