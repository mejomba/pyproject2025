
import pytest
from django.urls import reverse
from courses.tests.factories.users import UserFactory, StudentFactory
from courses.tests.factories.courses import CourseFactory


pytestmark = pytest.mark.django_db

def test_instructor_can_add_mentor(api_client):
    course = CourseFactory()
    instructor = course.instructor
    api_client.force_authenticate(user=instructor)
    mentor = UserFactory()
    url = reverse("courses:course-staff-list", kwargs={"course_pk": course.id})
    res = api_client.post(url, {"user": mentor.id, "role": "mentor", "course": course.id}, format="json")
    assert res.status_code in (200, 201)


def test_student_cannot_add_mentor(api_client):
    course = CourseFactory()
    student = StudentFactory()
    api_client.force_authenticate(user=student)
    url = reverse("courses:course-staff-list", kwargs={"course_pk": course.id})
    res = api_client.post(url, {"user": student.id, "role": "mentor"}, format="json")
    assert res.status_code in (401, 403)
