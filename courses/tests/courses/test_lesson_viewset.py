# courses/tests/test_lesson_viewset.py
import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from aaa.models import CustomUser
from courses.models import Course, Module, Lesson

pytestmark = pytest.mark.django_db


@pytest.fixture
def instructor_user():
    return CustomUser.objects.create_user(
        phone='09120000003', password='testpass', first_name='Ali', last_name='Instructor')


@pytest.fixture
def course(instructor_user):
    return Course.objects.create(
        title='Fullstack Web',
        description='Frontend + Backend',
        instructor=instructor_user,
        creator_user=instructor_user,
        editor_user=instructor_user
    )


@pytest.fixture
def module(course):
    instructor = course.instructor
    return Module.objects.create(
        title='Backend Basics',
        description='Intro to backend',
        course=course,
        creator_user=instructor,
        editor_user=instructor,
        order=1
    )


@pytest.fixture
def auth_client(instructor_user):
    client = APIClient()
    client.force_authenticate(user=instructor_user)
    return client


def test_create_lesson(auth_client, course, module):
    url = reverse('courses:module-lessons-list', args=[course.id, module.id])
    data = {
        'title': 'Lesson 1',
        'content': 'Content of lesson 1',
        'module': module.id,
        'order': 1
    }
    response = auth_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    lesson = Lesson.objects.get(title='Lesson 1')
    assert lesson.module == module
    assert lesson.creator_user == module.creator_user


def test_list_lessons(auth_client, course, module):
    Lesson.objects.create(title='L1', content='...', module=module, creator_user=module.creator_user, editor_user=module.creator_user, order=1)
    Lesson.objects.create(title='L2', content='...', module=module, creator_user=module.creator_user, editor_user=module.creator_user, order=2)
    url = reverse('courses:module-lessons-list', args=[course.id, module.id])
    response = auth_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2


def test_retrieve_lesson(auth_client, course, module):
    lesson = Lesson.objects.create(
        title='L Detail', content='...', module=module, order=1,
        creator_user=module.creator_user, editor_user=module.editor_user
    )
    url = reverse('courses:module-lessons-detail', args=[course.id, module.id, lesson.id])
    response = auth_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == lesson.title


def test_update_lesson(auth_client, course, module):
    lesson = Lesson.objects.create(
        title='L Old', content='...', module=module, order=1,
        creator_user=module.creator_user, editor_user=module.editor_user
    )
    url = reverse('courses:module-lessons-detail', args=[course.id, module.id, lesson.id])
    response = auth_client.patch(url, {'title': 'L Updated'})
    assert response.status_code == status.HTTP_200_OK
    lesson.refresh_from_db()
    assert lesson.title == 'L Updated'


def test_soft_delete_lesson(auth_client, course, module):
    lesson = Lesson.objects.create(
        title='L Delete', content='...', module=module, order=1,
        creator_user=module.creator_user, editor_user=module.editor_user
    )
    url = reverse('courses:module-lessons-detail', args=[course.id, module.id, lesson.id])
    response = auth_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    lesson.refresh_from_db()
    assert lesson.is_deleted is True
