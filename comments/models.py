from django.db import models
from django.contrib.auth.models import User
from shoutouts.models import Milestone


class Comments(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.content
