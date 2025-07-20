import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from aaa.models import CustomUser
from courses.models import Course, Module

pytestmark = pytest.mark.django_db


@pytest.fixture
def instructor_user():
    return CustomUser.objects.create_user(
        phone='09120000002', password='testpass', first_name='Sara', last_name='Instructor')


@pytest.fixture
def course(instructor_user):
    return Course.objects.create(
        title='Django Fundamentals',
        description='Learn Django from scratch',
        instructor=instructor_user,
        creator_user=instructor_user,
        editor_user=instructor_user
    )


@pytest.fixture
def auth_client(instructor_user):
    client = APIClient()
    client.force_authenticate(user=instructor_user)
    return client


def test_create_module(auth_client, course, instructor_user):
    url = reverse('courses:course-modules-list', args=[course.id])
    data = {
        'title': 'Intro to Django',
        'description': 'First steps in Django',
        'course': course.id,
        'order': 1
    }
    response = auth_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    module = Module.objects.get(title='Intro to Django')
    assert module.creator_user == instructor_user
    assert module.editor_user == instructor_user
    assert module.course == course


def test_list_modules(auth_client, course):
    Module.objects.create(title='Mod 1', description='...', course=course, creator_user=course.instructor, editor_user=course.instructor, order=1)
    Module.objects.create(title='Mod 2', description='...', course=course, creator_user=course.instructor, editor_user=course.instructor, order=2)
    url = reverse('courses:course-modules-list', args=[course.id])
    response = auth_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2


def test_retrieve_module(auth_client, course):
    module = Module.objects.create(
        title='Mod Detail', description='...', course=course, order=1,
        creator_user=course.instructor, editor_user=course.instructor
    )
    url = reverse('courses:course-modules-detail', args=[course.id, module.id])
    response = auth_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == module.title


def test_update_module(auth_client, course):
    module = Module.objects.create(
        title='Old Mod', description='...', course=course, order=2,
        creator_user=course.instructor, editor_user=course.instructor
    )
    url = reverse('courses:course-modules-detail', args=[course.id, module.id])
    response = auth_client.patch(url, {'title': 'New Mod'})
    assert response.status_code == status.HTTP_200_OK
    module.refresh_from_db()
    assert module.title == 'New Mod'


def test_soft_delete_module(auth_client, course):
    module = Module.objects.create(
        title='Temp Mod', description='...', course=course, order=1,
        creator_user=course.instructor, editor_user=course.instructor
    )
    url = reverse('courses:course-modules-detail', args=[course.id, module.id])
    response = auth_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    module.refresh_from_db()
    assert module.is_deleted is True
