from rest_framework import serializers
from courses.models.course_staff import CourseStaff

class CourseStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseStaff
        fields = ['id','course','user','role','joined_at']
        read_only_fields = ['id','joined_at']
