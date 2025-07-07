from rest_framework import serializers
from aaa.models.otp import OTP
from aaa.models.user_models import CustomUser


class OTPVerifySerializer(serializers.Serializer):
    phone = serializers.CharField()
    code = serializers.CharField(max_length=6)

    def validate(self, attrs):
        phone = attrs['phone']
        code = attrs['code']

        try:
            otp = OTP.objects.filter(phone=phone, code=code, is_used=False).latest('created_at')
        except OTP.DoesNotExist:
            raise serializers.ValidationError("Invalid or expired OTP.")

        if otp.is_expired():
            raise serializers.ValidationError("OTP has expired.")

        attrs['otp'] = otp
        return attrs

    def create(self, validated_data):
        otp = validated_data['otp']
        otp.is_used = True
        otp.save()

        user, created = CustomUser.objects.get_or_create(phone=otp.phone)
        return user
