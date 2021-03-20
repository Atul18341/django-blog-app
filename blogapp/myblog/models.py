from django.db import models

# Create your models here.
class blog(models.Model):
   content=models.TextField()
   image=models.ImageField(upload_to='uploads')

   def __str__(self):
      return self.post
