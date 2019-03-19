from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    #post_score = models.
    post_url = models.CharField(max_length=255)    
    description = models.TextField()
    slug = models.SlugField()

    class Meta:
        ordering = ["-date_posted"]

    def __str__(self):
        return self.title

    
class Comment(models.Model):
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(null=True)

class User(models.Model):   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)



    def __str__(self):
        return self.user.name



class Vote(models.Model):
    pass