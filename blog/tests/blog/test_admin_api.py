import pytest
from django.urls import reverse
from blog.models.post import Post
from blog.tests.factories.users import UserFactory, AdminFactory
from blog.tests.factories.blog import PostFactory

pytestmark = pytest.mark.django_db

ADMIN_LIST = "blog:blog-admin-posts-list"
ADMIN_DETAIL = "blog:blog-admin-posts-detail"


def test_author_can_create_post(api_client):
    user = UserFactory()
    api_client.force_authenticate(user=user)
    url = reverse(ADMIN_LIST)
    payload = {"title": "My Post", "content": "Body", "status": Post.STATUS_DRAFT}
    res = api_client.post(url, payload, format="json")
    assert res.status_code in (200, 201)


def test_non_owner_cannot_update_others_post(api_client):
    owner = UserFactory()
    other = UserFactory()
    post = PostFactory(author=owner, title="Initial")
    api_client.force_authenticate(user=other)
    url = reverse(ADMIN_DETAIL, kwargs={"pk": post.pk})
    res = api_client.patch(url, {"title": "Hack!"}, format="json")
    assert res.status_code in (403, 404)


def test_admin_can_update_any_post(api_client):
    owner = UserFactory()
    admin = AdminFactory()
    post = PostFactory(author=owner, title="Initial")
    api_client.force_authenticate(user=admin)
    url = reverse(ADMIN_DETAIL, kwargs={"pk": post.pk})
    res = api_client.patch(url, {"title": "Edited by admin"}, format="json")
    assert res.status_code in (200, 202)
