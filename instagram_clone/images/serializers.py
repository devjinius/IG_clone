# python object를 json으로 변형해주는 것이 serializers
from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    likes = LikeSerializer(many=True)

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',

            # hidden field -> 이 이미지에 belongs to 된 comments
            # 기본적으로는 comment_set
            'comments',
            'likes'
        )
