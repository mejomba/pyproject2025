from rest_framework.routers import DefaultRouter
from blog.views.post import PublicPostViewSet, AdminPostViewSet

app_name = "blog"
router = DefaultRouter()
router.register(r"posts", PublicPostViewSet, basename="blog-posts")
router.register(r"admin/posts", AdminPostViewSet, basename="blog-admin-posts")

urlpatterns = router.urls
