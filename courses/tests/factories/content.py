
import factory
from courses.models.content import VideoContent, ArticleContent, ImageContent


class VideoContentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = VideoContent
        skip_postgeneration_save = True

    file = factory.django.FileField(filename="v.mp4")
    duration = 120
    caption = ""

class ArticleContentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ArticleContent
        skip_postgeneration_save = True

    body = "Hello world"

class ImageContentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ImageContent
        skip_postgeneration_save = True

    image = factory.django.ImageField(filename="img.png")
    caption = ""
