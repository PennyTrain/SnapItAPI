from django.db import models
from django.contrib.auth.models import User
from snaps.models import Snap
"""
This code defines a Django model called SnapLike,
which represents a like given by a user to a snap.
Each SnapLike is linked to a user (owner) and a snap,
with a timestamp for when the like was created. The
model ensures uniqueness for each combination of user
and snap, orders the likes by creation date in descending
order, and provides a string representation combining
the owner's username and the snap.
"""


class SnapLike(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    snap = models.ForeignKey(Snap,
                             related_name="snaplikes",
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        unique_together = ('owner', 'snap')

    def __str__(self):
        return str(self.owner) + ' | ' + str(self.snap)
