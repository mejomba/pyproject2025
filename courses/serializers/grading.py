from rest_framework import serializers
from courses.models.grading import GradedSpec, Grade

class GradedSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradedSpec
        fields = ['id','course','lesson','weight']

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id','student','graded_spec','awarded_points','max_points','graded_at']
        read_only_fields = ['id','graded_at']
