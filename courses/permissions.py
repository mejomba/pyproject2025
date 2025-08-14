from rest_framework.permissions import BasePermission, SAFE_METHODS

from courses.models import CourseStaff


class IsCourseInstructorOrMentor(BasePermission):
    def has_permission(self, request, view):
        if request.method in ('GET','HEAD','OPTIONS'):
            return True
        get_course = getattr(view, 'get_course', None)
        if not get_course:
            return False
        course = get_course()
        if not course:
            return False
        user = request.user
        if not user or not user.is_authenticated:
            return False
        if getattr(course, 'instructor_id', None) == user.id:
            return True
        return course.staff.filter(user_id=user.id, role='mentor').exists()

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            # اگر مدل Course هست، باید published باشه یا کاربر staff باشه
            if hasattr(obj, "status") and getattr(obj, "status", None) == "published":
                return True
            return self._is_staff(request.user, obj)
        return self._is_staff(request.user, obj)

    def _is_staff(self, user, obj):
        course = self._get_course(obj)
        if not course:
            return False
        if getattr(course, "instructor_id", None) == user.id:
            return True
        return CourseStaff.objects.filter(course=course, user=user, role="mentor").exists()

    def _get_course(self, obj):
        # هندل انواع مدل: Course/Module/Lesson
        from .models.course import Course
        from .models.module import Module
        from .models.lesson import Lesson
        if isinstance(obj, Course):
            return obj
        if isinstance(obj, Module):
            return obj.course
        if isinstance(obj, Lesson):
            return obj.module.course
        return None
