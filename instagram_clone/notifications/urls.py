from django.urls import path
from . import views

app_name = "notifications"

urlpatterns = [
    path("", view=views.Notification.as_view(), name="notifications"),

]
