from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
"""
This code defines a Profile model
associated with the Django User model
via a one-to-one relationship,
containing fields such as name, content,
image, and pet-related information.
The model automatically records timestamps
for creation and updates, and orders profiles
by the creation date in descending order. A
friendship_count property is defined to count the
number of friendships for the profile's owner. Additionally,
a signal handler create_profile ensures a profile is created for
each new user, connecting to the post_save signal of the User model.
"""


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='images/Screenshot_2024-05-29_212019_h2nbja.png'
    )
    pet_name = models.CharField(max_length=100, blank=True)
    pet_age = models.IntegerField(blank=True, null=True)
    pet_breed = models.CharField(max_length=100, blank=True)
    pet_type = models.CharField(max_length=100, default="Other")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


@property
def friendship_count(self):
    return self.owner__friended__friended.count()


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
