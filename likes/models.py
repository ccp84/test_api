from django.db import models
from django.contrib.auth.models import User
from shoutouts.models import Milestone


class Likes(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    milestone = models.ForeignKey(
        Milestone,
        on_delete=models.CASCADE,
        related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["owner", "milestone"]

    def __str__(self):
        return f'{self.owner} {self.milestone}'
