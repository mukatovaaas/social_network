from .models import *
from rest_framework import serializers
from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('follower', 'username')

    username = serializers.ReadOnlyField(source='following.username')


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('following', 'username')

    username = serializers.ReadOnlyField(source='following.username')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user', 'content', 'created_at')

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('user', 'post', 'username')

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    username = serializers.ReadOnlyField(source='user.username')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'post', 'content')

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('follower', 'following')

    follower = serializers.HiddenField(default=serializers.CurrentUserDefault())


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            'id',
            'username',
            'is_following'
        )
        read_only_fields = ('username',)

    is_following = serializers.SerializerMethodField(read_only=True)

    def get_is_following(self, obj):
        user = self.context['request'].user
        return True if Follower.objects.filter(follower=user, following=obj) else False


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('sender', 'recipient', 'message', 'created_at')
        read_only_fields = ('created_at',)

    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())