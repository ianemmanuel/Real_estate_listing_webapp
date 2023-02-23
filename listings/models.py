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
    description = models.TextField(blank=True, null=True)


    class Meta:
        verbose_name_plural='1. Categories'
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.image.url))

    def __str__(self):
        return self.title




class Listing(models.Model):

    PAYMENT_TYPE=[
    ('R','Rent'),
    ('S','For Sale'),
    ]

    title = models.CharField(max_length=200)
    number_of_bedrooms = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    address = models.CharField(max_length=200)
    area_sqft = models.DecimalField(max_digits=12, decimal_places= 2)
    detail= models.TextField()
    #image
    slug  = models.CharField(max_length=400,default=title)
    video = models.FileField(upload_to="videos_uploaded/",null=True, blank=True)
    detail=RichTextField(blank=True, null=True)
    type = models.CharField(choices=PAYMENT_TYPE,max_length=1)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
     
    # status = models.BooleanField(default=True)
    is_featured=models.BooleanField(default=False)
    Agent=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title + "|" + self.Agent.name 



    def get_absolute_url(self):
        # return reverse('comic_detail', args=(str(self.id)))
        return reverse('index')


