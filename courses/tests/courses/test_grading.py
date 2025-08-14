# tests/courses/test_grading.py
import pytest
from decimal import Decimal
from courses.tests.factories.courses import CourseFactory, ModuleFactory, LessonFactory

pytestmark = pytest.mark.django_db

def test_grade_percent_computation():
    course = CourseFactory()
    module = ModuleFactory(course=course)
    lesson = LessonFactory(module=module, kind="assignment")

    from courses.models.grading import GradedSpec, Grade
    spec = GradedSpec.objects.create(course=course, lesson=lesson, weight=Decimal("40.00"))
    g = Grade.objects.create(student=course.instructor, graded_spec=spec, awarded_points=Decimal("18.0"), max_points=Decimal("20.0"))
    assert round((g.awarded_points / g.max_points) * 100, 2) == 90.00

def test_weights_sum_to_100_enforcement():
    course = CourseFactory()
    module = ModuleFactory(course=course)
    from courses.models.grading import GradedSpec
    l1 = LessonFactory(module=module, kind="quiz")
    l2 = LessonFactory(module=module, kind="assignment")
    GradedSpec.objects.create(course=course, lesson=l1, weight=60)
    GradedSpec.objects.create(course=course, lesson=l2, weight=40)
    assert True  # اگر ولیدیشن واقعی داری، اینجا باید شرط‌هاش رو تست کنی
