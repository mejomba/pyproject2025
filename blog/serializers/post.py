from rest_framework import serializers
from blog.models.post import Post


class PostListSerializer(serializers.ModelSerializer):
    reading_time = serializers.IntegerField(source="reading_time_minutes", read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "slug", "excerpt", "thumbnail", "publish_at", "reading_time", "category", "author",
                  "status"]


class PostDetailSerializer(serializers.ModelSerializer):
    reading_time = serializers.IntegerField(source="reading_time_minutes", read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "slug", "content", "excerpt", "thumbnail", "publish_at", "reading_time",
                  "seo_title", "seo_description", "category", "author", "status"]


class PostWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "slug", "content", "excerpt", "thumbnail", "publish_at", "seo_title",
                  "seo_description", "category", "status", "is_featured"]
