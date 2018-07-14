from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from instagram_clone.users import models as user_model


@python_2_unicode_compatible
class TimeStampModel (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Image(TimeStampModel):
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_model.User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)


@python_2_unicode_compatible
class Comment(TimeStampModel):
    message = models.TextField()
    creator = models.ForeignKey(user_model.User, on_delete=models.PROTECT, null=True)
    image = models.ForeignKey(Image, on_delete=models.PROTECT, null=True, related_name='comments')


@python_2_unicode_compatible
class Like(TimeStampModel):
    creator = models.ForeignKey(user_model.User, on_delete=models.PROTECT, null=True)
    image = models.ForeignKey(Image, on_delete=models.PROTECT, null=True, related_name='likes')

    def __str__(self):
        return '{} {}'.format(self.creator.username, self.image.caption)
