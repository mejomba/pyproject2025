import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from aaa.models import CustomUser
from courses.models.course import Course


@pytest.fixture
def instructor_user(db):
    return CustomUser.objects.create_user(phone='09120000001', password='testpass', first_name='Ali', last_name='Instructor')


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def auth_client(api_client, instructor_user):
    api_client.force_authenticate(user=instructor_user)
    return api_client


@pytest.mark.django_db
def test_create_course(auth_client, instructor_user):
    url = reverse('courses:course-list')
    data = {
        'title': 'Python Basics',
        'description': 'A beginner friendly course on Python.',
        'instructor': instructor_user.id,
    }
    response = auth_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Course.objects.count() == 1
    course = Course.objects.first()
    assert course.creator_user == instructor_user
    assert course.editor_user == instructor_user


@pytest.mark.django_db
def test_list_courses(auth_client):
    url = reverse('courses:course-list')
    response = auth_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_retrieve_course(auth_client, instructor_user):
    course = Course.objects.create(
        title='Test Course',
        description='Desc',
        instructor=instructor_user,
        creator_user=instructor_user,
        editor_user=instructor_user
    )
    url = reverse('courses:course-detail', args=[course.id])
    response = auth_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == course.title


@pytest.mark.django_db
def test_update_course(auth_client, instructor_user):
    course = Course.objects.create(
        title='Old Title',
        description='Desc',
        instructor=instructor_user,
        creator_user=instructor_user,
        editor_user=instructor_user
    )
    url = reverse('courses:course-detail', args=[course.id])
    response = auth_client.patch(url, {'title': 'New Title'})
    assert response.status_code == status.HTTP_200_OK
    course.refresh_from_db()
    assert course.title == 'New Title'


@pytest.mark.django_db
def test_soft_delete_course(auth_client, instructor_user):
    course = Course.objects.create(
        title='To Be Deleted',
        description='...',
        instructor=instructor_user,
        creator_user=instructor_user,
        editor_user=instructor_user
    )
    url = reverse('courses:course-detail', args=[course.id])
    response = auth_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    course.refresh_from_db()
    assert course.is_deleted is True
