from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse

# User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #post_score = models.
    post_url = models.CharField(max_legnth=255)    
    description = models.TextField()
    slug = models.SlugField()

    class Meta:
        ordering = ["-date_posted"]

    
    
class Comment(models.Model):
    date_posted = models.DateTimeField(auto_now_add=True)
    









class User(models.Model):
    username = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)







class Vote(models.Model):
    user_vote