# courses/tests/test_serializers.py
import pytest
from courses.models.course import Course
from courses.serializers.course import CourseSerializer


@pytest.mark.django_db
def test_course_serializer():
    pass
    # course = Course.objects.create(title="Test", description="Desc", instructor_id=1)
    # data = CourseSerializer(course).data
    # assert data['title'] == "Test"
    # assert 'created_at' in data
