from rest_framework import serializers
from courses.models.content import VideoContent, ArticleContent, ImageContent

class VideoContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoContent
        fields = ['id','file','duration','caption']

class ArticleContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleContent
        fields = ['id','body']

class ImageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageContent
        fields = ['id','image','caption']
