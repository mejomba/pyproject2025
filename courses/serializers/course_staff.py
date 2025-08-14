from rest_framework import serializers
from courses.models.course_staff import CourseStaff

class CourseStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseStaff
        fields = ['id','course','user','role','created_at']
        read_only_fields = ['id','created_at']
