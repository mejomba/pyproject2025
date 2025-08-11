from rest_framework.permissions import BasePermission


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
