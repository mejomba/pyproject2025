
import pytest
from django.urls import reverse
from courses.tests.factories.users import UserFactory
from courses.tests.factories.courses import CourseFactory, ModuleFactory


pytestmark = pytest.mark.django_db

def test_mentor_can_create_lesson_in_their_course(api_client):
    course = CourseFactory()
    mentor = UserFactory()
    from courses.models.course_staff import CourseStaff
    CourseStaff.objects.create(course=course, user=mentor, role="mentor")
    api_client.force_authenticate(user=mentor)
    module = ModuleFactory(course=course)
    data = {
        'title': 'Lesson 1',
        'content': 'Content of lesson 1',
        'module': module.id,
        'order': 1
    }
    url = reverse("courses:module-lessons-list", kwargs={"course_pk": course.id, "module_pk": module.id})
    res = api_client.post(url, data, format="json")
    assert res.status_code in (200, 201)
