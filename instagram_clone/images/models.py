from django.db import models
from instagram_clone.users import models as user_model


class TimeStampModel (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Image(TimeStampModel):
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_model.User, on_delete=models.PROTECT, null=True)


class Comment(TimeStampModel):
    message = models.TextField()
    creator = models.ForeignKey(user_model.User, on_delete=models.PROTECT, null=True)
    image = models.ForeignKey(Image, on_delete=models.PROTECT, null=True)


class Like(TimeStampModel):
    creator = models.ForeignKey(user_model.User, on_delete=models.PROTECT, null=True)
    image = models.ForeignKey(Image, on_delete=models.PROTECT, null=True)
