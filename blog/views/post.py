# blog/views/post.py
from rest_framework import viewsets, permissions, filters
from blog.models.post import Post
from blog.serializers.post import PostListSerializer, PostDetailSerializer, PostWriteSerializer

from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiExample


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and (request.user.is_staff or obj.author_id == request.user.id)


class PublicPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.published.all().select_related("author", "category")
    serializer_class = PostListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "excerpt", "content"]
    ordering = ["-publish_at"]

    def get_serializer_class(self):
        return PostDetailSerializer if self.action == "retrieve" else PostListSerializer

    lookup_field = "slug"


class AdminPostViewSet(viewsets.ModelViewSet):
    queryset = Post.all_objects.select_related("author", "category")  # دسترسی کامل
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwner]

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return PostDetailSerializer
        return PostWriteSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, creator_user=self.request.user)

    @extend_schema(tags=['jafar'], examples=[
        OpenApiExample(
            "CreateCourseExample",
            summary="Minimal payload",
            description="نمونه ساده برای ساخت دوره",
            value={"title": "Django 101", "slug": "django-101"},
        )
    ])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
