from rest_framework import serializers
from . from models


class ImageSerializer(serializers.Serializer):

    class Meta:
        model = models.Image
        fields = '__all__'


class CommentSerializer(serializers.Serializer):

    class Meta:
        model = models.Comment
        fields = '__all__'


class LikeSerializer(serializers.Serializer):

    class Meta:
        model = models.Like
        fields = '__all__'
