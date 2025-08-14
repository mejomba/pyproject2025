from rest_framework import viewsets, mixins
from django.shortcuts import get_object_or_404
from courses.models.course_staff import CourseStaff
from courses.serializers.course_staff import CourseStaffSerializer
from courses.models.course import Course
from courses.permissions import IsCourseInstructorOrMentor


class CourseStaffViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = CourseStaffSerializer
    permission_classes = [IsCourseInstructorOrMentor]

    def get_course(self):
        course_id = self.kwargs.get('course_pk') or self.kwargs.get('pk')
        return get_object_or_404(Course, pk=course_id)

    def get_queryset(self):
        return CourseStaff.objects.filter(course=self.get_course())

    def perform_create(self, serializer):
        serializer.save(course=self.get_course())
