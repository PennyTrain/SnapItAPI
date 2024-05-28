from django.db import models
from django.contrib.auth.models import User


class SnapFriendship(models.Model):
    """
This Django model, SnapFriendship,
represents a friendship relationship between
two users. It has foreign key references to
the User model for both the owner and the friended user,
ensuring that each friendship is unique through the
unique_together constraint on these fields. The model
also includes a timestamp for when the friendship was
created and a string representation method that returns
the usernames of the owner and friended users.
"""
    owner = models.ForeignKey(User,
                              related_name='owner',
                              on_delete=models.CASCADE)
    friended = models.ForeignKey(User,
                                 related_name='friended',
                                 on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'friended']

    def __str__(self):
        return f'{self.owner.username} - {self.friended.username}'
