# courses/models/lesson.py
from django.db import models
from core.models import AbstractCommWithUserModel


class Lesson(AbstractCommWithUserModel):
    module = models.ForeignKey('courses.Module', on_delete=models.DO_NOTHING, related_name='lessons')
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='courses/videos/', null=True, blank=True)
    content = models.TextField(blank=True)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.module.title} - {self.title}"