from django.db import models
from  django.contrib.auth.models import User
from django.utils import timezone

from django.db.models.signals import post_save
from django.dispatch import receiver

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

# to automatically create profile when user is created 

@receiver(post_save, sender=User)
def create_user_profile(sender, instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


    


        
    


    



