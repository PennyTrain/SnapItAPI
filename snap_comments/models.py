from django.db import models
from django.contrib.auth.models import User
from snaps.models import Snap
from profiles.models import Profile

# Create your models here.

class SnapComment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    snap = models.ForeignKey(Snap, 
                             related_name="snapcomments", 
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=150, blank=True)
    body = models.TextField(blank=True)

    def __str__(self):
        return str(self.id) + ' | ' + str(self.title)
    
    class Meta: 
        ordering=["-created"]

