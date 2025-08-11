# courses/models/lesson.py
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from core.models import AbstractCommWithUserModel


class Lesson(AbstractCommWithUserModel):
    KIND_CHOICES = [
        ('video','Video'),('article','Article'),('image','Image'),('quiz','Quiz'),('assignment','Assignment'),('project','Project'),
    ]
    kind = models.CharField(max_length=30, choices=KIND_CHOICES, default='article')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type','object_id')
    module = models.ForeignKey('courses.Module', on_delete=models.DO_NOTHING, related_name='lessons')
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='courses/videos/', null=True, blank=True)
    content = models.TextField(blank=True)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.module.title} - {self.title}"