from rest_framework import serializers
from ..models.course import Course


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for Course model.

    Fields:
        id, title, slug, description, price, image, category, status,
        created_at, updated_at, creator_user, editor_user.
    """

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'slug', 'description',
            'price', 'image', 'category', 'status',
            'created_at', 'updated_at',
            'creator_user', 'editor_user'
        ]
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at', 'creator_user', 'editor_user']
