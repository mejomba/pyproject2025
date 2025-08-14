import pytest
from django.utils.text import slugify
from courses.models.course import Course
from courses.models.module import Module
from courses.models.lesson import Lesson
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_course_slug_auto_generation():
    instructor = User.objects.create_user(phone='09121234567', password='pass123')
    course = Course.objects.create(
        title="My New Course",
        description="Desc",
        instructor=instructor,
        creator_user=instructor,
        editor_user=instructor
    )
    assert course.slug == slugify("My New Course")


@pytest.mark.django_db
def test_soft_delete_cascade_on_course():
    instructor = User.objects.create_user(phone='09121234568', password='pass123')
    course = Course.objects.create(
        title="Cascade Test",
        description="Desc",
        instructor=instructor,
        creator_user = instructor,
        editor_user = instructor
    )
    module = Module.objects.create(course=course, title="Mod1", order=1, creator_user=instructor, editor_user=instructor)
    lesson = Lesson.objects.create(module=module, title="Les1", order=1, creator_user=instructor, editor_user=instructor)

    # حذف نرم دوره
    course.delete()

    # خودش و وابستگان‌ش باید is_deleted=True شده باشند
    course.refresh_from_db()
    module.refresh_from_db()
    lesson.refresh_from_db()

    assert course.is_deleted is True
    assert module.is_deleted is True
    assert lesson.is_deleted is True
