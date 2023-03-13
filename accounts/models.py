from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='1. Users'

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    

    class Meta:
        verbose_name_plural='2. Customers'

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)


    class Meta:
        verbose_name_plural='3. Employees'


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic = models.ImageField(upload_to="profile_imgs/",null=True, blank=True)
    facebook_url=models.CharField(max_length=200, blank=True, null=True)
    instagram_url=models.CharField(max_length=200, blank=True, null=True)
    twitter_url=models.CharField(max_length=200, blank=True, null=True)
    website_url=models.CharField(max_length=200, blank=True, null=True)
    pinterest_url=models.CharField(max_length=200, blank=True, null=True)
    tiktok_url=models.CharField(max_length=200, blank=True, null=True)
    youtube_url=models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural='4. Profile'

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')



