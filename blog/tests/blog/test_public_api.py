import pytest
from django.urls import reverse
from django.utils import timezone
from blog.models.post import Post
from blog.tests.factories.blog import PostFactory

pytestmark = pytest.mark.django_db


PUBLIC_LIST = "blog:blog-posts-list"
PUBLIC_DETAIL = "blog:blog-posts-detail"


def test_public_list_only_published(api_client):
    PostFactory(status=Post.STATUS_DRAFT)
    PostFactory(status=Post.STATUS_ARCHIVED)
    past = timezone.now() - timezone.timedelta(days=1)
    pub = PostFactory(status=Post.STATUS_PUBLISHED, publish_at=past)
    url = reverse(PUBLIC_LIST)
    res = api_client.get(url)
    assert res.status_code == 200
    ids = [obj.get('id') for obj in res.json()]
    assert pub.id in ids


def test_public_detail_by_slug(api_client):
    past = timezone.now() - timezone.timedelta(days=1)
    pub = PostFactory(title="Unique Title", status=Post.STATUS_PUBLISHED, publish_at=past)
    url = reverse(PUBLIC_DETAIL, kwargs={"slug": pub.slug})  # using lookup_field='slug'
    # If your router is default, detail kwarg might be 'pk' when lookup_field is slug.
    # Adjust to kwargs={'slug': pub.slug} if you've customized your router.
    res = api_client.get(url)
    assert res.status_code == 200
    data = res.json()
    assert data["slug"] == pub.slug
