import pytest
from courses.models.course import Course
from courses.serializers.course import CourseSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_course_serializer_output_and_read_only_fields():
    instructor = User.objects.create_user(phone='09121234569', password='pass123')
    course = Course.objects.create(
        title="Serializer Test",
        description="Desc",
        instructor=instructor,
        creator_user=instructor,
        editor_user=instructor
    )
    data = CourseSerializer(course).data

    # خروجی باید شامل فیلدها باشد
    for field in ['id', 'title', 'slug', 'description', 'price', 'status', 'created_at']:
        assert field in data


@pytest.mark.django_db
def test_valid_course_serializer():
    instructor = User.objects.create_user(phone='09121234569', password='pass123')
    data = {
        'title': 'Test Course',
        'description': 'This is a test course.',
        'price': 99.9,
        'image': None,
        'category': '1',
        'status': 'published',
        'instructor': instructor,
        'creator_user': instructor,
        'editor_user': instructor
    }
    serializer = CourseSerializer(data=data)
    assert serializer.is_valid()
    assert 'title' in serializer.validated_data
    assert serializer.validated_data['title'] == 'Test Course'


@pytest.mark.django_db
def test_read_only_fields_are_ignored():
    instructor = User.objects.create_user(phone='09121234569', password='pass123')
    data = {
        'id': 999,
        'description': 'description',
        'title': 'Course With ID',
        'slug': 'should-not-come',
        'created_at': '2022-01-01T00:00:00Z',
        'updated_at': '2022-01-02T00:00:00Z',
        'instructor': instructor,
        'creator_user': instructor,
        'editor_user': instructor
    }
    serializer = CourseSerializer(data=data)
    assert serializer.is_valid()
    for field in ['id', 'slug', 'created_at', 'updated_at', 'creator_user', 'editor_user']:
        assert field not in serializer.validated_data


@pytest.mark.django_db
def test_missing_required_field_title():
    data = {
        'description': 'Missing title',
        'price': 50.0,
        'category': '1',
        'status': 'draft'
    }
    serializer = CourseSerializer(data=data)
    assert not serializer.is_valid()
    assert 'title' in serializer.errors


@pytest.mark.django_db
def test_partial_update_ignores_read_only_fields():
    instructor = User.objects.create_user(phone='09121234569', password='pass123')
    instance = Course.objects.create(
        title='Old Title',
        slug='old-title',
        description='desc',
        price=10,
        category='1',
        status='draft',
        instructor= instructor,
        creator_user= instructor,
        editor_user= instructor
    )
    serializer = CourseSerializer(instance, data={
        'title': 'New Title',
        'id': 1234,
        'slug': 'hacked',
    }, partial=True)

    assert serializer.is_valid()
    updated = serializer.save()

    assert updated.title == 'New Title'
    assert updated.id != 1234  # id shouldn't change
    assert updated.slug == 'old-title'  # read-only

