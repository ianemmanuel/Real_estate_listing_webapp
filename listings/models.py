from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from demo_register import settings
from django.urls import reverse
from datetime import datetime, date
from multiupload.fields import MultiFileField
# from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cat_imgs/")
    description = models.TextField(blank=True, null=True)
    banner = models.ImageField(upload_to="banner_imgs/",blank=True, null=True)


    class Meta:
        verbose_name_plural='1. Categories'
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.image.url))

    def __str__(self):
        return self.title

        
class Listing(models.Model):

    PAYMENT_TYPE=[
    ('R','For Rent'),
    ('S','For Sale'),
    ('L', 'For Lease')
    ]

    title = models.CharField(max_length=200)
    number_of_bedrooms = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    address = models.CharField(max_length=200)
    area_sqft = models.DecimalField(max_digits=12, decimal_places= 2)
    detail= models.TextField(blank=True,null=True)
    thumbnail = models.ImageField(blank=True, null=True,upload_to='thumbnail_imgs/')
    image_1 = models.ImageField(blank=True, null=True,upload_to='image_imgs1/')
    image_2 = models.ImageField(blank=True, null=True,upload_to='image_imgs2/')
    image_3 = models.ImageField(blank=True, null=True,upload_to='image_imgs3/')
    image_4 = models.ImageField(blank=True, null=True,upload_to='image_imgs4/')
    slug  = models.CharField(max_length=400,default=title)
    video = models.FileField(upload_to="videos_uploaded/",null=True, blank=True)
    
    type = models.CharField(choices=PAYMENT_TYPE,max_length=1)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    open_house_date = models.DateTimeField(null=True, blank=True)
    is_featured=models.BooleanField(default=False)
    Agent=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural='2. Listings'
    
    def __str__(self):
        return self.title + " | " + str(self.Agent)



    def get_absolute_url(self):
        # return reverse('comic_detail', args=(str(self.id)))
        return reverse('index')
