from .models import *
from rest_framework import serializers
from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('id', 'username',)

    username = serializers.ReadOnlyField(source='following.username')
    id = serializers.ReadOnlyField(source='following.id')


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('id', 'username')

    username = serializers.ReadOnlyField(source='following.username')
    id = serializers.ReadOnlyField(source='following.id')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'user_', 'content', 'created_at', 'likes', 'is_liked')

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_ = serializers.ReadOnlyField(source='user.username')
    likes = serializers.ReadOnlyField(source='like_set.count')
    is_liked = serializers.SerializerMethodField(read_only=True)

    def get_is_liked(self, obj):
        user = self.context['request'].user
        return bool(Like.objects.filter(post=obj, user=user))


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
        fields = ('sender', 'recipient', 'message', 'created_at', 'sender_', 'recipient_')
        read_only_fields = ('created_at', 'sender_', 'recipient_')

    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())
    recipient_ = serializers.ReadOnlyField(source='recipient.username')
    sender_ = serializers.ReadOnlyField(source='sender.username')
    created_at = serializers.DateTimeField(format="%Y %B %d at %H:%M", read_only=True)
