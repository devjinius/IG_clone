from django.urls import path
from . import views

app_name = "images"

urlpatterns = [
    # url has 3 param
    # regex, view, name
    path("", view=views.Images.as_view(), name="feed"),
    path("<int:image_id>", view=views.ImageDetail.as_view(), name="show_image"),
    path("<int:image_id>/likes/", view=views.LikeImage.as_view(), name="like_image"),
    path("<int:image_id>/comments/", view=views.CreateComment.as_view(), name="create_comment"),
    path("<int:image_id>/comments/<int:comment_id>", view=views.ModerateComments.as_view(), name="delete_comment"),
    path("comments/<int:comment_id>/", view=views.Comment.as_view(), name="comment"),
    path("search/", view=views.Search.as_view(), name="search"),
]
