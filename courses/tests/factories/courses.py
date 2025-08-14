import factory
from courses.models.course import Course
from courses.models.module import Module
from courses.models.lesson import Lesson
from courses.tests.factories.users import InstructorFactory

class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course
    title = factory.Sequence(lambda n: f"Course {n}")
    slug = factory.Sequence(lambda n: f"course-{n}")
    description = "desc"
    instructor = factory.SubFactory(InstructorFactory)
    status = "published"

class ModuleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Module
    course = factory.SubFactory(CourseFactory)
    title = factory.Sequence(lambda n: f"Module {n}")
    order = factory.Sequence(int)

class LessonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Lesson
    module = factory.SubFactory(ModuleFactory)
    title = factory.Sequence(lambda n: f"Lesson {n}")
    order = factory.Sequence(int)
    kind = "article"
