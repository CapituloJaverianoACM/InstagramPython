from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.CharField(max_length=100, null = True)
    follow_table = models.ManyToManyField("self",through='Follow', symmetrical=False)
    estado = models.CharField(max_length=300, null = True)
    def __str__(self):
        return self.user.username

class Follow( models.Model ):
    from_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='%(class)s_from_id' )
    to_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='%(class)s_to_id' )

class Post(models.Model):
    photo = models.CharField(max_length=100, null = True)
    video = models.CharField(max_length=100, null = True)
    time = models.DateTimeField(default=datetime.now)
    description = models.CharField(max_length=100, null = True)
    owner_user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
