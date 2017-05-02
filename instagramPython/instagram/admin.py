from django.contrib import admin
from django.contrib.auth.models import User
from .models import Post,Comment,Like,MyUser
# Register your models here.
admin.site.register(MyUser)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
