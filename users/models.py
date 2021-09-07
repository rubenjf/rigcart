from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage as storage
import os
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this
from PIL import Image

#ref: https://www.devhandbook.com/django/user-profile/



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/')
    phone = models.CharField(max_length=20, blank=True, default='')

    def __str__(self):
        return f'{self.user.username} Profile'


    @receiver(post_save, sender=User) #add this
    def create_user_profile(sender, instance, created, **kwargs):
       if created:
          Profile.objects.create(user=instance)

    @receiver(post_save, sender=User) #add this
    def save_user_profile(sender, instance, **kwargs):
       instance.profile.save()
    #    img = Image.open(self.image.path) # Open image
    #    # resize image  
    #    if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size) # Resize image
    #         img.save(self.image.path) # Save it again and override the larger image
        
        


