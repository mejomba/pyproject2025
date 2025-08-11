from django.conf import settings
from django.db import models
from core.models import AbstractCommWithUserModel


class GradedSpec(AbstractCommWithUserModel):
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='grading_rules')
    lesson = models.OneToOneField('courses.Lesson', on_delete=models.CASCADE, related_name='graded_spec')
    weight = models.DecimalField(max_digits=5, decimal_places=2)

class Grade(AbstractCommWithUserModel):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='grades')
    graded_spec = models.ForeignKey('courses.GradedSpec', on_delete=models.CASCADE, related_name='grades')
    awarded_points = models.DecimalField(max_digits=6, decimal_places=2)
    max_points = models.DecimalField(max_digits=6, decimal_places=2)
    graded_at = models.DateTimeField(auto_now=True)
