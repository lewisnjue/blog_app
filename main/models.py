from django.db import models
import time
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    profile_picture = models.ImageField(default='default.png', upload_to='profiles/%Y/%m/%d/')

    def __str__(self):
        return self.username

class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    dateposted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
