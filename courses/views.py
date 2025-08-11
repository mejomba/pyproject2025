from logging import raiseExceptions

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Module, Lesson
from .models.course import Course
from .serializers.course import CourseSerializer
from .serializers.lesson import LessonSerializer
from .serializers.module import ModuleSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing, creating, retrieving, updating and soft-deleting Courses.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # درج خودکار creator/editor
        serializer.save(creator_user=self.request.user, editor_user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(editor_user=self.request.user)


class ModuleViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing, creating, retrieving, updating, and soft-deleting Modules within a Course.
    """
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Assign audit fields and link module to instructor on creation.
        """
        serializer.save(
            creator_user=self.request.user,
            editor_user=self.request.user
        )

    def perform_update(self, serializer):
        """
        Update editor_user on module update.
        """
        serializer.save(editor_user=self.request.user)


class LessonViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing, creating, retrieving, updating, and soft-deleting Lessons within a Module.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Assign audit fields on lesson creation.
        """
        serializer.save(
            creator_user=self.request.user,
            editor_user=self.request.user
        )

    def perform_update(self, serializer):
        """
        Update editor_user on lesson update.
        """
        serializer.save(editor_user=self.request.user)
