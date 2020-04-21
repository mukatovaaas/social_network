from .models import *
from rest_framework import serializers


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('follower', 'username')

    username = serializers.ReadOnlyField(source='following.username')


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('following',)

    username = serializers.ReadOnlyField(source='follower.username')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user', 'content', 'created_at')

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
