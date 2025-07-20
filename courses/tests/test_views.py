import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from courses.models.course import Course
from django.contrib.auth import get_user_model


User = get_user_model()


@pytest.mark.django_db
class TestCourseAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.user = User.objects.create_user(phone='09121234570', password='pass123')
        self.client.force_authenticate(self.user)
        self.list_url = reverse('courses:course-list')

    def test_list_courses_initially_empty(self):
        response = self.client.get(self.list_url)
        assert response.status_code == 200
        assert response.data == []

    def test_create_course(self):
        data = {'title': 'API Course', 'description': 'Desc', 'price': 10.0, 'instructor': self.user.id}
        response = self.client.post(self.list_url, data, format='json')
        assert response.status_code == 201
        assert Course.objects.filter(title='API Course').exists()

    def test_retrieve_course(self):
        course = Course.objects.create(title='Ret', description='D', instructor=self.user)
        url = reverse('courses:course-detail', args=[course.pk])
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data['title'] == 'Ret'

    def test_update_course(self):
        course = Course.objects.create(title='Up', description='D', instructor=self.user)
        url = reverse('courses:course-detail', args=[course.pk])
        response = self.client.patch(url, {'title': 'Updated'}, format='json')
        assert response.status_code == 200
        course.refresh_from_db()
        assert course.title == 'Updated'

    def test_soft_delete_course(self):
        course = Course.objects.create(title='Del', description='D', instructor=self.user)
        url = reverse('courses:course-detail', args=[course.pk])
        response = self.client.delete(url)
        assert response.status_code == 204
        course.refresh_from_db()
        assert course.is_deleted is True

    def test_unauthenticated_cannot_create(self):
        client = APIClient()  # not authenticated
        response = client.post(self.list_url, {'title': 'X', 'description': 'Y'}, format='json')
        assert response.status_code == 401
