from django.db import models
from  django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify 

from django.db.models.signals import post_save
from django.dispatch import receiver

#  from image size optimizing 
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    slug = models.SlugField(max_length =100,blank=True,null=True)
    image = models.ImageField(upload_to='post_images', default='default.jpg')
    time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    # to generate slug form title wihout duplicating 
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug =slugify(self.title)
            slug = base_slug
            count=1

            while Post.objects.filter(slug=slug).exclude(id = self.id).exists():
                slug =f'{base_slug}-{count}'
                count +=1

            self.slug =slug
        super().save(*args, **kwargs)
        # Resize image
        if self.image and self.image.name != 'default.jpg':
            img = Image.open(self.image.path)
            max_width, max_height = 800, 600
            ratio = min(max_width / img.width, max_height / img.height)
            if ratio < 1:
               new_width = int(img.width * ratio)
               new_height = int(img.height * ratio)
               img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
               img.save(self.image.path, optimize=True, quality=70)


    # to resize image in post if the image is too large 
        
    

    def __str__(self):
        return self.title



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profiles_pics')
    bio =  models.TextField(blank=True)

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


    


        
    


    



