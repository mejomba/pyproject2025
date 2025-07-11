from rest_framework import serializers
from ..models.lesson import Lesson


class LessonSerializer(serializers.ModelSerializer):
    """
    Serializer for Lesson model.

    Fields:
        id, module, title, video, content, order,
        created_at, updated_at, creator_user, editor_user.
    """

    class Meta:
        model = Lesson
        fields = [
            'id', 'module', 'title', 'video', 'content', 'order',
            'created_at', 'updated_at',
            'creator_user', 'editor_user'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'creator_user', 'editor_user']
