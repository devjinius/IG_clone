from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

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

        print(image_id)
        return Response(status=200)

# this is test
# class ListAllImage(APIView):

#     def get(self, request, format=None):
#         # ORM으로 가져오고(model), serelize해서 반환

#         all_images = models.Image.objects.all()

#         serializedImages = serializers.ImageSerializer(all_images, many=True)

#         return Response(data=serializedImages.data)

# class ListAllComments(APIView):

#     def get(self, request, format=None):

#         all_comments = models.Comment.objects.filter(creator=request.user.id)

#         serializedComments = serializers.CommentSerializer(all_comments, many=True)

#         return Response(data=serializedComments.data)

# class ListAllLikes(APIView):

#     def get(self, request, format=None):

#         all_likes = models.Like.objects.all()

#         serializedLikes = serializers.LikeSerializer(all_likes, many=True)

#         return Response(data=serializedLikes.data)
