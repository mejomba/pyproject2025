from rest_framework import serializers
from ..models.module import Module


class ModuleSerializer(serializers.ModelSerializer):
    """
    Serializer for Module model.

    Fields:
        id, course, title, description, order,
        created_at, updated_at, creator_user, editor_user.
    """

    class Meta:
        model = Module
        fields = [
            'id', 'course', 'title', 'description', 'order',
            'created_at', 'updated_at',
            'creator_user', 'editor_user'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'creator_user', 'editor_user']
