from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #name = models.CharField(max_length=100)
    #nickname = models.CharField(max_length=20,unique = True)
    #password = models.CharField(max_length=50)
    #email = models.CharField(max_length=50, unique = True)
    photo = models.CharField(max_length=100, null = True)
    follow = models.ManyToManyField("self")
    def __str__(self):
        return self.name

class Post(models.Model):
    photo = models.CharField(max_length=100, null = True)
    video = models.CharField(max_length=100, null = True)
    time = models.DateTimeField(default=datetime.now)
    description = models.CharField(max_length=100, null = True)
    longitude = models.DecimalField(max_digits=9,decimal_places=6, null = True)
    latitude = models.DecimalField(max_digits=9,decimal_places=6, null = True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
