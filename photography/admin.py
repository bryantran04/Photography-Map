from django.contrib import admin

# Register your models here.
from .models import Post, Picture, Comment

admin.site.register(Post)
admin.site.register(Picture)
admin.site.register(Comment)

