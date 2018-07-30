from django.urls import path
from . import views

app_name = "images"

urlpatterns = [
    # url has 3 param
    # regex, view, name
    path("", view=views.Feed.as_view(), name="feed")

    # test data
    # path("all/", view=views.ListAllImage.as_view(), name="all_images"),
    # path("comments/", view=views.ListAllComments.as_view(), name="all_comments"),
    # path("likes/", view=views.ListAllLikes.as_view(), name="all_likes"),
]
