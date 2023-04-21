from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Milestone(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/', default='media/default.jpg')
    owner = models.ForeignKey(
        User, related_name='milestones', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
