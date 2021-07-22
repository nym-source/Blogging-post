from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):
  User_Name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User_Name')
  Category = models.CharField(max_length=100,null=True,primary_key=False)
  Title   = models.CharField(max_length=200,null=True,primary_key=False)
  Summary = models.TextField(max_length=1000,null=True,primary_key=False)
  Content = RichTextField(null=True)
  Publised = models.BooleanField(default=False)
  Image  = models.FileField(blank=True, upload_to='images/')
  published_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.Title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_PIC  = models.FileField(blank=True, upload_to='user_images/')
    Category = models.CharField(max_length=200,null=True)
    Full_Address = models.TextField(max_length=500,null=True)
    city   = models.CharField(max_length=200,null=True)
    state   = models.CharField(max_length=200,null=True)
    pincode   = models.CharField(max_length=200,null=True)

    def __str__(self):
      return self.city 


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
