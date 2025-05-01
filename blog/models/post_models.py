from django.db import models
from core.models import AbstractCommWithUserModel
from django.contrib.auth import get_user_model

from core.utils import Utils


User = get_user_model()


class Post(AbstractCommWithUserModel):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to=Utils.generic_image_path, null=True, blank=True)
