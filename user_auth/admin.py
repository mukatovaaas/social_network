from django.contrib import admin
from .models import *


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ['follower', 'following']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'created_at']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'content']
