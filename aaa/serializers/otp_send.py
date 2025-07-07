from rest_framework import serializers
from aaa.models.otp import OTP
from django.utils import timezone
from datetime import timedelta
import random
from django.conf import settings


# noinspection PyAbstractClass
class OTPSendSerializer(serializers.Serializer):
    phone = serializers.CharField()

    def create(self, validated_data):
        code = str(random.randint(10000, 99999))
        expires_at = timezone.now() + timedelta(minutes=settings.OTP_LIFE_TIME)

        otp = OTP.objects.create(
            phone=validated_data['phone'],
            code=code,
            expires_at=expires_at
        )
        # در عمل باید پیامک یا ایمیل ارسال بشه؛ فعلاً فقط چاپش می‌کنیم:
        print(f"[OTP] Code for {otp.phone}: {otp.code}")
        return otp
