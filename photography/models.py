from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User 

# Create your models here.

class Post(models.Model):
    location = models.TextField(max_length=100, default=False)
    description = models.TextField(blank = True, default=False)
    # zipcode = models.IntegerField(blank=False, null=True)
    zipcode = models.TextField(max_length=5, default=False)
    # date_posted = models.DateTimeField(default=timezone.now) 
    date_posted = models.TextField(max_length=15, default=False)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.TextField(max_length=100, default=False)

class Picture(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=400)
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=400)

