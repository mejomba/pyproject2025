
import pytest
from courses.tests.factories.courses import CourseFactory, ModuleFactory, LessonFactory


pytestmark = pytest.mark.django_db

def test_active_manager_excludes_soft_deleted():
    c = CourseFactory()
    Model = type(c)
    assert Model.objects.filter(id=c.id).exists()
    c.delete()
    assert not Model.objects.filter(id=c.id).exists()
    assert Model.all_objects.filter(id=c.id).exists()


def test_soft_delete_cascade_related_if_supported():
    m = ModuleFactory()
    l1 = LessonFactory(module=m)
    l2 = LessonFactory(module=m)
    m.delete()
    m.refresh_from_db()
    l1.refresh_from_db()
    l2.refresh_from_db()
    assert m.is_deleted is True
    assert getattr(l1, "is_deleted", False) is True
    assert getattr(l2, "is_deleted", False) is True
