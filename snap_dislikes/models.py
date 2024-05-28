from django.db import models
from django.contrib.auth.models import User
from snaps.models import Snap
"""
This code defines a Django model called SnapDislike,
representing instances where a user dislikes a snap.
Each SnapDislike instance is associated with a user
(owner) and a snap. The model includes a timestamp for
when the dislike was created and ensures that each
combination of user and snap is unique, ordering them
by creation date in descending order.
"""


class SnapDislike(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    snap = models.ForeignKey(Snap,
                             related_name="snapdislikes",
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        unique_together = ('owner', 'snap')

    def __str__(self):
        return str(self.owner) + ' | ' + str(self.snap)
