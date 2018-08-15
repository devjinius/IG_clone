# python object를 json으로 변형해주는 것이 serializers
from rest_framework import serializers
from . import models
from instagram_clone.users import models as user_model
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)


class SmallImageSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Image
        fields = (
            'file',
        )


class UserProfileImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'comments_count',
            'likes_count'
        )


class FeedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model.User
        fields = (
            'username',
            'profile_image'
        )


class CommentSerializer(serializers.ModelSerializer):

    creator = FeedUserSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator',
            'image'
        )


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = '__all__'


class ImageSerializer(TaggitSerializer, serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    creator = FeedUserSerializer()
    tags = TagListSerializerField()

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'created_at',
            'likes_count',
            'creator',
            'tags',
            # hidden field -> 이 이미지에 belongs to 된 comments
            # 기본적으로는 comment_set
            'comments'
        )


class InputImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = (
            'file',
            'location',
            'caption',
        )
