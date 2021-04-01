from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class blog(models.Model):
   content=models.TextField()
   image=models.ImageField(upload_to='uploads')

   def __str__(self):
      return self.content

class Profile(models.Model):
   user=models.OneToOneField(User, on_delete=models.CASCADE)
   name=models.CharField(max_length=100)
   age=models.IntegerField()
   gender=models.CharField(max_length=100)


