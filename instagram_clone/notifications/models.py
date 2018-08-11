from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from instagram_clone.users import models as user_models
from instagram_clone.images import models as image_models


@python_2_unicode_compatible
class Notification(image_models.TimeStampModel):

    TYPE_CHOICES = (
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow', 'Follow'),
    )

    creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT, related_name='creator')  # 유저이름
    to = models.ForeignKey(user_models.User, on_delete=models.PROTECT, related_name='to')  # 노티를 받는 사람
    image = models.ForeignKey(image_models.Image, on_delete=models.PROTECT, null=True, blank=True)
    noti_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    comment = models.TextField(null=True, blank=True)
