# python object를 json으로 변형해주는 것이 serializers
from rest_framework import serializers
from instagram_clone.images  import serializers as image_serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):

    images = image_serializers.UserProfileImageSerializer(many=True)

    class Meta:
        model = models.User

        fields = (
            'username',
            'name',
            'bio',
            'website',
            'post_count',
            'followers_count',
            'following_count',
            'images'
        )


class ExploreUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'id',
            'profile_image',
            'username',
            'name'
        )
