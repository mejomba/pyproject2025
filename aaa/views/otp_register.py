# aaa/views/auth/otp_register.py
from rest_framework.views import APIView
from rest_framework.response import Response
from aaa.models import CustomUser
from aaa.models.otp import OTP
from aaa.serializers.auth_signup import SignupSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone

class OtpRegisterAPIView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        code = request.data.get('code')

        if not phone or not code:
            return Response({'detail': 'phone and code are required.'}, status=400)

        try:
            otp = OTP.objects.get(phone=phone, code=code, is_used=False)
        except OTP.DoesNotExist:
            return Response({'detail': 'کد وارد شده معتبر نیست.'}, status=400)

        if otp.expires_at < timezone.now():
            return Response({'detail': 'کد منقضی شده است.'}, status=400)

        if CustomUser.objects.filter(phone=phone).exists():
            return Response({'detail': 'کاربر از قبل وجود دارد.'}, status=400)

        # ایجاد کاربر
        user = CustomUser.objects.create_user(phone=phone)
        otp.is_used = True
        otp.save()

        # صدور توکن
        refresh = RefreshToken.for_user(user)

        return Response({
            'user': SignupSerializer(user).data,
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }, status=201)
