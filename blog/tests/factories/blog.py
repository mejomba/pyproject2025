import factory
from core.models import Category
from blog.models.post import Post
from blog.tests.factories.users import UserFactory


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.Sequence(lambda n: f"Category {n}")


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Sequence(lambda n: f"Post {n}")
    author = factory.SubFactory(UserFactory)
    content = "Hello CKEditor-like content"
    status = Post.STATUS_DRAFT
    publish_at = None
