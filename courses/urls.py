from rest_framework_nested import routers
from .views import CourseViewSet, ModuleViewSet, LessonViewSet
from .views_grading import GradedSpecViewSet, GradeViewSet
from .views_staff import CourseStaffViewSet

app_name = 'courses'

router = routers.SimpleRouter()
router.register(r'courses', CourseViewSet, basename='course')

modules_router = routers.NestedSimpleRouter(router, r'courses', lookup='course')
modules_router.register(r'modules', ModuleViewSet, basename='course-modules')

# Merge with existing routers in courses/urls.py
modules_router.register(r'staff', CourseStaffViewSet, basename='course-staff')
modules_router.register(r'graded-spec', GradedSpecViewSet, basename='course-graded-spec')
modules_router.register(r'grades', GradeViewSet, basename='course-grades')

lessons_router = routers.NestedSimpleRouter(modules_router, r'modules', lookup='module')
lessons_router.register(r'lessons', LessonViewSet, basename='module-lessons')

urlpatterns = router.urls + modules_router.urls + lessons_router.urls

# <URLPattern '^courses/$' [name='course-list']>
# <URLPattern '^courses/(?P<pk>[^/.]+)/$' [name='course-detail']>
# <URLPattern '^courses/(?P<course_pk>[^/.]+)/modules/$' [name='course-modules-list']>
# <URLPattern '^courses/(?P<course_pk>[^/.]+)/modules/(?P<pk>[^/.]+)/$' [name='course-modules-detail']>
# <URLPattern '^courses/(?P<course_pk>[^/.]+)/modules/(?P<module_pk>[^/.]+)/lessons/$' [name='module-lessons-list']>
# <URLPattern '^courses/(?P<course_pk>[^/.]+)/modules/(?P<module_pk>[^/.]+)/lessons/(?P<pk>[^/.]+)/$' [name='module-lessons-detail']>
