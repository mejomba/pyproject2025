from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from courses.models.grading import GradedSpec, Grade
from courses.serializers.grading import GradedSpecSerializer, GradeSerializer
from courses.models.course import Course
from courses.permissions import IsCourseInstructorOrMentor

class GradedSpecViewSet(viewsets.ModelViewSet):
    serializer_class = GradedSpecSerializer
    permission_classes = [IsCourseInstructorOrMentor]

    def get_course(self):
        course_id = self.kwargs.get('course_pk')
        return get_object_or_404(Course, pk=course_id)

    def get_queryset(self):
        return GradedSpec.objects.filter(course=self.get_course())

    def perform_create(self, serializer):
        serializer.save(course=self.get_course())

class GradeViewSet(viewsets.ModelViewSet):
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Grade.objects.all()
        course_id = self.kwargs.get('course_pk')
        if course_id:
            qs = qs.filter(graded_spec__course_id=course_id)
        if not self.request.user.is_staff:
            qs = qs.filter(student_id=self.request.user.id)
        return qs
