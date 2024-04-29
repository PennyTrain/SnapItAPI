from django.db import models
from django.contrib.auth.models import User
from snaps.models import Snap

# Create your models here.
class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    snap = models.ForeignKey(Snap, related_name="snaplikes", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        unique_together = ('owner', 'snap')

    def __str__(self):
        return str(self.owner) + ' | ' + str(self.snap)