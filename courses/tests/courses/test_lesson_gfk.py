
import pytest
from django.contrib.contenttypes.models import ContentType
from courses.tests.factories.courses import LessonFactory
from courses.tests.factories.content import VideoContentFactory, ArticleContentFactory, ImageContentFactory


pytestmark = pytest.mark.django_db

def test_lesson_with_article_content():
    lesson = LessonFactory(kind="article")
    article = ArticleContentFactory()
    lesson.content_type = ContentType.objects.get_for_model(article)
    lesson.object_id = article.id
    lesson.save()
    assert lesson.content_object == article


def test_lesson_with_video_content():
    lesson = LessonFactory(kind="video")
    video = VideoContentFactory()
    lesson.content_type = ContentType.objects.get_for_model(video)
    lesson.object_id = video.id
    lesson.save()
    assert lesson.content_object == video
    assert video.duration > 0


def test_lesson_with_image_content():
    lesson = LessonFactory(kind="image")
    img = ImageContentFactory()
    lesson.content_type = ContentType.objects.get_for_model(img)
    lesson.object_id = img.id
    lesson.save()
    assert lesson.content_object == img
