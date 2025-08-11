from django.db import models
from core.models import AbstractCommWithUserModel


class VideoContent(AbstractCommWithUserModel):
    file = models.FileField(upload_to='videos/')
    duration = models.PositiveIntegerField(help_text='seconds')
    caption = models.CharField(max_length=200, blank=True)


class ArticleContent(AbstractCommWithUserModel):
    body = models.TextField()


class ImageContent(AbstractCommWithUserModel):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=200, blank=True)
