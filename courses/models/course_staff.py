from django.conf import settings
from django.db import models
from core.models import AbstractCommWithUserModel

class CourseStaff(AbstractCommWithUserModel):
    MENTOR = 'mentor'
    ROLE_CHOICES = [(MENTOR, 'Mentor')]
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='staff')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='course_staff')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    class Meta:
        unique_together = (('course','user','role'),)
