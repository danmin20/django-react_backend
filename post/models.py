from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=200)
    owner = models.ForeignKey(
        User, related_name="posts", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.text