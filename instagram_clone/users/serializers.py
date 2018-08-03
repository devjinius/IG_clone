# python object를 json으로 변형해주는 것이 serializers
from rest_framework import serializers
from . import models


class ExploreUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'profile_image',
            'username',
            'name'
        )
