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

# # Courses
# <URLPattern '^courses/$' [name='course-list']>
# <URLPattern '^courses/(?P<pk>[^/.]+)/$' [name='course-detail']>
#
# # Modules
# <URLPattern '^courses/(?P<course_pk>[^/.]+)/modules/$' [name='course-modules-list']>
# <URLPattern '^courses/(?P<course_pk>[^/.]+)/modules/(?P<pk>[^/.]+)/$' [name='course-modules-detail']>
#
# # Staff
# <URLPattern '^courses/(?P<course_pk>[^/.]+)/staff/$' [name='course-staff-list']>
# <URLPattern '^courses/(?P<course_pk>[^/.]+)/staff/(?P<pk>[^/.]+)/$' [name='course-staff-detail']>
#
# # Graded Spec
# <URLPattern '^courses/(?P<course_pk>[^/.]+)/graded-spec/$' [name='course-graded-spec-list']>
# <URLPattern '^courses/(?P<course_pk>[^/.]+)/graded-spec/(?P<pk>[^/.]+)/$' [name='course-graded-spec-detail']>
#
# # Grades
# <URLPattern '^courses/(?P<course_pk>[^/.]+)/grades/$' [name='course-grades-list']>
# <URLPattern '^courses/(?P<course_pk>[^/.]+)/grades/(?P<pk>[^/.]+)/$' [name='course-grades-detail']>
#
# # Lessons
# <URLPattern '^courses/(?P<course_pk>[^/.]+)/modules/(?P<module_pk>[^/.]+)/lessons/$' [name='module-lessons-list']>
# <URLPattern '^courses/(?P<course_pk>[^/.]+)/modules/(?P<module_pk>[^/.]+)/lessons/(?P<pk>[^/.]+)/$' [name='module-lessons-detail']>
