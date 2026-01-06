from django.db import models
from  django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    time = models.DateTimeField(default=timezone.now)
    auther = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profiles_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

