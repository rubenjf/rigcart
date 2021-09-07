from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField  

RIG_CHOICES= [
    ('Active', 'Active'),
    ('Archieve', 'Archieve'),
    ]

class Event(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    description = models.TextField()
    rig_date = models.DateTimeField(default=timezone.now)
    rig_choices = models.CharField("rig Type",max_length=20,choices=RIG_CHOICES, default='Active') 
    rig_image = models.ImageField(upload_to='images', default='images/anc-logo.png')
    document = models.FileField(upload_to ='documents')  # file will be saved to MEDIA_ROOT / rigs / 2015 / 01 / 30 
    current_url = models.CharField(max_length = 250, null = True, blank = True) 
   
    def __str__(self):
        return f'{self.name +",  "+ self.location}'
    class Meta:
        ordering = ['-rig_date'] 
        

class Categories(models.Model):
    name = models.CharField(max_length=250)
   
    def __str__(self):
        return f'{self.name}'
    class Meta:
        ordering = ['name'] 

# class Product(models.Model):

#     def __str__(self):
#         return f'{self.name}'
#     class Meta:
         

