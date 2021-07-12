from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.



class Profile(models.Model):
    image= models.TextField()
    bio = models.TextField()
    location = models.CharField(max_length=255)
    user = models.OneToOneField(User , related_name="profile" , on_delete=models.CASCADE)
    # products = models.ManyToManyField(Product)
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance , id =instance.id )
        

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()        







# class User(models.Model):
#     username = models.CharField(max_length=150, blank=True ,
#     verbose_name="name of the book",
#     help_text="add your book plz"
#      )
#     first_name = models.CharField(max_length=150,blank=True)
#     last_name = models.CharField(max_length=150,blank=True)
#     email = models.CharField(max_length=150,blank=True)
#     password = models.CharField(max_length=150)
#     image = models.TextField(max_length=150,blank=True)
   
    

#     def __str__(self):
#         return self.name