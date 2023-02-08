from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from demo_register import settings
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cat_imgs/")


    class Meta:
        verbose_name_plural='2. Categories'
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.image.url))

    def __str__(self):
        return self.title



class Location(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="pub_imgs/")


    class Meta:
        verbose_name_plural='3.Publishers'

    def __str__(self):
        return self.title


class Listing(models.Model):
    title = models.CharField(max_length=200)
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    address = models.CharField(max_length=200)
    square_footage = models.DecimalField(max_digits=4, decimal_places= 2)
    detail= models.TextField()
    #image
    slug  = models.CharField(max_length=400,default=title)
   
    detail=RichTextField(blank=True, null=True)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE) 
    status = models.BooleanField(default=True)
    is_featured=models.BooleanField(default=False)
    vendor=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)


