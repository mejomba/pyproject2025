from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models.course import Course
from .serializers.course import CourseSerializer


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
