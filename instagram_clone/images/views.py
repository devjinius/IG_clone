from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from rest_framework import status

# feed는 팔로잉 한 유저의 가장 최근 사진이 타임라인에 올라온다.


class Feed(APIView):

    def get(self, request, format=None):

        # 팔로잉 한 유저목록을 먼저 불러오자.
        user = request.user
        following_users = user.following.all()

        image_list = []

        for following_user in following_users:

            user_images = following_user.images.all()[:2]

            for image in user_images:

                image_list.append(image)

        sorted_list = sorted(image_list, key=get_key, reverse=True)

        serializedImages = serializers.ImageSerializer(sorted_list, many=True)

        return Response(data=serializedImages.data)


def get_key(image):
    return image.created_at


class LikeImage(APIView):

    def get(self, request, image_id, format=None):

        cur_user = request.user

        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            pre_existing_like = models.Like.objects.get(
                creator=cur_user,
                image=found_image
            )

            pre_existing_like.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Like.DoesNotExist:

            models.Like.objects.create(
                creator=cur_user,
                image=found_image
            )

        return Response(status=status.HTTP_201_CREATED)


class LikeImage(APIView):

    def get(self, request, image_id, format=None):

        cur_user = request.user

        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            pre_existing_like = models.Like.objects.get(
                creator=cur_user,
                image=found_image
            )

            pre_existing_like.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Like.DoesNotExist:

            models.Like.objects.create(
                creator=cur_user,
                image=found_image
            )

        return Response(status=status.HTTP_201_CREATED)


class CreateComment(APIView):

    def post(self, request, image_id, format=None):

        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.CommentSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(
                creator=request.user,
                image=found_image
            )

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=200)


class Comment(APIView):

    def delete(self, request, comment_id, format=None):

        try:
            comment = models.Comment.objects.get(id=comment_id, creator=request.user)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class Search(APIView):

    def get(self, request, format=None):

        hashtags = request.query_params.get('hashtags', None)

        if hashtags is not None:

            hashtags = hashtags.split(",")

            images = models.Image.objects.filter(tags__name__in=hashtags).distinct()

            serializer = serializers.UserProfileImageSerializer(images, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)
