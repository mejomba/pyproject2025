import pytest
from django.utils import timezone
from blog.models.post import Post
from tests.factories.blog import PostFactory, CategoryFactory

pytestmark = pytest.mark.django_db

def test_post_slug_and_excerpt_autofill():
    p = PostFactory(title="Hello World", content="A " * 350)
    assert p.slug  # auto-filled
    assert p.excerpt  # auto-filled from content
    assert len(p.excerpt) <= 350  # rough upper bound from our saver (300-350)

def test_publish_sets_publish_at_if_missing():
    p = PostFactory(status=Post.STATUS_DRAFT, publish_at=None)
    # move to published
    p.status = Post.STATUS_PUBLISHED
    p.save()
    assert p.publish_at is not None
    assert p.publish_at <= timezone.now()

def test_published_manager_filters_by_status_and_time():
    PostFactory(status=Post.STATUS_DRAFT)
    future = timezone.now() + timezone.timedelta(days=1)
    PostFactory(status=Post.STATUS_PUBLISHED, publish_at=future)  # future -> not public yet
    past = timezone.now() - timezone.timedelta(days=1)
    p_pub = PostFactory(status=Post.STATUS_PUBLISHED, publish_at=past)
    qs = Post.published.all()
    assert p_pub in qs
    assert qs.filter(id=p_pub.id).exists()
    assert qs.count() == 1

def test_reading_time_property():
    p = PostFactory(content=("word " * 600).strip())
    # 600 words ~ 3 minutes with 200 wpm
    assert p.reading_time_minutes >= 3

def test_category_slug_and_parent_soft_delete_cascade():
    parent = CategoryFactory(title="Parent Cat")
    child = CategoryFactory(title="Child Cat", parent=parent)
    assert child.parent_id == parent.id
    # soft delete parent should cascade to related with is_deleted (Category inherits abstract model)
    parent.delete()
    parent.refresh_from_db()
    child.refresh_from_db()
    assert parent.is_deleted is True
    assert child.is_deleted is True
