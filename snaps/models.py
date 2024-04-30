from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Posted"))

class Snap(models.Model):
    """
    The Snap model contains fields such as owner, created, 
    updated, title, body, featured_image, and status, 
    with appropriate data types and constraints. The Meta 
    inner class specifies the default ordering of instances 
    based on the date they were made.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=150, blank=True)
    body = models.TextField(blank=True)
    featured_image = models.ImageField(upload_to='images/', default='#')
    status = models.IntegerField(choices=STATUS, default=1)

    def __str__(self):
        return str(self.id) + ' | ' + str(self.title)
    
    class Meta:
        ordering=["-created"]