from . import serializers
from rest_framework import generics, mixins, permissions
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.utils.translation import gettext as _


class FollowerListView(generics.ListAPIView):
    serializer_class = serializers.FollowerSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Follower.objects.filter(following=self.request.user)


class FollowingListView(generics.ListAPIView):
    serializer_class = serializers.FollowerSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Follower.objects.filter(follower=self.request.user)


class PostListView(generics.ListAPIView):
    serializer_class = serializers.PostSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Post.objects.filter(
            user_id=self.kwargs.get('pk'),
        ).order_by('-created_at')
        return queryset


class MyPostListView(generics.ListAPIView):
    serializer_class = serializers.PostSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user).order_by('-created_at')


class PostView(generics.CreateAPIView):
    serializer_class = serializers.PostSerializer

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)


class PostLikesListView(generics.ListCreateAPIView):
    serializer_class = serializers.LikeSerializer

    def get_queryset(self):
        return Like.objects.filter(post_id=self.kwargs.get('pk'))


class PostCommentsListView(generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs.get('pk'))
