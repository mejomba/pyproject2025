from django.db import models
from core.models import AbstractCommWithUserModel


class Module(AbstractCommWithUserModel):
    course = models.ForeignKey('courses.Course', on_delete=models.DO_NOTHING, related_name='modules')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"

