from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    voted_by = models.ManyToManyField(to='Profile', related_name='votes', through='Vote')
    post_url = models.CharField(max_length=255)    
    description = models.TextField()
    slug = models.SlugField()

    class Meta:
        ordering = ["-date_posted"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)

    def set_slug(self):
        # If the slug is already set, stop here.
        if self.slug:
            return
        
        base_slug = slugify(self.title)
        slug = base_slug
        n = 0

        while Post.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)
        
        self.slug = slug

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.slug)])

    
class Comment(models.Model):
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(null=True)

class Profile(models.Model):   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    voted_for = models.ManyToManyField(to=Post, related_name='votes', through='Vote')

    def __str__(self):
        return self.user.username


class Vote(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    voted_at = models.DateTimeField(default = '2019-03-19 20:00')