from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from taggit.managers import TaggableManager
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
    creator = models.ForeignKey(user_model.User, on_delete=models.PROTECT, null=True, related_name='images')
    tags = TaggableManager()

    # 프로퍼티는 펑션이다.
    # 프로퍼티는 필드인데 데이터로 가지는 않고 모델에 들어만 있다.
    @property
    def likes_count(self):
        return self.likes.all().count()

    @property
    def comments_count(self):
        return self.comments.all().count()

    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)

    class Meta:
        ordering = ['-created_at']


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
