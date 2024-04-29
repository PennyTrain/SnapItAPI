from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Snap(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=150, blank=True)
    body = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_qdjgyp'
    )
    
