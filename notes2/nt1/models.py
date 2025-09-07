from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class note(models.Model):
    title = models.TextField()
    text = models.CharField(max_length=64)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_notes')

  