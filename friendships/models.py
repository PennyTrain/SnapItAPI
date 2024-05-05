from django.db import models
from django.contrib.auth.models import User

class SnapFriendship(models.Model):
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    friended = models.ForeignKey(User, related_name='friended', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'friended']

    def __str__(self):
        return str(self.owner) + ' | ' + str(self.friended)
